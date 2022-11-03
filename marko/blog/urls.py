from django.urls import path 
from . import views 

app_name = "blog"
urlpatterns = [
    path('<int:id>',views.blog_detail,name="blog_detail")
]