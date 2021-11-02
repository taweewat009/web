from django.urls import path
from .views import panel, displayform, insertdata, deleteData, editData,updateData

urlpatterns = [
    path('',panel, name="panel"),
    path('displayform',displayform, name="displayform"),
    path('insertdata',insertdata, name="insertdata"),
    path('deleteData/<int:id>',deleteData,name="deleteData"),
    path('editData/<int:id>',editData,name="editData"),
    path('updateData/<int:id>',updateData,name="updateData"),
]

