from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=500, null=False, blank=False, verbose_name='question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')


class Choice(models.Model):
    varText = models.TextField(max_length=1000, null=False, blank=False, verbose_name='answer')
    poll = models.ForeignKey('webapp.Poll', related_name='polls', on_delete=models.CASCADE)
