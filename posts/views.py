from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.mail import send_mail


# Function for showing Post lists
def post_list(request):
    posts = Post.objects.all().order_by('date_posted')
    return render(request, 'posts/post_list.html', {'posts': posts})

# Function for creating posts
@login_required(login_url = "/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save post to database
            instance = form.save(commit = False)
            instance.owner = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_create.html', {'form': form})

# Function for showing details of any particular post
@login_required(login_url = "/accounts/login/")
def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'posts/post_detail.html', {'post': post})


# Function for showing users' own advertisements        
def my_post(request):
    post = Post.objects.all()
    return render (request, 'posts/my_post.html',{'post': post})


# Function for searching
def search_bar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        post = Post.objects.filter(place__contains = searched)
        return render (request, 'posts/search_bar.html',{'searched': searched, 'post': post})

# Function for updating a particular post
def post_update(request,id):
    post = Post.objects.get(id=id)
    form = forms.CreatePost(request.POST or None, request.FILES or None, instance = post)
    if form.is_valid():
        form.save()
        return redirect('posts:detail', post.id)
    return render(request,'posts/post_update.html', {'post': post, 'form': form})

# Function to delete a post
def post_delete(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect('posts:myPost')
    return render(request, 'posts/post_delete.html',{'post': post})

# Funtion to filter posts by Budget
def post_filters(request):

    query = request.GET['query']
    if query == "0":
        post = Post.objects.filter(rent__gte = 0)
        return render(request, 'posts/filter.html',{'post': post})
    elif query == "1":
        post = Post.objects.filter(rent__lt = 15000)
        return render(request, 'posts/filter.html',{'post': post})
    elif query == "2":
        post = Post.objects.filter(rent__range = (15000,20000))
        return render(request, 'posts/filter.html', {'post': post})
    elif query == "3":
        post = Post.objects.filter(rent__range = (20001,25000))
        return render(request, 'posts/filter.html', {'post': post})
    elif query == "4":
        post = Post.objects.filter(rent__range = (25001,30000))
        return render(request, 'posts/filter.html', {'post': post})
    elif query == "5":
        post = Post.objects.filter(rent__range = (30001,40000))
        return render(request, 'posts/filter.html', {'post': post})
    elif query == "6":
        post = Post.objects.filter(rent__range = (40001,50000))
        return render(request, 'posts/filter.html', {'post': post})
    elif query == "7":
        post = Post.objects.filter(rent__gt = 50000)
        return render(request, 'posts/filter.html', {'post': post})
        
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # Sending a mail
        send_mail(
            message_name,
            message,
            message_email,
            ['sumiya.sadia@northsouth.edu', 'ezaz.ahamed@northsouth.edu', 'sumiya.sadia97@gmail.com', 'turkidot@gmail.com'] # Email addresses
        )
        return render(request, 'posts/contact.html', {'post': message_name, 'message_email': message_email, 'message': message})
    else:
        return render(request, 'posts/contact.html', {})