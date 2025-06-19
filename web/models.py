from django.db import models

from django.utils.timezone import now
from datetime import timedelta

membership_plan = (
    ('1year','1year'),
    ('1month','1month'),
)


class Books(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    stock_count = models.IntegerField(default = 1)
    in_stock = models.BooleanField(default = True)
    is_deleted = models.BooleanField(default = False)

    class Meta:
        verbose_name_plural = "Books"

    def update_availability(self):
        self.in_stock = stock_count > 0
        self.save()

    def __str__(self):
        return self.title


class Members(models.Model):
    name = models.CharField(max_length = 200)
    membership = models.CharField(max_length = 255, choices = membership_plan)
    date = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    expiry_date = models.DateTimeField(blank = True, null = True)

    class Meta:
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.name


class Rental(models.Model):
    book = models.ForeignKey('web.Books', on_delete = models.CASCADE)
    user_name = models.ForeignKey('web.Members', on_delete = models.CASCADE)
    rented_date = models.DateTimeField(auto_now_add = True, blank = True , null = True)
    return_date = models.DateTimeField(blank = True, null = True)
    is_returned = models.BooleanField(default = False)
    due_date = models.DateTimeField(blank = True, null = True)
    is_overdue = models.BooleanField(default = False)

    def __str__(self):
        return self.user_name.name


# def mark_overdue_books():
#     rentals = Rental.objects.filter(is_returned=False)
#     for rent in rentals:
#         if now() > rent.due_date:
#             rent.is_overdue = True
#             rent.save(update_fields=['is_overdue'])


