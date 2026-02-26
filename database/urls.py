from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_list, name='database-search'),
    path('database-search', views.entry_list, name='database-search'),

    path('oral-history/<int:id>', views.single_entry, name='single-entry'),
    path('home', views.home_page),
    path('how-to', views.howto_page),
    path('about', views.about_page)
]