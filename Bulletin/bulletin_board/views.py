from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
from .filters import FeedbackFilter
from .forms import FormPost, FormFeedback


class PostList(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'post_list'
    queryset = Post.objects.all()
    paginate_by = 10


class PostSingle(DetailView):
    model = Post
    form_class = FormFeedback
    template_name = 'posts/post_single.html'
    context_object_name = 'post_single'
    queryset = Post.objects.all()


class PostCreate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = 'bulletin_board.add_post'
    model = Post
    form_class = FormPost
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'bulletin_board.change_post'
    form_class = FormPost
    model = Post
    field = ['title', 'text', 'postCategory', 'cooper', 'cooper_video', 'cooper_audio']
    template_name = 'posts/edit.html'
    context_object_name = 'edit'
    success_url = reverse_lazy('main')


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'bulletin_board.delete_post'
    model = Post
    template_name = 'posts/delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('main')


class PostFeedback(CreateView):
    form_class = FormFeedback
    model = Feedback
    field = ['text']
    template_name = 'feedback/feedback.html'
    context_object_name = 'add_fb'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        feedback = form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.feedbackPost = Post.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        return super().form_valid(form)


class Profile(PermissionRequiredMixin, ListView):
    permission_required = 'accounts.view_profile'
    raise_exception = True
    model = Feedback
    template_name = 'profile.html'
    context_object_name = 'profile_list'
    queryset = Feedback.objects.all()
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = FeedbackFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


def accept_fb(request, pk):
    fb = Feedback.objects.get(id=pk)
    fb.status = 'Accept'
    fb.save()
    return redirect('profile')


def reject_fb(request, pk):
    fb = Feedback.objects.get(id=pk)
    fb.status = 'Reject'
    fb.save()
    return redirect('profile')
