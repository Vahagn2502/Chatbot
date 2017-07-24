from django.db import models

class FB_user(models.Model):
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20),
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Video(models.Model):
    video_url = models.URLField()
    video_size = models.IntegerField()
    video_duration = models.DurationField()
    video_name = models.CharField(max_length=50)


class Audio(models.Model):
    audio_name = models.CharField(max_length=50)
    audio_duration = models.DurationField()
    audio_size = models.IntegerField()
    #dwd_count = models.Count(default = 0)
    dwd_date_last = models.DateField()
    IN_PROCESS = 'in_process'
    CONVERT = 'convert'
    DOWNLOAD = 'download'
    DONE = 'done'
    STATUS = (
        (IN_PROCESS, 'In process'),
        (CONVERT, 'Convert'),
        (DOWNLOAD, 'Downloaded'),
        (DONE, 'Done')
    )

    action = models.CharField(max_length=50, choices=STATUS)