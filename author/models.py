from django.db import models
from django.forms import ModelForm


class Author(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes last name of the author
        type surname: str max_length=20
        param patronymic: Describes middle name of the author
        type patronymic: str max_length=20

    """

    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, max_length=20)

    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """
        # return str(self.to_dict())[1:-1]
        return f"{self.name} {self.surname}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['name', 'surname', 'patronymic', 'books']
