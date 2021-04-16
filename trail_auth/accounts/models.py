from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

# note creating the user manager for the costum user


class UserManager(BaseUserManager):

    # note: creating general user for user
    def create_user(self, email, full_name, password=None):

        if not email:
            raise ValueError("User must have an email address")
        if not full_name:
            raise ValueError("User must have full name ")
        user = self.model(
            email=self.normalize_email(email),
            full_name = full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # note: creating the staff user
    def create_staffuser(self, email, full_name, password):

        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    # note: creating the super user
    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# note: creating costem user from my projecct


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True)
    full_name = models.CharField(verbose_name="full name", max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    # note: required fields  default contains email and password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = UserManager()
    # note : sub function are

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
    # note: user permissions to costum user

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_lable):

        return True

    # note: propertys are
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
