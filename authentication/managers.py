from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, middle_name, last_name,
                    password=None, role=0, is_admin=False, is_active=True):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            role=role,
            is_admin=is_admin,
            is_active=is_active
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, middle_name, last_name, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, first_name, middle_name,
                                last_name, password)
        user.is_admin = True
        user.role = 1
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
