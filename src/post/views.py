from django.views.generic import TemplateView, ListView, CreateView, UpdateView,DetailView, DetailView
from post.models import BlogPost
from django.urls import reverse_lazy

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "post"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "post/blogpost_create.html"
    fields = ['title', 'content', ]


class BlogPostUpdate(UpdateView):
    model = BlogPost
    fields = '__all__'
    template_name = "post/blogpost_edit.html"


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'


class BlogPostDelete(DetailView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("post:home")
