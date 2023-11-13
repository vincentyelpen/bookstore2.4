# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer


@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        data = request.data
        author_name = data.get('author', '')
        title = data.get('title', '')
        price = data.get('price', '')

        author, created = Author.objects.get_or_create(name=author_name)
        book = Book.objects.create(title=title, author=author, price=price)

        return Response({'status': 'success'})


@api_view(['GET'])
def retrieve_inventory(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({'books': serializer.data})


@api_view(['GET'])
def filter_by_author(request):
    author_name = request.query_params.get('author', '')
    books = Book.objects.filter(author__name__icontains=author_name)
    serializer = BookSerializer(books, many=True)
    return Response({'books': serializer.data})
