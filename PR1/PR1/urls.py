"""PR1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def root(request):
    return redirect('blog:post_list')
urlpatterns = [

    url(r'^admin/', admin.site.urls),

    #url(r'^$', root, name = 'root'),
    url(r'^$', lambda r: redirect('blog:post_list'), name = 'root'),

    url(r'^blog/', include('blog.urls',namespace = 'blog')),
    url(r'^accounts/', include('accounts.urls', namespace = 'accounts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)