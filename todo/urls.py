from django.urls import path
from django.contrib import admin
from .views import index, remove

urlpatterns = [
    path('', index, name="todo"),
    path('del/<int:item_id>', remove, name="del"),
    path('admin/', admin.site.urls),
]