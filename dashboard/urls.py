from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .sitemap import *
from django.contrib.sitemaps.views import sitemap

router = DefaultRouter()
router.register(r'job_application', views.JobApplicationViewSet, basename='jobapplication')

sitemaps = {
    'pinenews': PineNewsSitemap,
    # 'auth': AuthSitemap,
}


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path ('chart/', views.chart, name='chart'),
    path('buttons/', views.buttons, name="buttons"),
    path('create_pine_news/', views.post_pine_news, name='create_pine_news'),
    path('pine_news/', views.pine_news, name="pine_news"),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("log_in/", views.login_view, name="login"),
    path("log_out", views.logout_view, name="logout"),
    path("cookies_consent", views.cookies_consent, name="cookies_consent"),
    path("charts/", views.charts, name="charts"),
    path('pine_news/<int:id>/', views.pine_news_detail, name='pine_news_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('pine-news/update/<int:pk>/', views.update_pine_news, name='update_pine_news'),
    path('pine-news/delete/<int:id>/', views.delete_pine_news, name='delete_pine_news'),
    path('notifications/', views.notifications, name="notifications")
]
