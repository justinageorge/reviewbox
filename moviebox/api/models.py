
from django.db import models

class Movies(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=200,null=True)
    LANGUAGE_CHOICES=[
        ('english','English'),
        ('hindi','Hindi'),
         ('telugu','Telugu'),
        ('malayalam','Malayalam'),
        ('tamil','Tamil'),
        ('multiple languages','Multiple languages'),


    ]
    Language=models.CharField(max_length=200,choices=LANGUAGE_CHOICES,null=True)
    year_released=models.DateTimeField(auto_now_add=True)
    runtime_duration=models.PositiveIntegerField()
    poster_image=models.ImageField(upload_to="movies",null=True,blank=True,default="1.jpg")
    director=models.CharField(max_length=200,null=True)
    is_active=models.BooleanField(deault=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def formatted_runtime(self):
        hours, minutes = divmod(self.runtime_duration, 60)
        return f"{hours}h {minutes}m"

    def __str__(self):
        return self.title
    

