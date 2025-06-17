from django.shortcuts import render,redirect
from django.templatetags.i18n import language
from django.urls import reverse_lazy



from movielist.models import Movie
from movielist.forms import MovieForm
# def addmovie(request):
#     if request.method=="POST":
#         print(request.POST)
#         print(request.FILES)
#         form_instance = MovieForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             m=Movie.objects.create(movie_name=form_instance.cleaned_data['movie_name'],
#                                    description=form_instance.cleaned_data['description'],
#                                    director_name=form_instance.cleaned_data['director_name'],
#                                    language=form_instance.cleaned_data['language'],
#                                    year=form_instance.cleaned_data['year'],
#                                    image=form_instance.cleaned_data['image'])
#             m.save()
#             return redirect('movielist')
#
#     form_instance=MovieForm()
#     return render(request, 'addmovie.html',{'form':form_instance})


# class based view using create class
from django.views.generic import CreateView, UpdateView


class AddMovieView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'addmovie.html'
    success_url = reverse_lazy('movielist')




# def movielist(request):
#     m=Movie.objects.all()
#     print(m)
#     return render(request,'movielist.html',{'movies':m}


# Class based view using listview
from django.views.generic import ListView, CreateView
class MovieListView(ListView):
    model = Movie
    template_name = 'movielist.html'
    context_object_name = 'movies'



# def moviedetail(request,i):
#     m=Movie.objects.get(id=i)
#     return render(request,'moviedetail.html',{'movie':m})

from django.views.generic import DetailView
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'moviedetail.html'
    context_object_name = 'movie'




# # delete movie view
# def deletemovie(request,i):
#     m=Movie.objects.get(id=i)
#     m.delete()
#     return redirect('movielist')

from django.views.generic import DeleteView
class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'deletemovie.html'
    success_url = reverse_lazy('movielist')




# def editmovie(request,i):
#     m=Movie.objects.get(id=i)
#     if(request.method=="POST"):
#         form_instance=MovieForm(request.POST,request.FILES,instance=m)
#         if (form_instance.is_valid()):
#             form_instance.save()
#             return redirect('movielist')
#     form_instance = MovieForm(instance=m)
#     return render(request, 'editmovie.html',{'form':form_instance})

 # Update view class
from django.views.generic import UpdateView
class EditMovieView(UpdateView):
    form_class = MovieForm
    template_name = 'editmovie.html'
    model = Movie
    success_url = reverse_lazy('movielist')