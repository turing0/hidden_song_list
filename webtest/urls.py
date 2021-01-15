from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('creat/', views.creat2, name='creat'),
    path(r'share/', views.share_html, name='share_html'),
    path(r'^share$', views.share, name='share'),
    path('gethtml/', views.gethtml),


]