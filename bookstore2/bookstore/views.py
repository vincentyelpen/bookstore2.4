import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Author, Book

@csrf_exempt
def add_book(request):
    if request.method == 'GET':
        # Handle GET request
        books = Book.objects.all()
        books_data = [{'id': book.id, 'title': book.title, 'author': book.author.name, 'price': book.price} for book in books]
        return JsonResponse({'status': 'success', 'books': books_data, 'message': 'This is a GET request'})

    elif request.method == 'POST':
        # Handle POST request
        try:
            data = json.loads(request.body.decode('utf-8'))
            author_name = data.get('author', '')
            title = data.get('title', '')
            price = float(data.get('price', ''))

            if not all(char.isalpha() or char.isspace() for char in author_name) or len(author_name) > 50:
                return JsonResponse({'status': 'error', 'message': 'Invalid author name'}, status=400)

            if len(title) > 100 or not title.isprintable():
                return JsonResponse({'status': 'error', 'message': 'Invalid title'}, status=400)

            author, created = Author.objects.get_or_create(name=author_name)
            book = Book.objects.create(title=title, author=author, price=price)

            return JsonResponse({'status': 'success'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data format'}, status=400)

@csrf_exempt
def inventory(request):
    if request.method == 'GET':
        # Handle GET request for inventory
        books = Book.objects.all()
        books_data = [{'title': book.title, 'author': book.author.name, 'price': book.price} for book in books]
        return JsonResponse({'books': books_data})

@csrf_exempt
def filter(request):
    if request.method == 'GET':
        # Handle GET request for filtering books
        author_name = request.GET.get('author', '')
        books = Book.objects.filter(author__name__icontains=author_name)
        books_data = [{'id': book.id, 'title': book.title, 'author': book.author.name, 'price': book.price} for book in books]
        return JsonResponse({'books': books_data})

    elif request.method == 'PUT':
        # Handle PUT request for filtering books
        try:
            data = json.loads(request.body.decode('utf-8'))
            author_name_to_filter = data.get('author', '')
            title_to_filter = data.get('title', '')
            min_price = data.get('min_price', '')
            max_price = data.get('max_price', '')

            query_params = {}
            if author_name_to_filter:
                query_params['author__name__icontains'] = author_name_to_filter
            if title_to_filter:
                query_params['title__icontains'] = title_to_filter
            if min_price:
                query_params['price__gte'] = min_price
            if max_price:
                query_params['price__lte'] = max_price

            books = Book.objects.filter(**query_params)
            books_data = [{'id': book.id, 'title': book.title, 'author': book.author.name, 'price': book.price} for book in books]

            return JsonResponse({'books': books_data})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data format'}, status=400)
@csrf_exempt
def update_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)

    if request.method == 'GET':
        # Handle GET request for updating a book
        book_data = {'title': book.title, 'author': book.author.name, 'price': book.price}
        return JsonResponse({'status': 'success', 'book': book_data})

    elif request.method == 'PUT':
        # Handle PUT request for updating a book
        try:
            data = json.loads(request.body.decode('utf-8'))
            author_name = data.get('author', '')
            title = data.get('title', '')
            price = data.get('price', '')

            if author_name:
                author, created = Author.objects.get_or_create(name=author_name)
                book.author = author

            if title:
                book.title = title

            if price:
                book.price = float(price)

            book.save()

            return JsonResponse({'status': 'success'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data format'}, status=400)

@csrf_exempt
def delete_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)

    if request.method == 'GET':
        # Handle GET request for deleting a book
        book_data = {'title': book.title, 'author': book.author.name, 'price': book.price}
        return JsonResponse({'status': 'success', 'book': book_data, 'message': 'This is a GET request'})

    elif request.method == 'DELETE':
        # Handle DELETE request for deleting a book
        book_data = {'id': book.id, 'title': book.title, 'author': book.author.name, 'price': book.price}
        book.delete()
        return JsonResponse({'status': 'success', 'message': 'Book deleted', 'deleted_book': book_data})