from django.shortcuts import render,redirect
from blog.models import Post,Author
from blog.forms import PostForm,AuthorForm
from django.views import View
from django.db.models import Q
# Create your views here.
# username = amit
#password =12345678

class RegisterAuthorView(View):
    template_name='blog/register_author.html'
    form=AuthorForm
    def get(self,request):
            form=self.form()
            context={'form':form}
            return render(request,self.template_name,context)
    
    def post(self,request):
          form=self.form(request.POST)
          if form.is_valid():
                form.save()
                return redirect('post_form')
          context={'form':self.form}
          return render(request,self.template_name,context)

class PostView(View):
      form=PostForm
      def get(self,request):
            template_name='blog/create_post.html'
            form=self.form()
            context={'form':form}
            return render(request,template_name,context)
    
      def post(self,request):
          template_name='blog/create_post.html'
          form=self.form(request.POST)
          if form.is_valid():
                form.save()
                return redirect('allpost_url')
          context={'form':self.form}
          return render(request,template_name,context)

class All_Post(View):
      def get(self,request):
            obj=Post.objects.order_by('-publication_date').all()
            template_name='blog/all_post.html'
            context={'obj':obj}
            return render(request,template_name,context)


def search(request):
      query=request.GET.get('q')
      if query:
            posts=Post.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
      else:
            posts = Post.objects.all()
      context={'posts':posts}
      return render(request,'blog/search.html',context)



