"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
from . views import home_view, login_view, logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('project/', include('project.urls')),
    path('issue/', include('issue.urls')),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

