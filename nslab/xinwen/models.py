from django.db import models

class Title(models.Model):
    text = models.CharField(max_length=200)
    url = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.text

class Content(models.Model):
    title=models.ForeignKey(Title)
    text=models.TextField()

    def __str__(self):
        return self.text[:50]
