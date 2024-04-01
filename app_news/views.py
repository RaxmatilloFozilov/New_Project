from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pyexpat.errors import messages

from app_news.models import News


# Create your views here.
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


# class UpdateNewsView(LoginRequiredMixin, UpdateView):
#     model = News
#     fields = ['title', 'content']  # Maqola modelining qaysi maydonlarini o'zgartirish kerakligini ko'rsating
#     template_name = 'news/update_news.html'
#     success_url = reverse_lazy('home')
#
# class DeleteNewsView(LoginRequiredMixin, DeleteView):
#     model = News
#     template_name = 'news/delete_news.html'
#     success_url = reverse_lazy('home')


class UpdateNewsView(LoginRequiredMixin, UpdateView):
    template_name = 'news/add_update.html'
    model = News
    success_url = reverse_lazy('home')


class DeleteNewsView(LoginRequiredMixin, DeleteView):
    template_name = 'news/add_delete.html'
    model = News
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'News deleted successfully')
        return super().delete(request, *args, **kwargs)
