from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

