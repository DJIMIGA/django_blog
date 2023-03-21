from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DetailView, DeleteView
from post.models import BlogPost
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class BlogHome(ListView):
    model = BlogPost
    context_object_name = "post"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "post/blogpost_create.html"
    fields = ['title', 'content', ]


@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    fields = '__all__'
    template_name = "post/blogpost_edit.html"


@method_decorator(login_required, name='dispatch')
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'


@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("post:home")
    context_object_name = 'post'
