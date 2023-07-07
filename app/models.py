from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=155, unique=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=True, blank=True)
    title = models.CharField(max_length=155)
    text = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    title = models.CharField(max_length=155)
    text = models.TextField(blank=True, null=True)


class Contact(models.Model):
    username = models.CharField(max_length=155)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.username

