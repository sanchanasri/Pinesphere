import os
from .forms import *
from .models import *
from .serializers import *
from django.conf import settings
from rest_framework import viewsets
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect, get_object_or_404
from django.template.loader import render_to_string
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect

@login_required(login_url='/log_in/')
def home(request):
    return render (request,'index.html')

def chart(request):
    return render (request,'chart-morris.html')

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    
    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')
        phone = serializer.validated_data.get('phone')        
        previous_application = JobApplication.objects.filter(email=email).order_by('-submitted_at').first() or JobApplication.objects.filter(phone=phone).order_by('-submitted_at').first()
        if previous_application:
            days_since_last_application = (timezone.now() - previous_application.submitted_at).days
            if days_since_last_application < 30:
                raise ValidationError({
                'detail': f"You can apply again after {30 - days_since_last_application} days."
            })
                return          
        job_application = serializer.save()
        subject = "New Job Application from"
        context = {
            'full_name': job_application.full_name,
            'email': email,
            'phone': phone,
        }
        message=render_to_string('Email Templates/job_application.html', context)
        recipient_list = ['sanchanasrig112302@gmail.com']
        email = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
        )
        email.content_subtype = 'html'
        if job_application.resume:
            resume_name=os.path.basename(job_application.resume.name)
            resume_content= job_application.resume.read()
            email.attach(resume_name, resume_content)
        email.send(fail_silently=False)

def post_pine_news(request):
    form = PineNewsForm()
    tags = PineNewsTags.objects.all()
    categories = PineNewsCategories.objects.all()
    if request.method=="POST":
        pine_news = PineNews(
            title=request.POST.get('title'),
            quote=request.POST.get('quote'),
            content=request.POST.get('content'),
            created_by=request.user if request.user.is_authenticated else User.objects.first()
        )
        pine_news.save()
        pine_news.categories.set(PineNewsCategories.objects.filter(id__in=request.POST.getlist('categories')))
        pine_news.tags.set(PineNewsTags.objects.filter(id__in=request.POST.getlist('tags')))
        images = request.FILES.getlist('images')
        for image in images:
            PineNewsImage.objects.create(pine_news=pine_news, image=image)
        return redirect('pine_news')
    context = {
        'tags': tags,
        'categories': categories,
        'form':form,
    }
    return render(request, 'Pine News Templates/pine_news_form.html', context)


def update_pine_news(request, pk):
    pine_news = get_object_or_404(PineNews, pk=pk)
    form = PineNewsForm(instance=pine_news)
    tags = PineNewsTags.objects.all()
    categories = PineNewsCategories.objects.all()

    if request.method == "POST":
        pine_news.title = request.POST.get('title')
        pine_news.quote = request.POST.get('quote')
        pine_news.content = request.POST.get('content')
        pine_news.created_by = request.user if request.user.is_authenticated else User.objects.first()

        pine_news.save()

        pine_news.categories.set(PineNewsCategories.objects.filter(id__in=request.POST.getlist('categories')))
        pine_news.tags.set(PineNewsTags.objects.filter(id__in=request.POST.getlist('tags')))

        images = request.FILES.getlist('images')
        for image in images:
            PineNewsImage.objects.create(pine_news=pine_news, image=image)
        return HttpResponseRedirect(reverse('pine_news'))

    context = {
        'tags': tags,
        'categories': categories,
        'form': form,
        'pine_news': pine_news,
    }
    
    return render(request, 'Pine News Templates/pine_news_update.html', context)

def delete_pine_news(request, id):
    pine_news = get_object_or_404(PineNews, id=id)
    pine_news.delete()
    return HttpResponseRedirect(reverse('pine_news'))



def pine_news_detail(request, id):
    pine_news= get_object_or_404(PineNews, id=id)
    return render(request, 'Pine News Templates/pine_news_detail.html', {'pine_news':pine_news})
    

def buttons(request):
    return render(request, 'button.html')

def charts(request):
    return render(request, "chart-morris.html")

def pine_news(request):
    news = PineNews.objects.prefetch_related('images').all()
    return render(request, 'Pine News Templates/pine_news.html',{'news':news})

def login_view(request):
    context = {
        'error': ""
    }
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['error'] = "Invalid username or password"
            return render(request, 'log_in.html', context)
    return render(request, "log_in.html")

def logout_view(request):
    logout(request)
    return redirect('/log_in')

def cookies_consent(request):
    return render(request,"index2.html")


