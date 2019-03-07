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
from blog import views as bv
from config import views as cv
from django.contrib import admin
from django.urls import re_path

# from typeidea.custom_site import custom_site

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path('', bv.post_list),
    re_path('^category/(?P<category_id>\d+)/$', bv.post_list),
    re_path('^tag/(?P<tag_id>\d+)/$', bv.post_list),
    re_path('^post/(?P<post_id>\d+)/$', bv.post_list),
    re_path('^links/$', cv.links),
    # path(r'^super_admin/',admin.site.urls),

]
