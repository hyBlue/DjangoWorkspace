from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User) # FIXME : BAD CASE
    user = models.OneToOneField('auth.User') # BAD CASE
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #장고 사용자 인증에 사용되는 USER모델 변경 지원
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)