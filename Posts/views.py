from django.shortcuts import redirect, render
from . models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import NewsletterForm, CommentForm, PostForm

# Create your views here.

def Index(request):
    post = Post.objects.filter(tag='MainContent')
    sub = Post.objects.filter(tag='SubContent')
    popular = Post.objects.filter(tag="Popular")
    news = Post.objects.filter(tag="News")
    top = Post.objects.all()[:4]
    post_count = top.count()

    # Categories

    lifestyle = Post.objects.filter(category="Lifestyle").count()
    fashion = Post.objects.filter(category="Fashion").count()
    tech = Post.objects.filter(category="Technology").count()
    art = Post.objects.filter(category="Art").count()
    travel = Post.objects.filter(category="Travel").count()
    health = Post.objects.filter(category="Health").count()
    food = Post.objects.filter(category="Food").count()
    nature = Post.objects.filter(category="Nature").count()
    gaming = Post.objects.filter(category="Gaming").count()

    context = {
        'post':post, 
        'sub': sub,
        'popular': popular,
        'news': news,

        'lifestyle': lifestyle,
        'fashion': fashion,
        'tech': tech,
        'art': art,
        'travel': travel,
        'health': health,
        'food': food,
        'nature': nature,
        'gaming': gaming,

        'top': top,
        'post_count': post_count,
    }   

    return render(request, 'Posts/index.html',context)

@login_required(login_url="login")
def details(request, pk):
    det = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have Subscribed to our Newsletter successfully!")
            return redirect('home')

        reply = CommentForm(request.POST)
        if reply.is_valid():
            reply.save()
            # messages.success(request, "Post Reply sent successfully!")
            return redirect('home')
    else:
        form = NewsletterForm()
        reply = CommentForm()
    return render(request, 'Posts/details.html', {'det': det, 'form':form, 'reply': reply})

def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, f"{title} post created successfully!!")
            return redirect("home")
    else:
        form = PostForm()
    return render(request, 'Posts/CreatePost.html', {'form': form})

def About(request):
    return render(request, 'Posts/about.html')

# def Search(request):
#     post_list = Post.objects.all()
#     filter = PostFilter(request.GET, queryset=post_list)
#     return render(request, 'Posts/base.html', {'filter': filter})