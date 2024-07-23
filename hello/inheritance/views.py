from django.shortcuts import render
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutUsPageView(TemplateView):
    template_name = 'about_us.html'
class ContactUsPageView(TemplateView):
    template_name = 'contact_us.html'