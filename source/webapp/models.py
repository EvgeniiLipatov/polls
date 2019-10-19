from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=500, null=False, blank=False, verbose_name='question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')

    def __str__(self):
        return self.question

class Choice(models.Model):
    varText = models.TextField(max_length=1000, null=False, blank=False, verbose_name='answer')
    poll = models.ForeignKey('Poll', related_name='polls', on_delete=models.CASCADE)

    def __str__(self):
        return self.varText


class Answer(models.Model):
    poll = models.ForeignKey('Poll', related_name='answers', on_delete=models.CASCADE)
    varText = models.ForeignKey('Choice', related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')

    def __str__(self):
        return self.varText
