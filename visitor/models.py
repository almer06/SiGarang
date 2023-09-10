import uuid

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, user_username, user_email, user_phone_number, user_address=None, password=None):
        """
        Creates and saves a User with the given username, email,
        number phone, and password.
        """
        if not user_username:
            raise ValueError("Users must have an username")

        user = self.model(
            user_username=user_username,
            user_email=self.normalize_email(user_email),
            user_phone_number=user_phone_number,
            user_address=user_address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_username, user_email, user_phone_number, password=None):
        """
        Creates and saves a superuser with the given username, email,
        number phone, and password.
        """
        user = self.create_user(
            user_username,
            user_email,
            user_phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user_username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[username_validator],
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    user_email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    user_phone_number = models.CharField(
        verbose_name='phone number',
        max_length=15,
        unique=True,
        blank=False,
        null=False
    )
    user_address = models.TextField(
        verbose_name='address',
        blank=True,
        null=True
    )
    password = models.CharField("password", max_length=128)
    last_login = models.DateTimeField("last login", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "user_username"
    REQUIRED_FIELDS = ["user_email", "user_phone_number"]
    EMAIL_FIELD = "user_email"

    def __str__(self):
        return self.user_username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
