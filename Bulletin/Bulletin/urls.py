"""
URL configuration for Bulletin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from bulletin_board.views import Profile, accept_fb, reject_fb

urlpatterns = [
    path('', include('bulletin_board.urls'), name='main'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('bulletin_board.urls')),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/accept_fb/<int:pk>/', accept_fb, name='accept_fb'),
    path('profile/reject_fb/<int:pk>/', reject_fb, name='reject_fb'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
