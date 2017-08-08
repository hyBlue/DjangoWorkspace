#blog.urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"), # name 설정 : url 이 바뀌어도 템플릿에서 name으로 호출 가능
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name = "post_edit"),
    url(r'^download/$', views.download),
    url(r'^(?P<id>\d+$)', views.post_detail, name = 'post_detail'),
    url(r'^post_posting/$', views.post_posting, name = 'post_posting')
    ]
