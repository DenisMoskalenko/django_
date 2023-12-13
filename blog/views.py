from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 

 
from .models import Post
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    def get_queryset(self):
        if self.request.user.is_authenticated:  
            
            if self.request.user.is_superuser:
                return Post.objects.all()
            return Post.objects.filter(author=self.request.user)
        else:
            return Post.objects.none() 
 
 
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
 
 
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 
 
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
 
 
class BlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
