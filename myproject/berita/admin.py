from django.contrib import admin
from berita.models import Kategori, Artikel
# Register your models here.

admin.site.register(Kategori)

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['judul','kategori', 'author']
    search_fields = ['judu']
admin.site.register(Artikel,ArtikelAdmin)
