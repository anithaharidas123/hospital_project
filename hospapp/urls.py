from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('base',views.base,name='base'),
    path('base2',views.base2,name='base2'),
    path('',views.home,name='home'),
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
    path('Your_Patient_Record',views.Your_Patient_Record,name='Your_Patient_Record'),
    path('patient_dash1',views.patient_dash1,name='patient_dash1'),
    path('appo_dash1',views.appo_dash1,name='appo_dash1'),
    path('approve_appointment2',views.approve_appointment2,name='approve_appointment2'),
    path('view_your_appointments',views.view_your_appointments,name='view_your_appointments'),
    path('app_tick_pat<int:id>',views.app_tick_pat,name='app_tick_pat'),
    path('reject_icon_pat<int:id>',views.reject_icon_pat,name='reject_icon_pat'),
    path('approve_doc1',views.approve_doc1,name='approve_doc1'),
    path('approve_tick<int:id>',views.approve_tick,name='approve_tick'),
    path('ad_drec',views.ad_drec,name='ad_drec'),
    path('reg_doc',views.reg_doc,name='reg_doc'),
    path('patient',views.patient,name='patient'),
    path('patient_signup',views.patient_signup,name='patient_signup'),
    path('approve_patient2',views.approve_patient2,name='approve_patient2'),
    path('patient_login',views.patient_login,name='patient_login'),
    path('logout',views.logout,name='logout'),
    path('d_spec',views.d_spec,name='d_spec'),
    path('patient_dashboard',views.patient_dashboard,name='patient_dashboard'),
    path('patient_dash_main',views.patient_dash_main,name='patient_dash_main'),
    path('patient_appoi',views.patient_appoi,name='patient_appoi'),
    path('book_appoi_pat',views.book_appoi_pat,name='book_appoi_pat'),
    path('book_app',views.book_app,name='book_app'),
    path('appo_book_tick<int:id>',views.appo_book_tick,name='appo_book_tick'),
    path('reject_book_icon<int:id>',views.reject_book_icon,name='reject_book_icon'),
    path('patient_record2',views.patient_record2,name='patient_record2'),
    path('delete_appointments',views.delete_appointments,name='delete_appointments'),
    path('ip_button<int:id>',views.ip_button,name='ip_button'),
    path('admit_patient1',views.admit_patient1,name='admit_patient1'),
    path('admit_tick_click<int:id>',views.admit_tick_click,name='admit_tick_click'),
    path('discharge_admin',views.discharge_admin,name='discharge_admin'),




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)