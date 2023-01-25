from rest_framework.views import APIView
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_book_by_id(self, id):
        try:
            return Book.objects.get(id=id)
        except:
            return Response({
             'error': 'Book does not exist'
         }, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        book = self.get_book_by_id(id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
        
    def put(self, request, id):
        book = self.get_book_by_id(id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors        
    
    def delte(self, request, id):
        book = self.get_book_by_id(id)
        book.delete()
        return Response({
             'delete':True
        })