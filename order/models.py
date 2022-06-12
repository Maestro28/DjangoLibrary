from django.db import models
from authentication.models import CustomUser
from book.models import Book

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField()

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
