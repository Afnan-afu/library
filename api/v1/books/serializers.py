from web.models import Books, Rental

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'stock_count', 'author', 'category']


class DeleteBookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ['is_deleted','id']


class RentalSerializer(ModelSerializer):
    book = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Rental
        fields = ['book','user','rented_date','return_date']

    def get_book(self,instance):
        return instance.book.title

    def get_user(self,instance):
        return instance.user_name.name


class OverdueSerializer(ModelSerializer):

    class Meta:
        model = Rental
        fields = ['book','user','rented_date','due_date']


    



