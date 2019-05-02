from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from app import views as v
from .router import router
from rest_framework.authtoken import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.Home, name='home'),
    path('about', v.About, name='about'),
    path('contact', v.Contact, name='contact'),
    path('user', v.user, name='employees'),
    path('feedback/', v.feedback, name='feed'),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



