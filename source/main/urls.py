"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import PollsView, PollView, PollCreateView, PollEditView, PollDeleteView, ChoiceForPollCreateView, \
    ChoiceEditView, ChoiceDeleteView, AnswerCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollsView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/create/', PollCreateView.as_view(), name='create_poll'),
    path('poll/edit/<int:pk>', PollEditView.as_view(), name='update_poll'),
    path('poll/delete/<int:pk>', PollDeleteView.as_view(), name='delete_poll'),
    path('choice/create/<int:pk>', ChoiceForPollCreateView.as_view(), name='poll_choice_create'),
    path('choice/edit/<int:pk>', ChoiceEditView.as_view(), name='update_choice'),
    path('choice/delete/<int:pk>', ChoiceDeleteView.as_view(), name='delete_choice'),
    path('choice/answer/<int:pk>', AnswerCreateView.as_view(), name='add_answer'),
]
