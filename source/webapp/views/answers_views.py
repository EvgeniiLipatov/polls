from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import  AnswerForm
from webapp.models import Poll, Choice, Answer


class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'answer/create.html'
    form_class = AnswerForm

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnswerCreateView, self).get_context_data()
        context['form'].fields['varText'].queryset = Choice.objects.filter(poll=self.get_poll())
        context['poll'] = self.get_poll()
        return context

    def form_valid(self, form):
        self.poll.answers.create(**form.cleaned_data)
        return redirect('poll_view', pk=self.poll.pk)

    def get_poll(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=pk)

