from django.db import models
from django.contrib.auth.models import User


# Creating a post
class Post(models.Model):
    place = models.CharField(max_length = 40)
    address = models.CharField(max_length = 100)
    rent = models.PositiveIntegerField()
    bedroom = models.PositiveSmallIntegerField()
    bathroom = models.PositiveSmallIntegerField()
    size = models.PositiveIntegerField()
    phone = models.PositiveIntegerField() 
    owner= models.ForeignKey(User,on_delete=models.CASCADE, default = None)
    date_posted = models.DateTimeField(auto_now_add = True,)
    image = models.ImageField(default = 'default.jpg', upload_to = 'house_pics')
    likes = models.ManyToManyField(User, related_name = 'advertisement_post')

    def __str__(self):
        return self.place




