from django.contrib import admin
from blog.models import Author,Post
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','email']

admin.site.register(Author,AuthorAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=['title','content','author','publication_date']

admin.site.register(Post,PostAdmin)