"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail
from config.views import links

# from typeidea.custom_site import custom_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('^$', post_list),
    path('^category/(?P<category_id>\d+)/$', post_list),
    path('^tag/(?P<tag_id>\d+)/$', post_list),
    path('^post/(?P<tag_id>\d+)/$', post_list),
    path('^links/$', links),
    # path(r'^super_admin/',admin.site.urls),

]
