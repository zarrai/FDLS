from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=25)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username