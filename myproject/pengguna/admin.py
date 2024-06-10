from django.contrib import admin
from pengguna.models import Book,Genre,Borrow

# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Borrow)