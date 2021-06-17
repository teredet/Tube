from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Video(models.Model):

    title = models.CharField(max_length=255)
    file = models.FileField()
    
    def __str__(self):
        return self.title


class VideoTag(models.Model):

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tag.name
