from django.db import models
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    author=models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE
    )
    title=models.CharField(max_length=20)
    text=models.TextField()



    def get_absolute_url(self):
        return reverse('home')

