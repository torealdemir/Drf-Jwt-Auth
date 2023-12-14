from django.db import models
from  django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('email is required')
        if not username:
            raise ValueError('username is required')
        
        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length = 60, unique = True)
    username = models.CharField(max_length = 255, unique = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    last_login_at = models.DateTimeField(auto_now = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    objects = AccountManager()

    def __str__(self):
        return self.username
