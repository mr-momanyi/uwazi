from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Post, Comment, Like, Profile
# from django.contrib.auth import logout

from django.shortcuts import render
from .models import Post

def home(request):
    county = request.GET.get('county')
    
    # Fetch trending posts
    trending_posts = Post.objects.annotate(
        total_interactions=Count('likes') + Count('comments')
    ).order_by('-total_interactions')[:10]  # Adjust limit as needed

    if county:
        posts = Post.objects.filter(county=county).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    
    return render(request, 'uongozini/home.html', {'posts': posts, 'county': county, 'trending_posts': trending_posts})

@login_required
def upload_post(request):
    if request.method == 'POST':
        image = request.FILES['image']
        description = request.POST['description']
        county = request.POST['county']
        Post.objects.create(user=request.user, image=image, description=description, county=county)
        return redirect('home')
    return render(request, 'uongozini/upload.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    comments = post.comments.all()
    likes = post.likes.count()
    return render(request, 'uongozini/post_detail.html', {'post': post, 'comments': comments, 'likes': likes})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        text = request.POST['text']
        Comment.objects.create(post=post, user=request.user, text=text)
    return redirect('home')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(post=post, user=request.user)
    return redirect('home')

@login_required
def leaderboard(request):
    users = User.objects.annotate(
        post_count=Count('post'),
        like_count=Count('post__likes'),
        comment_count=Count('post__comments')
    ).order_by('-post_count', '-like_count', '-comment_count')
    return render(request, 'uongozini/leaderboard.html', {'users': users})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'uongozini/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')

from django.contrib.auth import logout

def logoutview(request):

    return redirect ('home')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'uongozini/register.html', {'form': form})
