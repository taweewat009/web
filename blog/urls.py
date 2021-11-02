from django.contrib import admin
from django.urls import path , include
from .views import index, blogdetail,searchCategory,aboutme , lesson

urlpatterns = [
    path('',index,name="index"),
    path('blog/<int:id>',blogdetail,name="blogdetail"),
    path('blog/category/<int:category_id>',searchCategory,name="searchCategory"),
    path('about,',aboutme,name="aboutme"),
    path('lesson',lesson, name="lesson"),
    
]
