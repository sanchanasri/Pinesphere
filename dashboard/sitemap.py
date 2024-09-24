from django.contrib.sitemaps import Sitemap
from .models import PineNews
from django.urls import reverse

class PineNewsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return list(PineNews.objects.all())
    
    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        if isinstance(obj, PineNews):
            return obj.updated_at
        return None  

class AuthSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['login', 'logout', 'pine_news']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return None
