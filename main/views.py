from django.shortcuts import render
from django.views.generic import View


from .models import Video


class MainView(View):

    def get(self, request, *args, **kwargs):

        videos = Video.objects.all()
        video_count = Video.objects.all().count()
        context = {
            'videos': videos,
            'video_count': video_count,
        }

        return render(request, 'main/main.html', context)
