# todos/models.py

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """ A String Representation of the model """
        return self.title
