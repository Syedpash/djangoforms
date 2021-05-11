from django.db import models

# Create your models here.

class News(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # it will display author as heading for this model
    def __str__(self):
        return self.author


class SportNews(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # displays title as heading for this model
    def __str__(self):
        return self.title

class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username