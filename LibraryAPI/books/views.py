from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from rest_framework.filters import  SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializer import *
from .filter import *
# from .pagination import *

# Create your views here.
class BookPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
class booklistview(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    pagination_class = BookPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            raise NotFound(detail="No book found matching the criteria.")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class bookoneview(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            a = Book.objects.get(id=id)
            serializer = BookSerializer(a)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise serializers.ValidationError({"message": "Book not found"})

class createbook(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class bookdetailview(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            a = Book.objects.get(id=id)
            serializer = BookSerializer(a)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise serializers.ValidationError({"message": "Book not found"})

    def put(self,request,id):
        try:
            a = Book.objects.get(id=id)
            serializer = BookSerializer(a, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise serializers.ValidationError({"message":"Book not found"})

    def delete(self,request,id):
        try:
            a=Book.objects.get(id=id)
            a.delete()
            return Response({'message':"Book Deleted Successfully"},status=status.HTTP_200_OK)
        except:
            raise serializers.ValidationError({"message":"Book not found"})