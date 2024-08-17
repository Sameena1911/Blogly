from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail

"""
STATIC DEMO DATA
posts=[
        {'id':1, 'title':'Post 1', 'content':'content of post 1'},
        {'id':2,'title':'Post 2', 'content':'content of post 2'},
        {'id':3,'title':'Post 3', 'content':'content of post 3'},
        {'id':4,'title':'Post 4', 'content':'content of post 4'},
        {'id':5,'title':'Post 5', 'content':'content of post 5'},
        {'id':6,'title':'Post 6', 'content':'content of post 6'},
        
        
    ]
"""


def index(request):
    blogly_title = "Latest news"
    # getting data from post model
    all_posts = Post.objects.all()
    # paginate
    paginator = Paginator(all_posts, 6)
    page_no = request.GET.get("page")
    page_object = paginator.get_page(page_no)

    return render(
        request, "index.html", {"blog_title": blogly_title, "page_object": page_object}
    )


def detail(request, slug):
    """
    static data
    post = next((item for item in posts if item['id'] == int(post_id)), None)
    """
    # getting data from post model
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("post does not exist")
    return render(
        request, "detail.html", {"post": post, "related_posts": related_posts}
    )


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(name, email, message)
        send_mail(
            "BLOGLY CHAT",
            "my name is "+name+", my msg is "+message+", my email is "+email,
            email,
            ["feroz8955@gmail.com"],
            fail_silently=False,
        )
    return render(request, "contact.html")


def about_view(request):
    return render(request, "about.html")
