from django.urls import path
from blog.views import RegisterAuthorView,PostView,All_Post,search

urlpatterns=[
    path('',RegisterAuthorView.as_view(),name='author_reg'),
    path('post/',PostView.as_view(),name='post_form'),
    path('allpost/',All_Post.as_view(),name='allpost_url'),
    path('search/',search,name='search_url')
]