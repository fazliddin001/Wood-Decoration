from django.contrib import admin
from .models import BlogModel, DescriptionModel, FeedBackModel, \
    TagModel, BlogCategoryModel, UserFeedBackModel, ServiceModel, ServiceCategoryModel, \
    SubscribedUserEmailModel, TeamModel, EstimateModel


@admin.register(EstimateModel)
class EstimateModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')
    search_fields = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('fullname', "updated_at")
    search_fields = ('fullname', "updated_at")
    list_filter = ('fullname', "updated_at")


@admin.register(SubscribedUserEmailModel)
class SubscribedUserEmailAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')
    search_fields = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')


@admin.register(ServiceCategoryModel)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', "created_at")
    search_fields = ('created_at', "updated_at", "title")
    list_filter = ('title', 'updated_at', "created_at")


@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', "created_at")
    search_fields = ('created_at', "updated_at", "title")
    list_filter = ('title', 'updated_at', "created_at")


@admin.register(UserFeedBackModel)
class UserFeedBackModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')
    search_fields = ('name', 'updated_at')
    list_filter = ('name', 'updated_at')


@admin.register(DescriptionModel)
class DescriptionModelAdmin(admin.ModelAdmin):
    list_display = ('text', 'updated_at')
    search_fields = ('text', 'updated_at')
    list_filter = ('text', 'updated_at')


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'updated_at')
    list_filter = ('title', 'updated_at')


@admin.register(FeedBackModel)
class FeedBackModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')
    search_fields = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'updated_at')
    list_filter = ('title', 'updated_at')


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'updated_at')
    list_filter = ('title', 'updated_at')
