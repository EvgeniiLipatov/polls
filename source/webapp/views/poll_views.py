from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm
from webapp.models import Poll


class PollsView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ["-created_at"]


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll


class PollCreateView(CreateView):
    template_name = "poll/create.html"
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollEditView(UpdateView):
    form_class = PollForm
    template_name = 'poll/update.html'
    model = Poll
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('index')
