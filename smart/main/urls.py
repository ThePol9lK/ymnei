from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('course', views.course, name = 'course'),
    path('about', views.about, name = 'about'),
    path('contacts', views.contatcs, name = 'contacts'),
    path('course/<str:title>', views.CourseDetailView.as_view(), name = 'course-detail'),
    path('course2/<str:title>', views.PreSchoolDetailView.as_view(), name = 'course-detail2'),
    path('course3/<str:title>', views.ExtraClasslDetailView.as_view(), name = 'course-detail3'),
    path('send_message/', views.contact, name='send_message'),
]

