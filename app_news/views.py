from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView , FormView, TemplateView
from pyexpat.errors import messages

from django.core.mail import send_mail
from django.utils import timezone
from app_news.models import News
from django.contrib.auth.models import User


# from .forms import RequestMessageForm


class AddNewsView(LoginRequiredMixin, CreateView):
    template_name = 'news/add_news.html'
    model = News
    success_url = reverse_lazy('home')
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']

    def form_valid(self, form):
        form.instance.news_author = self.request.user
        return super().form_valid(form)


class ListNewsView(ListView):
    template_name = 'news/list_news.html'
    model = News
    paginate_by = 2
    # context_object_name = 'xabar'


class DetailNewsView(DetailView):
    template_name = 'news/show_news.html'
    model = News


class UpdateNewsView(LoginRequiredMixin, UpdateView):
    template_name = 'news/add_update.html'
    model = News
    success_url = reverse_lazy('home')
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']


class DeleteNewsView(LoginRequiredMixin, DeleteView):
    template_name = 'news/add_delete.html'
    model = News
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'News deleted successfully')
        return super().delete(request, *args, **kwargs)


from .forms import MessageForm


class MessageFormView(LoginRequiredMixin, FormView):
    template_name = 'news/message_form.html'
    form_class = MessageForm
    success_url = '/success/'  # Your preferred success URL

    def form_valid(self, form):
        try:
            recipients = [user.email for user in User.objects.all() if user.email]
            subject = form.cleaned_data['mavzu']
            message = form.cleaned_data['matn']
            sender_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender_email, recipients, fail_silently=False)
            messages.success(self.request, 'Message sent successfully.')
        except Exception as e:
            messages.error(self.request, f'Xabar yuborishda xatolik yuzaga keldi: {e}')
        return super().form_valid(form)


class CustomView(LoginRequiredMixin, TemplateView):
    template_name = 'news/custom_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_data'] = 'Custom Context Data'
        return context

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# class SuperuserRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         user = self.request.user
#         return user.is_superuser
#         # return self.request.user.is_superuser
#
#
# # SuccessMessageMixin,,  FormView
# class SendRequestToCustomersView(SuperuserRequiredMixin):
#     template_name = 'news/message_form.html'
#     # form_class = RequestMessageForm
#     success_url = '/send_request/'
#     success_message = 'Request message sent to all customers.'
#
#     def form_valid(self, form):
#         message = form.cleaned_data['message']
#         users = User.objects.all()
#         recipients = [user.email for user in users]
#         send_mail('Request Message', message, 'your_email@example.com', recipients)
#         return super().form_valid(form)
