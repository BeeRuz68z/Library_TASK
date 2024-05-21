# test.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Clean up the database before each test
        Book.objects.all().delete()

        # Create a sample book
        self.book_data = {
            'title': 'Test Book',
            'author': 'Author Name',
            'publicationDate': '2023-01-01',
            'ISBN': 1111111111111
        }
        self.book = Book.objects.create(**self.book_data)

        # Store the URLs for list and detail views
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        new_book_data = {
            'title': 'New Test Book',
            'author': 'New Author',
            'publicationDate': '2024-05-21',
            'ISBN': 2222222222222
        }
        response = self.client.post(self.list_url, new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, new_book_data['title'])

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a book.
        """
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['ISBN'], self.book.ISBN)
    #
    def test_update_book(self):
        """
        Ensure we can update a book.
        """
        updated_data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publicationDate': '2023-02-01',
            'ISBN': 1111111111111
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_data['title'])
    #
    def test_partial_update_book(self):
        """
        Ensure we can partially update a book.
        """
        partial_data = {'title': 'Partially Updated Book'}
        response = self.client.patch(self.detail_url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, partial_data['title'])
    #
    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        response = self.client.delete(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    #
    def test_list_books(self):
        """
        Ensure we can list all books.
        """
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        r=response.data
        data=r['results']
        self.assertEqual(data[0]['title'], self.book.title)
        self.assertEqual(data[0]['ISBN'], self.book.ISBN)

