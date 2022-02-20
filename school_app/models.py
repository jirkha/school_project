from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=256)
    abbrev = models.CharField(max_length=256)

    def __str__(self):
        return f"Name: {self.name}, Abbrev: {self.abbrev}"

class Teacher(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    degree = models.CharField(max_length=256)

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Degree: {self.degree}"
