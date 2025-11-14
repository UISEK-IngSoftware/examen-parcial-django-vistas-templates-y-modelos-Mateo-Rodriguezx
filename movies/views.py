from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})


def add_movie(request):
    if request.method == "POST":
        Movie.objects.create(
            Título=request.POST["Título"],
            Año=request.POST["Año"],
            Director=request.POST["Director"],
            Categoría=request.POST["Categoría"],
            Sinapsis=request.POST["Sinapsis"],
            imagen=request.FILES.get("imagen")
        )
        return redirect("movies:index")

    return render(request, "movie_form.html")


def edit_movie(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        movie.Título = request.POST["Título"]
        movie.Año = request.POST["Año"]
        movie.Director = request.POST["Director"]
        movie.Categoría = request.POST["Categoría"]
        movie.Sinapsis = request.POST["Sinapsis"]

        if request.FILES.get("imagen"):
            movie.imagen = request.FILES["imagen"]

        movie.save()
        return redirect("movies:index")

    return render(request, "movie_form.html", {"movie": movie})


def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return redirect("movies:index")


def view_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, "view_movie.html", {"movie": movie})
