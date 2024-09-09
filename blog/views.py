from django.shortcuts import render,redirect
from .forms import BlogForm , UserRegistrationForm
from .models import blog
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
import logging

# Create your views here.
def index(request):
    return render(request, 'index.html',{'title': 'Home'})

def blog_list(request):
    blogs=blog.objects.all().order_by('-created_at')
    return render(request,'blog_list.html',{'blogs':blogs})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  # Set the user to the currently logged-in user
            blog.save()
            return redirect('blog_list')  # Redirect to a success page or another view
    else:
        form = BlogForm()
    
    return render(request, 'create_blog.html', {'form': form})

@login_required
def blog_edit(request, blog_id):
    blog_instance = get_object_or_404(blog, pk=blog_id, user=request.user)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_instance)
        if form.is_valid():
            blog_instance = form.save(commit=False)  # Get the instance from the form
            blog_instance.user = request.user  # Ensure user is set (usually not needed if instance is correctly set)
            blog_instance.save()  # Save the instance
            return redirect('blog_list')  # Redirect to blog list view
    else:
        form = BlogForm(instance=blog_instance)
    
    return render(request, 'create_blog.html', {'form': form})

def blog_delete(request, blog_id):
    blog_instance = get_object_or_404(blog, pk=blog_id, user=request.user)
    
    if request.method == 'POST':
        blog_instance.delete()  # Delete the blog instance
        return redirect('blog_list')  # Redirect to blog list view

    return render(request, 'blog_confirm_delete.html', {'blog': blog_instance})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           user= form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request , user)
           return redirect(blog_list)
            
    else:
        form = UserRegistrationForm()
        
    return render(request, 'registration/register.html', {'form': form})

def blog_detail(request, blog_id):
    blog_instance = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog_instance})

# Define the search logger
search_logger = logging.getLogger('search_logger')

def search(request):
    query = request.GET.get('q', '')
    if query:
        # Assuming `blog` is the model where you're searching
        results = blog.objects.filter(text__icontains=query)
        
        # Log the search query with the username if available
        search_logger.info(f"Search query: '{query}' by User: {request.user.username if request.user.is_authenticated else 'Anonymous'}")
        
        return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        return render(request, 'search_results.html', {'results': [], 'query': query})