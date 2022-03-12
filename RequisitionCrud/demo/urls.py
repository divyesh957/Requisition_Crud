from django.urls import path
from demo import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),

    path('changepasswordform', views.changepasswordform, name='changepasswordform'),
    path('changepassword/<int:id>', views.changepassword, name='changepassword'),

    path('addCategory', views.addCategory, name='addCategory'),
    path('Category', views.Category, name='Category'),

    path('deleteCategory/<int:id>', views.deleteCategory, name='deleteCategory'),

    path('updateCategory/<int:id>', views.updateCategory, name='updateCategory'),
    path('updateCategoryData/<int:id>', views.updateCategoryData, name='updateCategoryData'),

    path('addsubCategory', views.addsubCategory, name='addsubCategory'),
    path('subCategory', views.subCategory, name='subCategory'),

]
