from django.contrib import admin
from tweet.models import Tweet


# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'created_at']
