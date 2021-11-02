from django.shortcuts import render,redirect
from blog.models import Blogs
from database.models import Category
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.

@login_required(login_url="member")
def panel(request):
    writer= auth.get_user(request)
    blog = Blogs.objects.filter(writer=writer)
    blogCount = blog.count()
    total_view = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    return render(request, 'backends/index.html',{'blog':blog, 'writer':writer,'blogCount':blogCount,'total_view':total_view})



def displayform(request): 
    writer= auth.get_user(request)
    blog = Blogs.objects.filter(writer=writer)
    blogCount = blog.count()
    total_view = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    categories = Category.objects.all()
    return render(request , 'backends/displayform.html',{'blog':blog, 'writer':writer,'blogCount':blogCount,'total_view':total_view,'categories':categories})


def insertdata(request):
    try:
        if request.method == "POST" and request.FILES["image"]:
            datafile = request.FILES["image"]

            # รับค่าจากฟอร์ม 
            name = request.POST["name"]
            category = request.POST["category"]
            description = request.POST["description"]
            content = request.POST["content"]
            writer = auth.get_user(request)

            if str(datafile.content_type).startswith("image"): 
                fs = FileSystemStorage()
                img_url = "blogsImage/"+datafile.name
                filename = fs.save(img_url,datafile)
                blog = Blogs(name=name,category_id=category,description=description,content=content,writer=writer,images=img_url)
                blog.save()
                messages.info(request,"บันทึกข้อมูลเรียบร้อย")
                return redirect("displayform")
            else:
                messages.info(request,"ไฟล์ที่อัพโหลดไม่รองรับ กรุณาอัพโหลดไฟล์รูปภาพอีกครั้ง")
                return redirect("displayform")
    except:
        return redirect("displayform")
    

def deleteData(request, id):
    try:
        blog = Blogs.objects.get(id=id)
        fs = FileSystemStorage()

        #ลยภาพที่ค้างอยู่
        fs.delete(str(blog.images))


        #ลบข้อมูลจากฐานข้อมูล
        blog.delete()
        return redirect("panel")
    except:
        return redirect("panel")
    

def editData(request,id):
    writer= auth.get_user(request)
    blog = Blogs.objects.filter(writer=writer)
    blogCount = blog.count()
    total_view = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    categories = Category.objects.all()

    blogedit = Blogs.objects.get(id=id)

    
    return render(request, 'backends/editform.html',{'blogedit':blogedit,'writer':writer,'blogCount':blogCount,'total_view':total_view,'categories':categories})

def updateData(request, id):
    try:
         if request.method == "POST":
             # ดึงข้อมูลเดิมที่ต้องการแก้ไขมาใช้งาน
            blog = Blogs.objects.get(id=id) 
            # รับค่าจากฟอร์ม ห
            name = request.POST["name"]
            category = request.POST["category"]
            description = request.POST["description"]
            content = request.POST["content"]


        #อัพเดทข้อมล
            blog.name = name
            blog.category_id = category
            blog.description = description
            blog.content = content
            blog.save()
        
            if request.FILES["image"]:
                datafile = request.FILES["image"]
                if str(datafile.content_type).startswith("image"):
                    fs = FileSystemStorage()
                    fs.delete(str("blog.images"))

                    img_url = "blogsImage/"+datafile.name
                    filename = fs.save(img_url,datafile)    
                    blog.images = img_url
                    blog.save()
            return redirect("panel")
    except:
        return redirect("panel")


   
        

    
        