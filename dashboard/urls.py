from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'job_application', views.JobApplicationViewSet, basename='jobapplication')


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path ('chart/', views.chart, name='chart'),
    path('buttons/', views.buttons, name="buttons"),
    path('create_pine_news/', views.post_pine_news, name='create_pine_news'),
    path('pine_news/', views.pine_news, name="pine_news"),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("log_in/", views.login_view, name="login"),
    path("log_out", views.logout_view, name="logout")
]
