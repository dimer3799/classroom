from django.db import models

# Create your models here.

'''
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    position_lat = models.DecimalField(decimal_places=8, max_digits=10, verbose_name="Широта")
    position_long = models.DecimalField(decimal_places=8, max_digits=10, verbose_name="Довгота")
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
 '''