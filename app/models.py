from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
