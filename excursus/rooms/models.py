import json
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from channels import Group
from django.template.defaultfilters import linebreaks_filter
from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name=models.CharField(max_length=150, help_text="Enter a new category")
    
    slug = models.SlugField(help_text="Specify url",unique=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/rooms/category/%s/" % self.slug

    @property
    def group_name(self):
        return "category-%s" % self.id


class Post(models.Model):

    text=models.TextField(max_length=2000, help_text="Enter post")

    user=models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, help_text="a")

    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)

    photo=models.FileField(upload_to='uploads/photos/',null=True, blank=True)


    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        return "#%i: %s" % (self.id, self.text_intro())

    def text_intro(self):
        return self.text[:300]

    def text_body(self):
        return linebreaks_filter(self.text)

    def send_notification(self):
        notification = {
            "id": self.id,
            "text": self.text_body(),
            "created_date": self.created_date.strftime("%a %d %b %Y %H:%M"),
        }
        Group(self.category.group_name).send({
            "text": json.dumps(notification),
        })

    def save(self, *args, **kwargs):
        result = super(Post, self).save(*args, **kwargs)
        self.send_notification()
        return result



class Comment(models.Model):

    text=models.CharField(max_length=200, help_text="Enter comment")

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=timezone.now)

    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])