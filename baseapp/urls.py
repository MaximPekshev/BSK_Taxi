from django.urls import path
from django.contrib import admin
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import show_index
from .views import show_driver
from .views import driver_add_new


urlpatterns = [
	path('', 						show_index, name='show_index'),
	path('driver/<str:slug>/', 		show_driver, name='show_driver'),
	path('new-driver/', 			driver_add_new, name='driver_add_new'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()