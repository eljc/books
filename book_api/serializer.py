from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_title(self, value):
        if len(value) < 3:
            raise ValidationError("The title of the book must be a least 3 characters")
        return value