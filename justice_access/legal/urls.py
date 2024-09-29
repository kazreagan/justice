from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('legal-info/', views.legal_info, name='legal_info'),
    path('legal-information/', views.legal_information, name='legal_information'),
    path('legal-aid/', views.legal_aid, name='legal_aid'),
    path('track-case/', views.track_case, name='track_case'),
    path('legal-info/', views.legal_info_list, name='legal_info_list'),
    path('legal-info/<int:topic_id>/', views.legal_info_detail, name='legal_info_detail'),    
    path('request-legal-aid/', views.request_legal_aid, name='request_legal_aid'),
    path('thank-you/', views.legal_aid_thanks, name='legal_aid_thanks'),
    path('case-tracking/', views.case_tracking, name='case_tracking'),
    path('view-requests/', views.view_requests, name='view_requests'),
    
]