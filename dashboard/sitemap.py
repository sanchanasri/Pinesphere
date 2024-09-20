from django.contrib.sitemaps import Sitemap
from .models import PineNews
from django.urls import reverse

class PineNewsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return PineNews.objects.all()
    
    def location(self, obj):
        return obj.get_absolute_url()
    
    def lastmod(self, obj):
        return obj.updated_at
    
# class AuthSitemap(Sitemap):
#     changefreq = "monthly"
#     priority = 0.5

#     def items(self):
#         return ['login', 'logout']

#     def lastmod(self, obj):
#         return None 