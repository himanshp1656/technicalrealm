from django.shortcuts import render , HttpResponseRedirect
from .models import submitform , contactmdl , topposts
# Create your views here.

def home(request):
    posts=topposts.objects.all()
    def reverse(lst):
        new_lst=lst[::-1]
        return new_lst
    lst=posts
    lst=reverse(lst)
    print(posts)
    return render(request,'index.html' ,{'lst': lst})  

def recent(request):
    posts=submitform.objects.all()
    dots=topposts.objects.all()
    def reverse(lst):
        new_lst=lst[::-1]
        return new_lst
    lst=posts
    lst=reverse(lst)
    print(posts)
    print(dots)
    print('hey')

    return render(request,'recentblog.html' ,{'lst': lst , 'dots':dots}) 

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def adminposting(request):
    return render(request,'adminposting.html')

# def submit(request):
#     if request.method=='POST':
#         topic=request.POST['topic']
#         file=request.POST['file']
#         content=request.POST['content']
#         justcontent=request.POST['justcontent']
#         slug=request.POST['slug']
#         # print(name,email,phone,skills)
#         sb=submitform(topic=topic,file=file,content=content,justcontent=justcontent,slug=slug)
#         sb.save()

#     return render(request,'index.html')


def contactproblem(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        contactprob=request.POST['contactprob']
        # print(name,email,phone,skills)
        ab=contactmdl(name=name,email=email,contactprob=contactprob)
        ab.save()
    return HttpResponseRedirect('/contact')

def search(request):
    if request.method=='GET':
        search=request.GET['search']
        topic=submitform.objects.filter(topic__icontains=search)
        print(topic)
        return render(request,'searchedblog.html' ,{'topic':topic})

    # else:
    #     topic=submitform.objects.all()
    #     print(topic)
    #     return render(request,'searchedblog.html' ,{'topic': topic})   
     

def blog(request,slug):
    print('yes it reched blog')
    posts=submitform.objects.filter(slug=slug).first()

    print(posts)

    return render(request,'blog.html',{'posts':posts})

def top_posts(request,top_slug):
    print('yes it reched')
    posts=topposts.objects.filter(top_slug=top_slug).first()
    print(posts)
    return render(request,'toppost.html',{'posts':posts})


def privacy(request):
    return render(request,'privacy.html')

def disclaimer(request):
    return render(request,'disclaimer.html')
def term(request):
    return render(request,'term.html')
