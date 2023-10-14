from django.db import models

class TestsBase(models.Model):
    Question = models.CharField(max_length=300)
    Solve = models.CharField(max_length=150)