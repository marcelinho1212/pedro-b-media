from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("packages/", views.packages, name="packages"),
    path("projects/", views.projects, name="projects"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
] 

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)