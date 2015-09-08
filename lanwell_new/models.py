from django.db import models

# Create your models here.

class ProjectTag(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    def __str__(self):
        return self.name+" "+self.display_name

class CompletedProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image = models.ImageField()
    tags = models.ManyToManyField(ProjectTag)
    def __str__(self):
        return self.name


class CustomerRequest(models.Model):
    name = models.CharField(max_length=300, verbose_name="Ваше имя*")
    email = models.EmailField(verbose_name="e-mail*",blank=True)
    phone = models.CharField(max_length=50, verbose_name="Ваш телефон", blank=True)
    description = models.CharField(max_length=2000, verbose_name="Суть проблемы*",blank=True)
    def __str__(self):
        return self.name + " " + self.email