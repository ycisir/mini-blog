from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})


def dashboard_page(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        fullname = user.get_full_name()
        groups = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'fullname':fullname, 'groups':groups})
    else:
        return HttpResponseRedirect('login')

def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return HttpResponseRedirect('dashboard')
        else:
            form = LoginForm()

        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('dashboard')

def signup_page(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request, 'Account created successfully!')
            return HttpResponseRedirect('login')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

def logout_page(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return HttpResponseRedirect('login')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                tmp = Post(title=title, desc=desc)
                tmp.save()
                messages.success(request, 'Post added successfully!')
                return HttpResponseRedirect('dashboard')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('login')
    

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            tmp = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=tmp)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post updated successfully!')
                return redirect('dashboard')
        else:
            tmp = Post.objects.get(pk=id)
            form = PostForm(instance=tmp)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('login')
    

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            tmp = Post.objects.get(pk=id)
            tmp.delete()
            messages.success(request, 'Post deleted successfully!')
            return redirect('dashboard')
    else:
        return HttpResponseRedirect('login')