from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
