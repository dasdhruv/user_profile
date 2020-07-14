from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
The django already have provided default User which has in built attributes username, firstName, lastname, email and password.
In addition to these attributes we also need other attributes such as users' own portfolio site or users'own profile picture etc.
Hence we are creating an object called end_user which will have one-one relationship to the in-built User.
"""
class EndUserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    ## Additional attributes
    end_user_site = models.URLField(blank=True)
    # to use image field install pillow libraries
    # display_pics is the folder name which is in media folder and we have set the path and tagged to MEDIA_ROOT in settings.py file
    end_user_dp = models.ImageField(blank=True, upload_to = 'display_pics' )

    def __str__(this):
        # we are returning default username that comes with django
        return this.user.username
