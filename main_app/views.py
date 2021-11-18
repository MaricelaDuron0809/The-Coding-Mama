from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView

class LandingPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')

class PostList(TemplateView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        form = PostForm()

        context = {
            'post_list': posts,
             'form': form,
          
        }

        return render(request, 'post_list.html', context)
    
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.mama = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'post_list.html', context)
    
class PostDetail(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        
        comments = Comment.objects.filter(post=post).order_by('-created_at')


        context = {
             'post': post,
             'form': form,
             'comments': comments,
           
        }
       

        return render(request, 'post_detail.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.mama = request.user
            new_comment.post = post
            new_comment.save()
        
        comments = Comment.objects.filter(post=post).order_by('-created_at')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'post_detail.html', context)
    

class PostUpdate(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post_update.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk': pk})
    
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.mama

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post_detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.mama


class Profile(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(mama=user).order_by('-created_at')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts
        }

        return render(request, 'profile.html', context)
    
    
