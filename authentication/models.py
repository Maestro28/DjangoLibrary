# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email
from django.db import models

from .managers import CustomUserManager

# Create your models here.

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
        This class represents a basic user.
    """

    first_name = models.CharField(blank=True, max_length=20)
    middle_name = models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    password = models.CharField(max_length=128)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    role = models.IntegerField(default=0, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'middle_name', 'last_name']

    # objects = BaseUserManager()
    objects = CustomUserManager()

    ordering = ('email',)
    # class Meta:
    #     ordering = ['id']

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at,
                 user role, user is_active
        """
        return str(self.email)

    def __repr__(self):
        """
        This magic method is redefined to show class and id of CustomUser object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'


