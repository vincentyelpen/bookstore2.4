import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Author, Book
from django.db import transaction

@csrf_exempt
def add_book(request):
    if request.method == 'GET':
        # Handle GET request
        books = Book.objects.all()
        books_data = [{'id': book.id, 'title': book.title, 'authors': [author.name for author in book.authors.all()], 'price': book.price} for book in books]
        return JsonResponse({'status': 'success', 'books': books_data, 'message': 'This is a GET request'})

    elif request.method == 'POST':
        # Handle POST request
        try:
            data = json.loads(request.body.decode('utf-8'))
            author_names = data.get('authors', '').split(', ')
            title = data.get('title', '')
            price = float(data.get('price', ''))

            # Validate title and price (unchanged from your original code)

            # Create or get authors
            authors = [Author.objects.get_or_create(name=author.strip())[0] for author in author_names]

            # Check if the book already exists
            existing_book = Book.objects.filter(title=title).first()
            if existing_book:
                existing_book.authors.add(*authors)
            else:
                new_book = Book.objects.create(title=title, price=price)
                new_book.authors.add(*authors)

            return JsonResponse({'status': 'success'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data format'}, status=400)


@csrf_exempt
def add_books(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            books_info = data.get('books', [])

            with transaction.atomic():
                for index, book_info in enumerate(books_info, start=1):
                    author_names = book_info.get('authors', '').split(', ')
                    title = book_info.get('title', '')
                    price = float(book_info.get('price', ''))

                    # Validate title and price (unchanged from your original code)

                    # Create or get authors
                    authors = [Author.objects.get_or_create(name=author.strip())[0] for author in author_names]

                    # Check if the book already exists
                    existing_book = Book.objects.filter(title=title).first()
                    if existing_book:
                        existing_book.authors.add(*authors)
                    else:
                        new_book = Book.objects.create(title=title, price=price)
                        new_book.authors.add(*authors)

            return JsonResponse({'status': 'success'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data format'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def inventory(request):
    if request.method == 'GET':
        # Handle GET request for inventory
        books = Book.objects.all()
        books_data = [
            {'title': book.title, 'authors': [author.name for author in book.authors.all()], 'price': book.price} for
            book in books]

        return JsonResponse({'books': books_data})

@csrf_exempt
def filter(request):
    if request.method == 'GET':
        # Handle GET request for filtering books
        author_name = request.GET.get('author', '')
        books = Book.objects.filter(authors__name__icontains=author_name)

        books_data = [{'id': book.id, 'title': book.title, 'authors': [author.name for author in book.authors.all()],
                       'price': book.price} for book in books]

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
                query_params['authors__name__icontains'] = author_name_to_filter  # 修改这里

            if title_to_filter:
                query_params['title__icontains'] = title_to_filter
            if min_price:
                query_params['price__gte'] = min_price
            if max_price:
                query_params['price__lte'] = max_price

            books = Book.objects.filter(**query_params)
            books_data = [{'id': book.id, 'title': book.title, 'authors': [author.name for author in book.authors.all()],
                           'price': book.price} for book in books]

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
        book_data = {'title': book.title, 'authors': [author.name for author in book.authors.all()],
                     'price': book.price}

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
        book_data = {'id': book.id, 'title': book.title, 'authors': [author.name for author in book.authors.all()], 'price': book.price}

        return JsonResponse({'status': 'success', 'book': book_data, 'message': 'This is a GET request'})

    elif request.method == 'DELETE':
        # Handle DELETE request for deleting a book
        book_data = {'id': book.id, 'title': book.title, 'authors': [author.name for author in book.authors.all()], 'price': book.price}

        book.delete()
        return JsonResponse({'status': 'success', 'message': 'Book deleted', 'deleted_book': book_data})


@csrf_exempt
def aggregate_delete(request):
    if request.method == 'GET':
        return JsonResponse({'test': 'ok'})

    if request.method == 'DELETE':
        try:
            data = json.loads(request.body.decode('utf-8'))
            book_array = data.get('book_array', [])

            deleted_book = []
            not_founded_book = []

            for book_info in book_array:
                # delete mutiple books by ID
                if 'id' in book_info:
                    id = book_info['id']
                    try:
                        book = Book.objects.get(pk=id)
                        book_detail = {'id': book.id, 'title': book.title, 'author': book.author.name,
                                       'price': book.price}
                        deleted_book.append(book_detail)
                        book.delete()
                    except Book.DoesNotExist:
                        not_founded_book.append({'id': id, 'error message': 'can not found by id'})

                # delete mutiple books by title
                elif 'title' in book_info:
                    title = book_info['title']
                    try:
                        book = Book.objects.get(title=title)
                        book_detail = {'id': book.id, 'title': book.title, 'author': book.author.name,
                                       'price': book.price}
                        deleted_book.append(book_detail)
                        book.delete()
                    except Book.DoesNotExist:
                        not_founded_book.append({'title': title, 'error message': 'can not found by title'})

                response_data = {'status': 'success', 'deleted books': deleted_book}

            if not_founded_book:
                response_data['status'] = 'partly success'
                response_data['not found books'] = not_founded_book

            return JsonResponse(response_data)

        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data format'}, status=400)