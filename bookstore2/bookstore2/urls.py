# bookstore2/urls.py
from django.contrib import admin
from bookstore.views import add_book, add_books,inventory, filter,update_book,delete_book,aggregate_delete
from django.urls import path




urlpatterns = [
    path('add_book/', add_book),
    path('add_books/', add_books),
    path('inventory/', inventory),
    path('filter/', filter),
    path('update_book/<int:book_id>/', update_book),  # Add the update_book view with a dynamic book_id parameter
    path('delete_book/<int:book_id>/', delete_book),
    path('aggregate_delete/', aggregate_delete),# Add the delete_book view with a dynamic book_id parameter
    path('admin/', admin.site.urls),

]