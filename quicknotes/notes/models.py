from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.

class RegisterUserManager(BaseUserManager):
    def create_user(self, name,email, password=None):
        if not email:
            raise ValueError('Fill the email id first')
        user= self.model(
            email = self.normalize_email(email),
            name= name

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, email, password = None):
        user = self.create_user(name=name, email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class RegisterUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    objects= RegisterUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
    
    
class Notes(models.Model):
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

