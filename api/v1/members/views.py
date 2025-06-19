from datetime import timedelta
from django.utils.timezone import now

from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.v1.members.serializers import MemberSerializer
from web.models import Members


@api_view(['GET'])
def members(request):
    member_list = Members.objects.all()
    serializer = MemberSerializer(instance = member_list, many = True)

    response_data = {
        'status_code' : 6000,
        'data' : serializer.data
    }

    return Response(response_data)


@api_view(['POST'])
def add_member(request):
    name = request.data.get('name')
    membership = request.data.get('membership')

    if name and membership:
        if not Members.objects.filter(name__iexact = name).exists():
            members = Members.objects.create(
                name = name,
                membership = membership 
            )
            if members.membership == '1year':
                members.expiry_date = now() + timedelta(days=365)
            else:
                members.expiry_date = now() + timedelta(days=30)
            
            members.save()

            response_data = {
                'status_code' : 6000,
                'message' : 'Member Successfully Added'
            }
            return Response(response_data)
        else:
            response_data = {
            'status_code' : 6001,
            'message' : 'User is already a Member'
            }
            return Response(response_data)

    else:
        response_data = {
            'status_code' : 6001,
            'message' : 'Name and Membership details required'
        }
        return Response(response_data)



@api_view(['PUT'])
def renew_membership_year(request,pk):
    if Members.objects.filter(id = pk).exists():
        member = Members.objects.get(id = pk)
        member.membership = '1year'
        member.date = now()
        member.expiry_date = now() + timedelta(days = 365)
        member.save()
        response_data = {
            'status_code' : 6000,
            'message' : 'Renewed upto 1Year'
        }
        return Response(response_data)
    else:
        response_data = {
            'status_code' : 6001,
            'message' : 'User not found'
        }
        return Response(response_data)


@api_view(['PUT'])
def renew_membership_month(request,pk):
    if Members.objects.filter(id = pk).exists():
        member = Members.objects.get(id = pk)
        member.membership = '1month'
        member.date = now()
        member.expiry_date = now() + timedelta(days = 30)
        member.save()

        response_data = {
            'status_code' : 6000,
            'message' : 'Renewd upto 1Month'
        }
        return Response(response_data)
    else:
        response_data = {
            'status_code' : 6001,
            'message' : 'User not found'
        }
        
        return Response(response_data)