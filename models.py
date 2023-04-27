from django.db import models

# Create your models here.

class User(models.Model):

    #fields
    UserID = models.CharField(MaxLength = 6, primary_key = True, unique=True)
    Password = models.CharField(MaxLength = 100)
    UserFirstName = models.CharField(MaxLength = 20)
    UserLastName = models.CharField(MaxLength = 20)
    PhoneNumber = models.CharField(MaxLength = 6)
    Email = models.EmailField()
    AddressLine1 = models.CharField(MaxLength = 50)
    AddressLine2 = models.CharField(MaxLength = 50)
    City = models.CharField(MaxLength = 50)
    State = models.CharField(MaxLength = 20)
    ZipCode = models.CharField(MaxLength = 5)
    UserTypeID = models.ForeignKey('UserType')
    NumBooksLost = models.IntegerField(MaxLength = 6, default=0)
    TotalFeesDue = models.IntegerField(MaxLength = 6, default = 0)

class UserType(models.Model):
    UserTypeID = models.CharField(MaxLength = 5, primary_key=True, unique=True)
    UserType = models.CharField()

class Rental(models.Model):
    UserID = models.ForeignKey('User', primary_key=True)
    ISBN = models.ForeignKey('Book', primary_key=True)
    DateRented = models.DateField()
    RenewalDate = models.DateField()
    FeeIfLate = models.IntegerField()

class Book(models.Model):
    ISBN = models.IntegerField(max_length=13, primary_key=True, unique=True)
    Title = models.CharField(max_length=100)
    NumPages = models.BigIntegerField()
    SeriesID = models.ForeignKey('Series')
    ReleaseDate = models.DateField()
    BookType = models.ForeignKey('BookType')
    Genre = models.ForeignKey('BookGenre')

class BookAuthor(models.Model):
    AuthorID = models.ForeignKey('Author', primary_key=True, unique=True)
    ISBN = models.ForeignKey('Book', primary_key=True)

class Author(models.Model):
    AuthorID = models.CharField(Max_length = 10, primary_key=True, unique=True)
    AuthorFirstName = models.CharField()
    AuthorLastName = models.CharField()
    Alive = models.BooleanField()

class Series(models.Model):
    SeriesID = models.IntegerField(primary_key=True, unique=True)
    SeriesName = models.CharField(max_length=50)

class BookType(models.Model):
    BookType = models.CharField(primary_key=True, unique=True)

class BookGenre(models.Model):
    Genre = models.CharField(max_length=50, primary_key=True, unique=True)
