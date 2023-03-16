from django.contrib import admin

from post.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title",  "slug", "created_on",)
    #list_editable = ('published',)


admin.site.register(BlogPost, BlogPostAdmin)
