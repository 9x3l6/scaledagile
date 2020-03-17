from django.urls import path
from . import views


app_name="training"

urlpatterns = [
    path('index/',views.index_views,name="index"),
    path('SP/',views.SP_views,name="SP"),
    path('form/',views.form_views,name="form"),
    path('contact/',views.contact_views,name='contact'),
    path('ourCourses/',views.ourCourses_views,name='ourCourses'),
    path('leadingSAFe/', views.leadingSAFe_views, name='leadingSAFe'),
    path('SAFePOPM/', views.SAFePOPM_views, name='SAFePOPM'),
    path('SAFeSSM/', views.SAFeSSM_views, name='SAFeSSM'),
    path('ADSAFeSSM/', views.ADSAFeSSM_views, name='ADSAFeSSM'),
    path('SAFeDevOps/', views.SAFeDevOps_views, name='SAFeDevOps'),
    path('policies/',views.policies_views,name='policies'),
    path('faq/', views.faq_views, name='faq'),
    path('about/', views.about_views, name='about'),
    path('privacy/', views.privacy_views, name='privacy'),

    path('<slug>/',views.slug_views,name='slug'),

]
