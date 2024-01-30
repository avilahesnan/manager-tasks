from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    OPTIONS_CATEGORIES = [
        ('PROGRAMMING','programming'),
        ('COMPUTER SCIENCE','computer science'),
        ('MATHEMATICS','mathematics'),
        ('PORTUGUESE','portuguese'),
        ('ENGLISH','english'),
        ('LEGISLATION','legislation'),
    ]

    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=100, choices=OPTIONS_CATEGORIES, default='NOT SPECIFIED')
    subject = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    term = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.name
