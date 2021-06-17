from django.contrib import admin

from .models import Tag, Video, VideoTag

admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(VideoTag)

