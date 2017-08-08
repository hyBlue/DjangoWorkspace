from django.db import models
from django.conf import settings
import re
from django.forms import ValidationError
from django.core.urlresolvers import reverse
from django import forms
# Create your models here.
def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value) :
        raise ValidationError('Invalid lnglat type')
def min_length_validator(value):
    if(not value):
        raise forms.ValidationError('글자를 입력해 주세요.')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    photo = models.ImageField(blank = True, upload_to = 'blog/post/%Y/%m/%d')
    user_agent = models.CharField(max_length=200, blank = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, validators = [min_length_validator]) # 길이제한있는 문자열
    content = models.TextField()            # 길이제한없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) #최초 저장 시간만 저장
    updated_at = models.DateTimeField(auto_now=True)    #갱신이 될때마다 시간 저장
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
                              validators=[lnglat_validator],
                              help_text = ' 경도, 위도 포맷으로 입력',
                              blank =True)
    author = models.CharField(max_length = 30, default = 'anonymous')
    status = models.CharField(max_length=1, choices = STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank = True) #문자열로 지정해줘야함(Tag의 정의가 밑에 있기 때문)
    """
    다른 앱에 있는 모델과 relation을 걸 경우 app_name.model 이라고 써야함
    """
    class Meta: #class 내부의 class. default로 id의 역순 정렬
        ordering = ['-id']
    def __str__(self):      #shell 에서 제목을 보여주게 하기 위함
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args = [self.id])

class Comment(models.Model):
    post =models.ForeignKey(Post) # 이 comment는 Post 모델에 대해 1:N의 관계를  갖는다. post_id 필드 생성
    author = models.CharField(max_length=10)
    message = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.name