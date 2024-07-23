from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/students/', views.student_list, name='student_list'),
    path('register/', views.register_student, name='register_student'),
    path('courses/<int:course_id>/enroll/', views.enroll_student, name='enroll_student'),
]

