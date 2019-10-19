from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, ChoiceForm, PollChoiceForm
from webapp.models import Poll, Choice


class ChoiceForPollCreateView(CreateView):
    model = Choice
    form_class = PollChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = poll.polls.create(**form.cleaned_data)
        return redirect('poll_view', pk=choice.poll.pk)


class ChoiceEditView(UpdateView):
    form_class = ChoiceForm
    model = Choice
    template_name = "choice/update.html"
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
