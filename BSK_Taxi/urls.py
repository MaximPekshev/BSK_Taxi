from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
	
	path(''                 , include('baseapp.urls')),
    path('working-days/'    , include('workingdayapp.urls')),
    path('profile/'         , include('authapp.urls')),

    path('admin/', admin.site.urls),
]
