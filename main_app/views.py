from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from main_app.forms import UserFeedBackForm, BlogFeedBackForm, EstimateForm
from main_app.models import UserFeedBackModel, BlogModel, FeedBackModel, TagModel, \
    BlogCategoryModel, ServiceCategoryModel, ServiceModel, SubscribedUserEmailModel, TeamModel, EstimateModel


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        user_feedbacks = UserFeedBackModel.objects.all()
        context = {
            "first_user_feedback": user_feedbacks[0],
            "user_feedbacks": user_feedbacks[1:5],
            "blogs": BlogModel.objects.all()[:3],
            "services": ServiceModel.objects.all()[:6]
        }

        return context


class AboutView(TemplateView):
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        context = {
            "teams": TeamModel.objects.all()
        }

        return context


class BlogDetailView(DetailView):
    template_name = "blog-details.html"
    model = BlogModel
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = FeedBackModel.objects.filter().order_by('-id')
        return context


class BlogView(ListView):
    template_name = "blog.html"
    model = BlogModel
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tags"] = TagModel.objects.all()
        context["categories"] = BlogCategoryModel.objects.all()

        return context


class SearchBlogView(ListView):
    template_name = "blog.html"
    model = BlogModel
    context_object_name = "blogs"

    def get_queryset(self):
        items = self.request.GET

        item = items.get("s", "")
        tag = items.get("tag", "")
        cat = items.get("cat", "")

        result = set(BlogModel.objects.filter(title__icontains=item).filter(tags__title__icontains=tag
                                                                            ).filter(categories__title__icontains=cat))

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        item = self.request.GET.get("s", "")

        context.update(
            {
                "tags": TagModel.objects.all(),
                "categories": BlogCategoryModel.objects.all(),
                "item": item
            }
        )
        return context


def blog_comment_view(request, pk):
    blog = BlogModel.objects.filter(pk=pk).first()

    if not blog:
        return Http404("Blog does not exist")

    if request.method != "POST":
        return redirect(request.GET.get("next", "/"))

    form = BlogFeedBackForm(data=request.POST)

    if not form.is_valid():
        text = form.errors
        return HttpResponse(text)

    comment = form.save(commit=False)
    comment.blog = blog
    comment.save()

    return redirect(request.GET.get("next", "/"))


class ContactView(TemplateView):
    template_name = "contact.html"


class ContactCreateView(CreateView):
    success_url = reverse_lazy("main_app:contact")
    model = UserFeedBackModel
    form_class = UserFeedBackForm


class TeamView(TemplateView):
    template_name = "team.html"

    def get_context_data(self, **kwargs):
        context = {
            "teams": TeamModel.objects.all()
        }

        return context


class ServiceView(ListView):
    template_name = "service.html"
    model = ServiceModel
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    template_name = "service-details.html"
    model = ServiceModel
    context_object_name = 'service'


def subscribe_view(request):
    email = request.POST.get('email_address', None)

    if email:
        new_email = SubscribedUserEmailModel.objects.create(email=email)
        new_email.save()

        return redirect("main_app:home")
    else:
        return Http404()


class EstimateView(CreateView):
    success_url = reverse_lazy("main_app:home")
    form_class = EstimateForm
    model = EstimateModel
