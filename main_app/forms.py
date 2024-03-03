from django import forms

from main_app.models import UserFeedBackModel, FeedBackModel, EstimateModel


class UserFeedBackForm(forms.ModelForm):
    class Meta:
        model = UserFeedBackModel
        fields = ['name', 'email', 'subject', 'message', 'phone_number']


class BlogFeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBackModel
        fields = ["fullname", "email", "website_url", "comment"]


class EstimateForm(forms.ModelForm):
    class Meta:
        model = EstimateModel
        fields = "__all__"
        exclude = ["create_at", "updated_at"]
