from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/', ProductsPageView.as_view(), name='product'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
