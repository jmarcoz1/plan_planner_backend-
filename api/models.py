from django.db import models

class TimeOfDay(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parentcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='activities')
    time_of_day = models.ManyToManyField(TimeOfDay)
