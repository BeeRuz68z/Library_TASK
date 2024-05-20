from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_ISBN(self, value):
        if len(str(value)) < 6:
            raise serializers.ValidationError('ISBN must be at least 6 characters long')
        else:
            return value