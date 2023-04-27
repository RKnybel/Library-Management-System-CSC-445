from django.db import models

# Create your models here.

class User(models.Model):

    #fields
    UserID = models.CharField(max_length = 6, primary_key = True, unique=True)
    Password = models.CharField(max_length = 100)
    UserFirstName = models.CharField(max_length = 20)
    UserLastName = models.CharField(max_length = 20)
    PhoneNumber = models.CharField(max_length = 6)
    Email = models.EmailField()
    AddressLine1 = models.CharField(max_length = 50)
    AddressLine2 = models.CharField(max_length = 50)
    City = models.CharField(max_length = 50)
    State = models.CharField(max_length = 20)
    ZipCode = models.CharField(max_length = 5)
    UserTypeID = models.ForeignKey('UserType', on_delete=models.SET_DEFAULT, default=0)
    NumBooksLost = models.IntegerField(max_length = 6, default=0)
    TotalFeesDue = models.IntegerField(max_length = 6, default = 0)

class UserType(models.Model):
    UserTypeID = models.CharField(max_length = 5, primary_key=True, unique=True)
    UserType = models.CharField(max_length=20)

class Rental(models.Model):
    UserID = models.ForeignKey('User', on_delete=models.SET_DEFAULT, primary_key=True, default=0)
    ISBN = models.ForeignKey('Book', on_delete=models.SET_DEFAULT, primary_key=True, default=0)
    DateRented = models.DateField()
    RenewalDate = models.DateField()
    FeeIfLate = models.IntegerField()

class Book(models.Model):
    ISBN = models.IntegerField(max_length=13, primary_key=True, unique=True)
    Title = models.CharField(max_length=100)
    NumPages = models.BigIntegerField()
    SeriesID = models.ForeignKey('Series', on_delete=models.SET_DEFAULT, default=0)
    ReleaseDate = models.DateField()
    BookType = models.ForeignKey('BookType', on_delete=models.SET_DEFAULT, default=0, max_length=20)
    Genre = models.ForeignKey('BookGenre', on_delete=models.SET_DEFAULT, default=0)

class BookAuthor(models.Model):
    AuthorID = models.ForeignKey('Author', on_delete=models.SET_DEFAULT, primary_key=True, unique=True, default=0)
    ISBN = models.ForeignKey('Book', on_delete=models.SET_DEFAULT, primary_key=True, default=0)

class Author(models.Model):
    AuthorID = models.CharField(max_length = 10, primary_key=True, unique=True)
    AuthorFirstName = models.CharField(max_length=50)
    AuthorLastName = models.CharField(max_length=50)
    Alive = models.BooleanField()

class Series(models.Model):
    SeriesID = models.IntegerField(primary_key=True, unique=True)
    SeriesName = models.CharField(max_length=50)

class BookType(models.Model):
    BookType = models.CharField(primary_key=True, unique=True, max_length=20)

class BookGenre(models.Model):
    Genre = models.CharField(max_length=50, primary_key=True, unique=True)
