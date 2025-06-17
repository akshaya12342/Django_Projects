from django.shortcuts import render,redirect
from django.template.defaultfilters import title
from django.templatetags.i18n import language



# def home(request):
#     return render(request,'home.html',)

# Class Based views
from django.views import View
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')





from books.models import Book
# def addbook(request):
    # if(request.method=="POST"):
    #     print(request.POST)
    #     print(request.FILES)
    #     t=request.POST['t']
    #     a=request.POST['a']
    #     p=request.POST['p']
    #     pg=request.POST['pg']
    #     l=request.POST['l']
    #     i=request.FILES['i']
    #     b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l,image=i)
    #     b.save()
    #     return render(request,'addbook.html')
    # return render(request,'addbook.html')

#      Class Based View
class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'addbook.html')
    def post(self,request,*args,**kwargs):
            t = request.POST['t']
            a=request.POST['a']
            p=request.POST['p']
            pg=request.POST['pg']
            l=request.POST['l']
            i=request.FILES['i']
            b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l,image=i)
            b.save()
            return redirect('books:viewbook')





from books.forms import BookForm
# def addbook1(request):
#     if(request.method=="POST"):
#         # print(request.POST)
#         # print(request.FILES)
#         form_instance=BookForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             # b=Book.objects.create(title=form_instance.cleaned_data['title'],
#             #                   author=form_instance.cleaned_data['author'],
#             #                   pages=form_instance.cleaned_data['pages'],
#             #                   price=form_instance.cleaned_data['price'],
#             #                   language=form_instance.cleaned_data['language'],
#             #                   image=form_instance.cleaned_data['image'])
#             # b.save()
#             # or
#             form_instance.save()
#             return redirect('books:home')
#     form_instance=BookForm()
#     return render(request,'addbook1.html',{'form':form_instance})

class AddBook1View(View):
    def get(self,request,*args,**kwargs):
        form_instance = BookForm()
        return render(request,'addbook1.html',{'form':form_instance})
    def post(self,request,*args,**kwargs):
        form_instance = BookForm(request.POST, request.FILES)
        if form_instance.is_valid():
             # b=Book.objects.create(title=form_instance.cleaned_data['title'],
             #                       author=form_instance.cleaned_data['author'],
             #                       pages=form_instance.cleaned_data['pages'],
             #                       price=form_instance.cleaned_data['price'],
             #                       language=form_instance.cleaned_data['language'],
             #                       image=form_instance.cleaned_data['image'])
             # b.save()
             #    #  or
             form_instance.save()
        return redirect('books:viewbook')




# def viewbook(request):
#     b=Book.objects.all()
#     print(b)
#     return render(request,'viewbook.html',{'books':b})

class ViewBookView(View):
    def get(self,request,*args,**kwargs):
        b=Book.objects.all()
        return render(request,'viewbook.html',{'books':b})



# detail view
# def bookdetail(request,i):
#     # print(i)
#     b=Book.objects.get(id=i)
#     return render(request,'bookdetail.html',{'book':b})

class BookDetailView(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        return render(request,'bookdetail.html',{'book':b})

# edit view
# def editbook(request,i):
#     b = Book.objects.get(id=i)
#     if(request.method=="POST"):
#         form_instance=BookForm(request.POST,request.FILES,instance=b)
#         if(form_instance.is_valid()):
#             form_instance.save()
#             return redirect('books:viewbook')
#
#     form_instance=BookForm(instance=b)
#     return render(request,'editbook.html',{'form':form_instance})


class EditBookView(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        return render(request,'editbook.html',{'form':form_instance})
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance = BookForm(request.POST, request.FILES, instance=b)
        if (form_instance.is_valid()):
             form_instance.save()
        return redirect('books:viewbook')

# delete view
# def deletebook(request,i):
#     b=Book.objects.get(id=i)
#     b.delete()
#     return redirect('books:viewbook')

class DeleteBookView(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbook')


from django.db.models import Q
# def searchbook(request):
#     if(request.method=="POST"):
#         data=request.POST['q']
#         print(data)
#         # __contains=Django lookups
#         # syntax- (field_name__lookup eg: age__gt,age__lt,title__contains,title__icontains)
#
#         b=Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) | Q(language__contains=data))
#         # filter condition - to read 2 or more records from a table
#         # Q object - To use logical and/or/not syntax in ORM Queries
#         print(b)
#         context={'books':b}
#         return render(request,'searchbook.html',context)
#     return render(request,'searchbook.html')


class SearchBookView(View):
    def get(self,request):
        return render(request, 'searchbook.html')
    def post(self,request):
        data = request.POST['q']
        print(data)
        b = Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) | Q(language__contains=data))
        print(b)
        context = {'books': b}
        return render(request, 'searchbook.html', context)