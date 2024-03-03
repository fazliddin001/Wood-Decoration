from django.db import models


class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}\t{self.updated_at}"

    class Meta:
        verbose_name_plural = "Blog Categories"
        verbose_name = "Blog Category"


class TagModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}\t{self.updated_at}"

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"


class BlogModel(models.Model):
    title = models.CharField(max_length=255)

    short_description = models.TextField()
    long_description = models.TextField()

    attention = models.TextField()

    tags = models.ManyToManyField(TagModel, related_name="blogs")
    categories = models.ManyToManyField(BlogCategoryModel, related_name="blogs")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}\t{self.updated_at}"

    class Meta:
        verbose_name_plural = "Blogs"
        verbose_name = "Blog"


class DescriptionModel(models.Model):
    text = models.TextField()

    blogs = models.ForeignKey(BlogModel, related_name="descriptions", on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text}\t{self.updated_at}"

    class Meta:
        verbose_name_plural = "Descriptions"
        verbose_name = "Description"


class FeedBackModel(models.Model):
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    blogs = models.ForeignKey(BlogModel, related_name="feedbacks", on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fullname}\t{self.updated_at}"

    class Meta:
        verbose_name_plural = "FeedBacks"
        verbose_name = "FeedBack"


class UserFeedBackModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}\t{self.created_at}\t{self.updated_at}"

    class Meta:
        verbose_name_plural = "User FeedBacks"
        verbose_name = "User FeedBack"


class ServiceCategoryModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Service Categories"
        verbose_name = "Service Category"


class ServiceModel(models.Model):
    title = models.CharField(max_length=255)

    short_description = models.CharField(max_length=255)
    first_long_description = models.TextField()
    second_long_description = models.TextField()
    categories = models.ManyToManyField(ServiceCategoryModel, related_name="services")

    attention = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"


class SubscribedUserEmailModel(models.Model):
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"self.updated_at"

    class Meta:
        verbose_name_plural = "Subscribed Emails"
        verbose_name = "Subscribed Email"


class TeamModel(models.Model):
    fullname = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    image = models.ImageField(upload_to="team/")

    twitter = models.CharField(max_length=255)
    google = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    pinterest = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fullname}\t {self.created_at}"

    class Meta:
        verbose_name_plural = "Teams"
        verbose_name = "Team"


class EstimateModel(models.Model):
    wd_height = models.FloatField()
    wd_width = models.FloatField()

    wnd_height = models.FloatField()
    wnd_width = models.FloatField()

    door_height = models.FloatField()
    door_width = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at}"

    class Meta:
        verbose_name_plural = "Estimates"
        verbose_name = "Estimate"
