from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=254, db_index=True)

    class Meta:
        unique_together = 'category', 'name'

    def __str__(self):
        return self.name
