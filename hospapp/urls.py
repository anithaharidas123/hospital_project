from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('base2',views.base2,name='base2'),
    path('home',views.home,name='home'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('about_us',views.about_us,name='about_us'),
    path('admin',views.admin_home,name='admin'),
    path('admin_signup',views.admin_signup,name='admin_signup'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_dash1',views.admin_dash1,name='admin_dash1'),
    path('doctor1',views.doctor1,name='doctor1'),
    path('patient1',views.patient1,name='patient1'),
    path('appointment1',views.appointment1,name='appointment1'),
    path('doctor',views.doctor_home,name='doctor'),
    path('doctor_signup',views.doctor_signup,name='doctor_signup'),
    path('doctor_login',views.doctor_login,name='doctor_login'),
    path('doctor_dashboard',views.doctor_dashboard,name='doctor_dashboard'),
    path('doctor-dash1',views.doctor_dash1,name='doctor_dash1'),
    path('patient_dash1',views.patient_dash1,name='patient_dash1'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)