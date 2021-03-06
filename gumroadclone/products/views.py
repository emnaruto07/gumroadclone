from django.views import generic
from gumroadclone.products.models import Product


class ProductListView(generic.ListView):
    template_name = "discover.html"
    queryset = Product.objects.all()

class ProductDetailView(generic.DetailView):
    template_name = "products/product.html"
    queryset = Product.objects.all()
