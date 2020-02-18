from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import working_day_add_new, working_day_edit, working_day_delete


urlpatterns = [

	path('working-day-add/<str:driver_slug>/', 		working_day_add_new, name='working_day_add_new'),
	path('working-day-edit/<str:day_slug>/', 		working_day_edit, name='working_day_edit'),
	path('working-day-delete/<str:day_slug>/', 		working_day_delete, name='working_day_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()