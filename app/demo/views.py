from django.views.generic import ListView, TemplateView
from demo.models import Product


class HomeView(TemplateView):
    template_name = "home.html"


class ProductsBaseView(ListView):
    model = Product
    queryset = Product.objects.all().select_related("category")
    paginate_by = 10


class InfiniteScrollView(ProductsBaseView):
    template_name = "infinite_scroll/base.html"


class InfiniteScrollMoreRowsView(ProductsBaseView):
    template_name = "infinite_scroll/table_load_more_rows.html"


class ClickToLoadView(ProductsBaseView):
    template_name = "click_to_load/base.html"


class ClickToLoadMoreRowsView(ProductsBaseView):
    template_name = "click_to_load/table_load_more_rows.html"
