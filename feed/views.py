# from django.shortcuts import render    / This is used for function based views /
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import FormView

from feed.models import Post
from feed.forms import PostForm



class HomePageView(TemplateView):

    template_name='home.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['post']= Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name='detail.html'
    model=Post


class AddPostView(FormView):
    template_name = 'new_post.html'
    form_class=PostForm
    success_url ='/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # print(form.cleaned_data['text'])  // to get the text entered in the text area field and printing in terminal

        # Create a post
         
        new_object =Post.objects.create (
        text=form.cleaned_data['title'],
        img=form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, "Your post was successful")
        return super().form_valid(form)
        



