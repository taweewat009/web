from django.shortcuts import render
from database.models import Category
from .models import Blogs
from django.core.paginator import Paginator , EmptyPage , InvalidPage

# Create your views here.
def index(request):
    categories = Category.objects.all()
    blog = Blogs.objects.all()
    lastest = Blogs.objects.all().order_by('-pk')[:4]


    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    # บทความแนะนำ
    recommend = Blogs.objects.all().order_by('views')[:3]


    #pagination การแบ่งเพจ
    paginator = Paginator(blog, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        blogperpage = paginator.page(page)
    except (EmptyPage,InvalidPage):
        blogperpage = paginator.page(paginator.num_pages)


    return render(request, 'index.html',{'categories':categories, 'blog':blogperpage, 'lastest':lastest,'page':page, 'popular':popular, 'recommend':recommend})

def blogdetail(request, id):
    categories = Category.objects.all()   # อ่านข้อมูลหมวดหมู่ทั้งหมด แล้วเก็บในตัวแปร categories

    lastest = Blogs.objects.all().order_by('-pk')[:4]   # อ่านของข้อมูลblogทั้งหมด แล้วเรียงลำดับตาม id จากมากไปน้อย เอาแค่4 ตัว เก็บในตัวแปร lastest

    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    # บทความแนะนำ
    recommend = Blogs.objects.all().order_by('views')[:3]
    
    singleblog = Blogs.objects.get(id=id) #อ่านข้อมูลโดยเข้าถึง id ที่รับมาจาก template  
    singleblog.views = singleblog.views+1  # แสดงยอดวิวเข้าชม 
    singleblog.save()  # บันทึกข้อมูล
    return render(request, 'blog.html',{'singleblog':singleblog,'categories':categories, 'lastest':lastest, 'popular':popular, 'recommend':recommend})

def searchCategory(request,category_id):
    
    blogs = Blogs.objects.filter(category_id = category_id)
       # อ่านข้อมูลหมวดหมู่ทั้งหมด แล้วเก็บในตัวแปร categories
    categories = Category.objects.all()   

    lastest = Blogs.objects.all().order_by('-pk')[:4]   # อ่านของข้อมูลblogทั้งหมด แล้วเรียงลำดับตาม id จากมากไปน้อย เอาแค่4 ตัว เก็บในตัวแปร lastest

    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    # บทความแนะนำ
    recommend = Blogs.objects.all().order_by('views')[:3]

    


    return render(request, 'searchcategory.html',{'blogs':blogs,'categories':categories ,'lastest':lastest, 'popular':popular, 'recommend':recommend})



def aboutme(request):
    
       # อ่านข้อมูลหมวดหมู่ทั้งหมด แล้วเก็บในตัวแปร categories
    categories = Category.objects.all()   

    lastest = Blogs.objects.all().order_by('-pk')[:4]   # อ่านของข้อมูลblogทั้งหมด แล้วเรียงลำดับตาม id จากมากไปน้อย เอาแค่4 ตัว เก็บในตัวแปร lastest

    # บทความยอดนิยม
    popular = Blogs.objects.all().order_by('-views')[:3]

    # บทความแนะนำ
    recommend = Blogs.objects.all().order_by('views')[:3]

    return render(request, 'about.html',{'categories':categories ,'lastest':lastest, 'popular':popular, 'recommend':recommend})


def lesson(request):
    catgories = Category.objects.all()
    blog = Blogs.objects.all()
    
    
    return render(request , 'lesson.html',{'blog':blog,'categories':catgories} )