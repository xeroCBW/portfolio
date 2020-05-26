from django.db import models

# Create your models here.

class Gallery(models.Model):
    description = models.CharField(default='作品的描述',max_length=100)
    pic = models.ImageField(default='default.png',upload_to='images/')
    title = models.CharField(default='这里写简介',max_length=100)

    def __str__(self):
        return self.title






