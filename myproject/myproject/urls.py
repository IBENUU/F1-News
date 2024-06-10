from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from myproject.views import home, about,contact, detail_artikel
from myproject.autentikasi import akun_login, akun_registrasi, akun_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('artikel/<slug:slug>', detail_artikel, name="detail_artikel"),
    path('dashboard/',include("berita.urls")),
    path('autentikasi/login', akun_login, name="akun_login"),
    path('autentikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('autentikasi/logout', akun_logout, name="akun_logout"),



    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
