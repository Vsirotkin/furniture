from django.views.generic import TemplateView



class HomePageView(TemplateView):
    template_name = 'index.html'


class ProductsPageView(TemplateView):
    template_name = 'product.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
