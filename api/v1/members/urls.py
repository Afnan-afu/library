from django.urls import path
from api.v1.members.views import members, add_member, renew_membership_year,renew_membership_month


urlpatterns = [
    path('', members),
    path('add-member/', add_member),
    path('renew-membership-year/<int:pk>/', renew_membership_year),
    path('renew-membership-month/<int:pk>/', renew_membership_month)

]