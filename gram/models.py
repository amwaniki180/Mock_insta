from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    Name = models.TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome Me!")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
     

    @classmethod
    def find_profile(cls,name):
        return cls.objects.filter(user__username__icontains = name).all()

    def togglefollow(self, profile):
        if self.following.filter(followee=profile).count() == 0:
            Follows(followee=profile, follower=self).save()
            return True
        else:
            self.following.filter(followee=profile).delete()
            return False

    def like(self, photo):
        if self.mylikes.filter(photo=photo).count() == 0:
            Likes(photo=photo,user=self).save()