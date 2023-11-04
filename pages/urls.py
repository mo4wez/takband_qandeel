from django.urls import path

from .views import HomePageView, AboutUsPageView, ContactUsPageView, NotFoundPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-us/', AboutUsPageView.as_view(), name='about_us'),
    path('contact-us/', ContactUsPageView.as_view(), name='contact_us'),
    path('notfound/', NotFoundPageView.as_view(), name='not_found'),
]
