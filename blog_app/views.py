from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import CreateView,  DeleteView,  DetailView, UpdateView, ListView
from .models import Post
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = settings.LOGIN_REDIRECT_URL


class UserLogoutView(LogoutView):
   next_page = reverse_lazy('homepage')


class PostDetails(DetailView):
    model = Post
    context_object_name = "post"
    template_name = 'post_details.html'


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ['-created_at']


class UserPostDetails(DetailView):
    model = Post
    context_object_name = "post"
    template_name = 'user_details.html'


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'create_post.html'
    success_url = reverse_lazy('user_posts')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'create_post.html'
    success_url = reverse_lazy('user_posts')


class DeletePost(DeleteView):
    model = Post
    context_object_name = "post"
    template_name = 'delete_post.html'
    success_url = reverse_lazy('user_posts')


class UserPostList(ListView):
    model = Post
    template_name = 'user_list.html'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)
