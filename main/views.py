from django.shortcuts import render
from django.views.generic import View


from .models import Video, VideoTag


class MainView(View):

    def get(self, request, *args, **kwargs):

        videos = Video.objects.all()
        video_count = Video.objects.all().count()
        video_tags = VideoTag.objects.all()
        context = {
            'videos': videos,
            'video_count': video_count,
            'video_tags': video_tags,
        }

        q = self.request.GET.get('q') or ''
        if q:
            context['videos'] = context['videos'].filter(title__contains=q)

        context['q'] = q

        tag = request.GET.get('tag') or ''
        if tag:
            video_tags = VideoTag.objects.filter(tag__name__iexact=tag)
            context['videos'] = set([tag.video for tag in video_tags])

        context['tag'] = tag

        return render(request, 'main/main.html', context)
