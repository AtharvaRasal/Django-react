from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Note

from rest_framework_simplejwt.tokens import RefreshToken  # 🔑 this is the key part

class NoteTests(APITestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Generate JWT token for that user
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # Set Authorization header with JWT token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

    def test_create_note(self):
        data = {
            'title': 'Test Note',
            'content': 'This is a test note.',
            'author': self.user.id
        }
        response = self.client.post('/api/notes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_title(self):
        data = {
            'content': 'Missing title test',
            'author': self.user.id
        }
        response = self.client.post('/api/notes/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_notes(self):
        Note.objects.create(title='Sample Note', content='Note body', author=self.user)
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_string_representation(self):
        note = Note.objects.create(title='My Note', content='Hello!', author=self.user)
        self.assertEqual(str(note), 'My Note')
