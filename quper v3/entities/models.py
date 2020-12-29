from django.db import models
from django.utils import timezone
from django.urls import reverse
from multiselectfield import MultiSelectField

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class ActivityGroup(models.Model):
    activityGroup = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, default='')
    user = models.ForeignKey(User, related_name="activityGroup",on_delete=models.CASCADE)

    def __str__(self):
        return self.activityGroup

    # def get_absolute_url(self):
    #     return reverse("activity_detail",kwargs={'pk':self.pk})

    class Meta:
        verbose_name_plural = 'Activity Groups'

class Activity(models.Model):
    activity = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, default='')
    # activityGroup = models.ForeignKey(ActivityGroup, related_name='activities',on_delete=models.CASCADE, null=True)
    activityGroup = models.ForeignKey(ActivityGroup, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name="activities",on_delete=models.CASCADE)

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse("activity_detail",kwargs={'pk':self.pk})

    class Meta:
        verbose_name_plural = 'Activities'

class Entity(models.Model):
    entityName = models.CharField(max_length=200, unique=True )
    # activity = models.ForeignKey('entities.Activity', related_name='activities', on_delete=models.CASCADE)
    activity = models.ManyToManyField(Activity)
    description = models.TextField(blank=True, default='')
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=200, blank=False, null=True, default='')
    city = models.CharField(max_length=200, blank=False, null=True, default='')
    postcode = models.CharField(max_length=10, blank=False, null=True, default='')
    country = models.CharField(max_length=20, null=True, default='Belgium')
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, related_name="entities",on_delete=models.CASCADE)

    def __str__(self):
        return self.entityName

    def approve_comments(self):
        # the approved_comment is a field in the comment model defined below
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("entity_detail",kwargs={'pk':self.pk})

    class Meta:
        verbose_name_plural = 'Entities'


class Comment(models.Model):
    # entity will be linked on the primary key (id) that is generated automatically for the Entity model
    entity = models.ForeignKey('entities.Entity', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    # user = models.ForeignKey(User, related_name="comments",on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("entity_list")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Comments'
