from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
     path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('fetch-report-data/', views.fetch_report_data, name='fetch_report_data'),
    path('api/generate-report', views.fetch_report_data, name='report_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
