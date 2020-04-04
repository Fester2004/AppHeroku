from django.db import models


class Article(models.Model):
    author= models.CharField(max_length=22)
    title = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        template = f'{self.author} {self.title} {self.text}'
        return template.format(self)