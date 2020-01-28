from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import show_index
from .views import show_driver


urlpatterns = [
	path('', 						show_index, name='show_index'),
	path('driver/<str:slug>/', 		show_driver, name='show_driver'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()