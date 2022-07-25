from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe


class Event(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.id


class NavLink(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Banner(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    path = models.ImageField(upload_to='uploads/Banner')
    url = models.CharField(max_length=200)
    position_x = models.DecimalField(decimal_places=4, max_digits=10)
    position_y = models.DecimalField(decimal_places=4, max_digits=10)
    position_z = models.DecimalField(decimal_places=4, max_digits=10)
    rotation = models.DecimalField(decimal_places=4, max_digits=10)
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return self.title

    @property
    def banner_preview(self):
        if self.path:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.path.url))
        return ""


class Model_All(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=40, editable=False)
    modellink = models.FileField(upload_to='uploads/Models')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Model_All, self).save(*args, **kwargs)


class Point(models.Model):
    position_x = models.DecimalField(max_digits=10, decimal_places=4)
    position_y = models.DecimalField(max_digits=10, decimal_places=4)
    position_z = models.DecimalField(max_digits=10, decimal_places=4)
    label = models.IntegerField()
    text = models.CharField(max_length=100)
    audiolink = models.FileField(upload_to='uploads/Models/Points')
    model_link = models.ForeignKey(
        Model_All, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
