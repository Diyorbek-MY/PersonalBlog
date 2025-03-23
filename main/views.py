from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django import forms

# ✅ Home Page View
def home(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'main/home.html', {'posts': posts})

# ✅ Post Detail View
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_detail.html', {'post': post})

# ✅ Create a form for new posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# ✅ View to handle new post creation
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to homepage after saving
    else:
        form = PostForm()
    
    return render(request, 'main/create_post.html', {'form': form})

# ✅ Signup View (You referenced it in URLs but didn't define it)
def signup(request):
    return render(request, 'main/signup.html')  # Placeholder, update later
