from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/about_us.html'


class ContactUsPageView(TemplateView):
    template_name = 'pages/contact_us.html'


class NotFoundPageView(TemplateView):
    template_name = 'pages/404_page.html'
