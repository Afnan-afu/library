from django.utils.timezone import now
from datetime import timedelta

from web.models import Books, Rental, Members

from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.v1.books.serializers import BookSerializer, RentalSerializer, OverdueSerializer


@api_view(['GET'])
def books(request):
    instances = Books.objects.filter(is_deleted = False, in_stock = True)
    serializer = BookSerializer(instance = instances , many = True)

    response_data = {
        'status_code' : 6000,
        'data': serializer.data
    }
    return Response(response_data)


@api_view(['PUT'])
def update_book(request,pk):
    if Books.objects.filter(id = pk).exists():
        current_book = Books.objects.get(id = pk)
        serializer = BookSerializer(instance = current_book, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status_code' : 6000,
                'message': "Book Successfully Updated"
            }
            return Response(response_data)
        else:
            response_data = {
                'status_code' : 6001,
                'message': "Invalid Data"
            }
            return Response(response_data)
    else:
        response_data = {
            'status_code' : 6001,
            'message' : 'No Books Found'
        }

        return Response(response_data)     


@api_view(['DELETE'])
def delete_book(request,pk):
    if Books.objects.filter(id = pk).exists():
        current_book = Books.objects.get(id = pk)
        current_book.is_deleted = True
        current_book.save()
        response_data = {
            'status_code' : 6000,
            'message' : 'Book Deleted Successfully'
        }
        return Response(response_data)
    else:
        response_data = {
            'status_code' : 6001,
            'message' : 'No Books Found'
        }
        return Response(response_data) 


@api_view(['POST'])
def add_book(request):
    title = request.data.get('title')
    author = request.data.get('author')
    category = request.data.get('category')
    stock_count = request.data.get('stock_count')

    if title and author and category and stock_count:
        created = Books.objects.create(
            title = title,
            author = author,
            category = category,
            stock_count = stock_count
        )
        response_data = {
            'status_code' : 6000,
            'message' : 'Book successfully added'
        }
        return Response(response_data)
    else:
        response_data = {
            'status_code' : 6001,
            'message' : 'all fields are required'
        }    
        return Response(response_data)


@api_view(['GET'])
def rented(request):
    members = Rental.objects.all()
    serializer = RentalSerializer(instance = members, many = True)

    response_data = {
        'status_code' : 6000,
        'data' : serializer.data
    }

    return Response(response_data)


@api_view(['POST'])
def rent_book(request):
    book = request.data.get('book')
    user = request.data.get('user')
    
    if not user or not book:

        response_data = {
            'status_code' : 6001,
            'message' : 'Book name and User is required'
        }
        return Response(response_data)
    
    if not Books.objects.filter(title__iexact = book).exists():

        response_data = {
            'status_code' : 6001,
            'message' : 'Book not found'
        }
        return Response(response_data)
    
    if not Members.objects.filter(name__iexact = user).exists():

        response_data = {
            'status_code' : 6001,
            'message' : 'User dont have a Membership'
        }
        return Response(response_data)
    
    user_instance = Members.objects.get(name__iexact = user)
    book_instance = Books.objects.get(title__iexact = book)

    rented = Rental.objects.create(
        book = book_instance,
        user_name = user_instance,
        due_date = now() + timedelta(days=7)
    
    )

    response_data = {
        'status_code' : 6000,
        'message' : f'Book {book} rented to {user}'
    }
    return Response(response_data)


@api_view(['GET'])
def rent_out(request):

    rented = Rental.objects.filter(is_returned = False)
    serializer = RentalSerializer(instance = rented, many = True)

    response_data  = {
        'status_code' : 6000,
        'data' : serializer.data
    }
    return Response(response_data)


@api_view(['PUT'])
def return_book(request,pk):

    if not Rental.objects.filter(user_name__id = pk, is_returned = False).exists():
        response_data = {   
            'status_code' : 6001,
            'message' : 'User not found or No Rentals'
        }
        return Response(response_data)
    

    rented = Rental.objects.get(user_name__id = pk, is_returned = False)
    user = rented.user_name.name
    rented.return_date = now()
    rented.is_returned = True
    rented.save(update_fields = ['is_returned','return_date'])

    response_data = {
        'status_code' : 6000,
        'message' : f'Book Successfully returned by {user}'
    }

    return Response(response_data)


@api_view(['GET'])
def mark_overdue_books(request):
    rentals = Rental.objects.filter(is_returned=False)

    for rent in rentals:
        if rent.rented_date and now() > rent.rented_date + timedelta(days=7):
            rent.is_overdue = True
            rent.save(update_fields=['is_overdue'])

    overdued_list = Rental.objects.filter(is_overdue=True)
    serializer = OverdueSerializer(overdued_list, many=True)

    if not overdued_list.exists():
        response_data = {
            'status_code': 6001,
            'message': 'No Overdue Books'
        }
    else:
        response_data = {
            'status_code': 6000,
            'data': serializer.data
        }

    return Response(response_data)