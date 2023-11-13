# bookstore2/urls.py
from django.contrib import admin
from django.urls import path
from bookstore.views import add_book, retrieve_inventory, filter_by_author

urlpatterns = [
    path('add_book/', add_book),
    path('retrieve_inventory/', retrieve_inventory),
    path('filter_by_author/', filter_by_author),
    path('admin/', admin.site.urls),
]