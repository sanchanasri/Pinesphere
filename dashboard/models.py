from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field



class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    device_name = models.CharField(max_length=100, null=True, blank=True)  

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"

class Job(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True) 
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    resume = models.FileField(upload_to='assets/files/job_application_resumes')
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name 

# class AboutUs(models.Model):
#     about_us_title = models.CharField(max_length=250)
#     about_us_sub_title= models.CharField(max_length=250)
#     about_us_content = models.TextField()
#     about_us_tags = ArrayField(
#         models.JSONField(),
#         size=10,             
#         blank=True,
#         null=True
#     )
#     about_us_image= models.ImageField(upload_to='assets/image/')
#     vision_title= models.CharField(max_length=250)
#     vision_content= models.TextField()
#     mission_title= models.CharField(max_length=250)
#     mission_content = models.TextField()
#     why_we_title=models.CharField(max_length=250)
#     why_we_sub_title=models.CharField(max_length=500)
#     why_we_content= models.TextField()
#     why_we_tags=ArrayField(
#         models.JSONField(),
#         size=10,             
#         blank=True,
#         null=True
#     )
#     why_choose_us_title= models.CharField(max_length=250)
#     why_choose_us_sub_title= models.CharField(max_length=500)
#     why_choose_us_tags=ArrayField(
#         models.JSONField(),
#         size=10,             
#         blank=True,
#         null=True
#     )
#     why_choose_us_image= models.ImageField(upload_to='assets/images/')
 
# class Why_Us(models.Model):
#     slider_button = models.CharField(max_length=100)
#     company_intro = models.CharField(max_length=100)
#     company_intro_sub_heading = models.CharField (max_length=255)
#     company_intro_content = models.TextField()
#     company_intro_content_subtopic = models.CharField(max_length=255)
#     company_intro_content_subtopic2 = models.CharField(max_length=255)
#     company_intro_content_subtopic_text = models.CharField(max_length=255)
#     company_intro_content_subtopic2_text2 = models.CharField(max_length=255)
#     years_of_experience = models.CharField(max_length=3)
#     certified_company = models.CharField(max_length=255)
#     certified_company_content = models.TextField() 
#     our_services_heading = models.CharField(max_length=255)
#     our_services_sub_heading = models.TextField()
#     customer_satisfactory_heading = models.CharField(max_length=255)
#     customer_satisfactory_content = models.TextField()
#     customer_satisfactory_bgimage = models.ImageField() 
#     customer_worldwide_heading = models.CharField(max_length=255)
#     customer_worldwide_content = models.TextField()
#     customer_worldwide_bgimage = models.ImageField() 
#     why_us_heading = models.CharField(max_length=255)
#     why_us_sub_heading = models.TextField()
#     why_us_content = models.TextField()
#     why_us_bgimage = models.ImageField()
#     why_us_btn_text = models.CharField(max_length=30)
#     how_we_work_bgimage = models.ImageField()
#     how_we_work_heading = models.CharField(max_length=255)
#     how_we_work_sub_heading = models.CharField(max_length=255)
#     watch_process_text = models.CharField(max_length=255)
#     watch_process_icon = models.ImageField()
#     query_text = models.CharField(max_length=255)
#     query_icon = models.ImageField()
#     query_mail = models.CharField(max_length = 255)
#     client_partners = models.CharField(max_length=255)
#     contact_us_bgimage = models.ImageField()
#     contact_us_heading = models.CharField(max_length=255)
#     contact_us_sub_heading = models.CharField(max_length=255)
#     contact_us_content1 = models.TextField()
#     contact_us_content2 = models.TextField()
#     emergency_contact_text = models.CharField(max_length=255)
#     emergency_contact_icon = models.ImageField()
#     emergency_contact_number = models.CharField(max_length=255)
#     pine_news_heading = models.CharField(max_length=255)
    
    
# class Slider_Images(models.Model):
#     image_name = models.CharField(max_length=255)
#     slider = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
#     images = models.ImageField()
#     heading = models.CharField(max_length=255)
#     content = models.TextField()
    
# class Intro_Images(models.Model):
#     image_name = models.CharField(max_length=255)
#     intro_image = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
#     images = models.ImageField()
    
# class Icons (models.Model):
#     icon_name = models.CharField(max_length=255)
#     icons = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
#     icons_images = models.ImageField()

# class Our_services_content(models.Model):
    
#     our_services = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
#     icon = models.ImageField()
#     content = models.TextField()
#     hover_image = models.ImageField()
#     more_details_icon = models.ImageField()
#     heading = models.CharField(max_length=255)
    
# class why_us_tiles(models.Model):
#     why_us = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
#     why_us_icons = models.ImageField()
#     why_us_heading = models.CharField(max_length=255)
#     why_us_content = models.CharField(max_length=255)
#     why_us_readmore = models.CharField(max_length=255)

# class How_we_work (models.Model):
#     how_we_work_heading = models.CharField(max_length=255)
#     how_we_work_content = models.TextField()
#     how_we_work_hover_icon = models.TextField()
#     how_we_work = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
    
# class client_partners(models.Model):
#     client_partners_logos = models.ImageField()
#     client_partners = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
    
# class Pine_news (models.Model):
#     pine_news = models.ForeignKey(Why_Us, on_delete=models.CASCADE)
#     pine_news_heading = models.CharField(max_length=255)
#     pine_news_image = models.ImageField()
#     pine_news_content = models.TextField()
#     pine_news_read_more = models.CharField(max_length=255)


class PineNewsCategories(models.Model):
    category_name=models.CharField(max_length=500)
    
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = "Pine News Categories"
    
class PineNewsTags(models.Model):
     tag_name= models.CharField(max_length=250)
     
     def __str__(self):
              return self.tag_name
     class Meta:
        verbose_name_plural = "Pine News Tags"
          
    
class PineNews(models.Model):
    title = models.CharField(max_length=700)
    content = CKEditor5Field('content', config_name='extends')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,)
    categories= models.ManyToManyField(PineNewsCategories, related_name="news_items")
    tags= models.ManyToManyField(PineNewsTags, related_name="news_items")
    quote= models.CharField(max_length=500)
    
    def get_absolute_url(self):
        return reverse('pine_news_detail', args=[self.id])  
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Pine News"
        
class PineNewsImage(models.Model):
    pine_news = models.ForeignKey(PineNews, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='assets/images/pine_news_images/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.pine_news.title}"

    
