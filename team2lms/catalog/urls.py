from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail')
]


