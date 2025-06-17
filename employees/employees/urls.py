"""
URL configuration for employees project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views
from django.conf.urls.static import static
from django.conf import settings
# from employees.employee.views import create_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.employee_list,name="employee_list"),
    path('create_employee',views.create_employee,name="create_employee"),
    path('displayemployee/<int:i>',views.displayemployee,name="displayemployee"),
    path('editemployee/<int:i>',views.editemployee,name="editemployee"),
    path('deleteemployee/<int:i>',views.deleteemployee,name="deleteemployee"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
