from django.urls import path
from .views import ServiceView, ServiceDetailView, BlogDetailView, \
    BlogView, HomeView, TeamView, AboutView, ContactView, ContactCreateView, \
    TemplateView, blog_comment_view, SearchBlogView, subscribe_view, EstimateView

app_name = "main_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("service/", ServiceView.as_view(), name="service"),
    path("service-detail/<int:pk>", ServiceDetailView.as_view(), name="service-detail"),
    path("blog-detail/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog-search/", SearchBlogView.as_view(), name="search-blog"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact-create/", ContactCreateView.as_view(), name="contact-create"),
    path("team/", TeamView.as_view(), name="team"),
    path("template/", TemplateView.as_view(), name="template"),
    path("blog-comment/<int:pk>", blog_comment_view, name="blog-comment"),
    path("subscribe/", subscribe_view, name="subscribe"),
    path("estimate/", EstimateView.as_view(), name="estimate")
]
