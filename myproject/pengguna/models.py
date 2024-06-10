from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.borrower.username}"
    
#penjelasan
    
#Dalam kasus yang saya buat di atas, terdapat relasi many-to-many antara model Book dan Genre, karena setiap buku dapat memiliki beberapa genre, dan setiap genre dapat terkait dengan beberapa buku. Sedangkan untuk peminjaman buku, menggunakan model Borrow dengan relasi many-to-one antara Book dan User (bawaan Django untuk manajemen pengguna), karena setiap buku dapat dipinjam oleh banyak pengguna, dan setiap pengguna dapat meminjam banyak buku.