from django.test import TestCase                # erstellt Testdatenbank im Hintergrund, wird nach jedem Test gelöscht
from django.contrib.auth.models import User
from .models import Book

# Create your tests here.

# The setup method has already created a book. Let's test if it was created correctly:
class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
       cls.user = User.objects.create_user(
           username="testuser",
           email="test@mail.de",
           password="12345"
       )
       cls.book = Book.objects.create(
           title="Schönes Buch",
           author="Ich",
           description="Schönes Buch",
           published_date="2023-01-01",
           price=109.10
       )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Schönes Buch")
        self.assertEqual(self.book.author, "Ich")
        self.assertEqual(self.book.description, "Schönes Buch")
        self.assertEqual(self.book.published_date, "2023-01-01")
        self.assertEqual(self.book.price, 109.10)
    
    # Test if you can retrieve the book from the database.
    def test_book_retrieval(self):
        book_from_db = Book.objects.get(pk=1)
        self.assertEqual(book_from_db, self.book)
    
    # Modify a field of the Book instance, save it, then retrieve it again to check if the updated value is stored in the database.
    def test_book_update(self):
        self.book.title = "An updated title"
        self.book.save()
        self.assertEqual(self.book.title, "An updated title")

    # Delete the Book instance and then attempt to retrieve it to ensure it's been deleted.
    def test_book_deletion(self):
       # book_id = self.book.id
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=1)
    
    # Test the __str__ method and get_absolute_url() method.
    def test_str_representation(self):
        self.assertEqual(self.book.__str__(), 'Schönes Buch')

    def test_book_get_absolute_url(self):
        # Assuming you've defined a get_absolute_url method on the Book model that returns "/book/1/"
        self.assertEqual(self.book.get_absolute_url(), f'/book/{self.book.id}')



