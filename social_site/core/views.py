from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from forum.models import Discussione, Sezione, Post
from django.views.generic.list import ListView
# Create your views here.

# def homepage(request):
#     return render(request, "core/homepage.html")


class HomeView(ListView):
    queryset = Sezione.objects.all()
    template_name = "core/homepage.html"
    context_object_name = "lista_sezioni"


class userListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "core/users.html"


def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    discussioni_utente = Discussione.objects.filter(autore=user).\
        order_by("-pk")
    context = {'user': user, "discussioni_utente": discussioni_utente}
    return render(request, "core/user_profile.html", context)


# "Cerca" utilizza GET, invece di POST. Di default se il metodo non è definito,
# viene utilizzato GET.
def cerca(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/cerca/")
        discussioni = Discussione.objects.filter(titolo__icontains=querystring)
        posts = Post.objects.filter(contenuto__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {"discussioni": discussioni,
                   "posts": posts,
                   "users": users}
        return render(request, "core/cerca.html", context)
    else:
        return render(request, "core/cerca.html")
