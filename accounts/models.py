from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.
class ProfileManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password=None):
        """
        Create y guarda un Usuario con el email dado, contraseña, etc
        """
        if not email:
            raise ValueError("Usuario debiese tener un correo electronico")

        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, apellido, password=None):
        user = self.create_user(
            email,
            password=password,
            nombre=nombre,
            apellido=apellido,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='dirección email',
                              max_length=255,
                              unique=True,
                              )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
