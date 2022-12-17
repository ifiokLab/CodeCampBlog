
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.views import LoginView,LogoutView
from .forms import MyLoginForm
from .models import *
from django.db.models import Q
from taggit.models import Tag
from django.http import HttpResponseRedirect
# Create your views here.


def Signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Blog/registration.html', {'form': form})


def home(request):
    posts = Post.objects.filter(status = 'published')
    recent_posts = posts[0:3]
    category = Categories.objects.all()
    
    return render(request,'Blog/home.html',{'posts':posts,'recent_posts':recent_posts,'category':category})

class Login(LoginView):
  form_class = MyLoginForm





def Search_Result(request):
    #search
  
    if request.method == 'POST':
        query = request.POST['query']
        posts = Post.published.filter(Q(title__icontains = query) | Q(tags__name__icontains = query)).distinct()

    #recent post
    recent_posts  = Post.objects.filter(status = 'published')[0:3]
    return render(request,'Blog/search.html',{'posts':posts,'recent_posts':recent_posts,'query':query})


def Post_Detail(request,pk):
    #get post object by id
   
    post = Post.objects.get(id = pk)
    comments = post.comments.filter(active = True)
    recent_posts  = Post.objects.filter(status = 'published')[0:3]
    category = Categories.objects.all()
    print(request.POST)
    comment_form = CommentForm(data = request.POST)
    if request.method == 'POST' and comment_form.is_valid():
        
        body = comment_form.cleaned_data['body']

        try:
            parent = comment_form.cleaned_data['parent']
        except:
            parent = None
        print(body)
        new_comment = BlogComment(body = body,User = request.user,post = post,parent = parent)
        new_comment.save()

    return render(request,'Blog/post_detail.html',{'post':post,'recent_posts':recent_posts,'category':category,'comments':comments,'comment_form':comment_form })





'''
def Post_Detail(request,pk):
   
    #get post object by id
    post = Post.objects.get(id = pk)
    # list active parent comments
    comments = post.comments.filter(active = True)
    recent_posts  = Post.objects.filter(status = 'published')[0:3]
    category = Categories.objects.all()
    if request.method == 'POST':
        # comments has been added
        comment_form = CommentForm(data = request.POST)
        
        if comment_form.is_valid():
            reply_obj = None
            
            print(request.POST)
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            if reply_id:
                reply_obj = BlogComment.objects.get(id = reply_id)
            print(comment_form.cleaned_data)
            author = request.user
            comment = comment_form.cleaned_data['body']
            if reply_obj:
               BlogComment(User = author,body = comment,parent =reply_obj,post = post).save()
            else:
                BlogComment(User = author,body = comment,post = post).save()
            return redirect(reverse('Post_Detail',args = [post.id]))
    else:
        comment_form = CommentForm()


    return render(request,'Blog/post_detail.html',{'post':post,'recent_posts':recent_posts,'category':category,'comments':comments,'comment_form':comment_form })

'''












'''
if request.method == 'POST':
        # comments has been added
        comment_form = CommentForm(data = request.POST)
        print(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            #get parent obj id from hiddent input
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            #if parent id has been submitted get the parent_obj id
            if parent_id:
                parent_obj = BlogComment.objects.get(id = parent_id)
                #if parent object exist
                if parent_obj:
                    #create reply comment object
                    reply_comment = CommentForm.save(commit=False)
                    #assign parent obj to reply obj
                    reply_comment.parent = parent_obj
            #normal comment
            #create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            #assign ship to the comment 
            new_comment.post = post

            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
'''