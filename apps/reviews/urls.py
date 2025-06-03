from django.urls import path
from apps.reviews.views import ReviewCreateView, RentReviewListView

urlpatterns = [
     path('create/', ReviewCreateView.as_view(), name='create-review'),
     path('rent/<int:rent_id>/', RentReviewListView.as_view(), name='rent-reviews'),
]
