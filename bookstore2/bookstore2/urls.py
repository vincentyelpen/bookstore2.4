# bookstore2/urls.py
from django.contrib import admin
from bookstore.views import add_book, inventory, filter,update_book,delete_book
from django.urls import path




urlpatterns = [
    path('add_book/', add_book),
    path('inventory/', inventory),
    path('filter/', filter),
    path('update_book/<int:book_id>/', update_book),  # Add the update_book view with a dynamic book_id parameter
    path('delete_book/<int:book_id>/', delete_book),  # Add the delete_book view with a dynamic book_id parameter
    path('admin/', admin.site.urls),

]