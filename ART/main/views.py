from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import Blog,Comment
from django.contrib.auth.models import User
# Create your views here.
from .models import Blog, Comment, Contact


# ..................صفحه الهوم....................

def home(request:HttpRequest):
     #get user info
    if request.user.is_authenticated:
        print(request.user.first_name)
    comments=Comment.objects.all()[0:3]
    art = Blog.objects.all()[0:3]


    return render(request,'main/index.html', {'art' : art ,'comments' : comments})
    
# .............................الان نسوي add.........................
def add_images(request:HttpRequest):
      if request.method == 'POST':
        try:
            new_blog = Blog(user=request.user,name = request.POST["name"],about = request.POST["about"],
                            image = request.FILES.get("image", Blog.image.field.default),
                            is_published = request.POST.get("is_published", False),category = request.POST['category'])
            new_blog.save()
            return redirect("main:detail_images",new_blog.id)
            
        except Exception as e:
            print(e)
        return redirect("main:all_images")

      return render(request, "main/add_images.html", {'category' : Blog.Categories.choices})

# ................الحين نسويي allllll.........................

def all_images(request:HttpRequest):
    user=request.user
    if "cat" in request.GET:
        art = Blog.objects.filter(category = request.GET["cat"])
    elif "user" in request.GET:
        user=User.objects.get(id=request.GET["user"])
        art = Blog.objects.filter(user =user )
    else:
        art = Blog.objects.all().order_by("-created_at") 
    
        #calculate the page content
    limit = 8
    pages_count = [str(n) for n in range(1, round(art.count()/limit)+1)]
    start = (int(request.GET.get("page", 1))-1)*limit
    end = (start)+limit

    print(list(pages_count))


    #apply the limit/slicing
    art = art[start:end]

    # print(start, end)

    return render(request, "main/all_images.html", {"art" : art, "category" : Blog.Categories.choices, "pages_count":pages_count})



# ....................الحين نبدا في detail...............
def detail_images(request:HttpRequest,blog_id):
    comments=[]
    related_posts=[]

    try:
        #getting a  post detail
        art = Blog.objects.get(pk=blog_id)
        comments = Comment.objects.filter(Blog=art) #this is to get the comments on the above post using filter
        related_posts = Blog.objects.filter(category=art.category).exclude(id=art.id) #get related posts
        # is_favored = request.user.is_authenticated and  Favorite.objects.filter(user=request.user, post=plant).exists()
    except Blog.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)


    return render(request, "main/detail_images.html", {"art" : art, "comments" :comments , "related" : related_posts  })
    

 # ............الحين Search .........................

def search(request:HttpRequest):
    art = []
    try: 
        if "search" in request.GET:
            art = Blog.objects.filter(name__contains=request.GET["search"])

        
        # if "date" in request.GET and len(request.GET["date"]) > 4:
        #     first_date = date.fromisoformat(request.GET["date"])
        #     end_date = first_date + timedelta(days=1)
        #     plants = plants.filter(created_at__gte=first_date, created_at__lt=end_date)
    except Exception as e:
        print(e)
    
    context = {"art" : art}
    return render(request,"main/Search.html", context)
    

def delete_images(request:HttpRequest,blog_id):
    try:
        art = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return render(request, "main/404.html")
    
    try:
        art.delete()
    except Exception as e:
        print(e)
    
    return redirect("main:home")



# ............الحين massage .........................

def user_massage(request:HttpRequest):
    if not request.user.is_superuser:
        return render(request, "main/not_found.html")
    
    con=Contact.objects.all()

    return render(request,"main/massage.html", {"con" : con})
    



# ............الحين contact .........................
def contact_us(request:HttpRequest):
 if request.method=="POST":
        try:
            info=Contact(
            f_name=request.POST["f_name"],
            l_name=request.POST["l_name"],
            email=request.POST["email"],
            message=request.POST["message"],
            )
            info.save()
            return redirect('main:home')
        except Exception as e :
            print(e)
 return render(request,"main/contact.html")

# ............الحين comment ......................... 

def add_comment(request:HttpRequest, blog_id):

    object = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        #add new comment
        print(object)
        new_comment = Comment(Blog=object,user=request.user, content=request.POST["content"])
        new_comment.save()
    
    return redirect("main:detail_images", blog_id=object.id)
# Create your views here.
# testttttttttttttttttttttttt
