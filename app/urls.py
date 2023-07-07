from django.urls import path

from app.views import index_view, project_view, blog_view, add_contact

urlpatterns = [
    path('', index_view, name='index'),
    path('project/<int:project_id>', project_view, name='project'),
    path('blog/<int:blog_id>', blog_view, name='blog'),
    path('contact/', add_contact, name='add_contact')
]