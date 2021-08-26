"""django_htmx_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from demo.views import HomeView, InfiniteScrollView, InfiniteScrollMoreRowsView, ClickToLoadView, ClickToLoadMoreRowsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("inifite-scroll/", InfiniteScrollView.as_view(), name="infinite_scroll"),
    path("inifite-scroll/more-rows/", InfiniteScrollMoreRowsView.as_view(), name="infinite_scroll_more_rows"),
    path("click-to-load/", ClickToLoadView.as_view(), name="click_to_load"),
    path("click-to-load/more-rows/", ClickToLoadMoreRowsView.as_view(), name="click_to_load_more_rows"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
