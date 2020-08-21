from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Posts
from django.db.models import F
from .forms import InputPostForm


def index(request):
    data = Posts.objects.order_by('-post_date')
    return render(request, "index.html", {
        "data": data,
        "title": "Ghost Post"
    })


def boasts_view(request):
    data = Posts.objects.filter(boast=True).order_by('-post_date')
    return render(request, "boasts.html", {
        "data": data,
        "title": "Ghost Post - Boasts"
    })


def roasts_view(request):
    data = Posts.objects.filter(boast=False).order_by('-post_date')
    return render(request, "roasts.html", {
        "data": data,
        "title": "Ghost Post - Roasts"
    })


def score_view(request):
    data = Posts.objects.order_by(
        -(F('up_votes') - F('down_votes')))

    return render(request, "score.html", {
        "data": data,
        "title": "Ghost Post - Scores"
    })


def upvote_view(request, post_id):
    post_value = Posts.objects.get(id=post_id)
    post_value.up_votes = F('up_votes') + 1
    post_value.save()
    return HttpResponseRedirect(reverse("homepage"))


def downvote_view(request, post_id):
    post_value = Posts.objects.get(id=post_id)
    post_value.down_votes = F('down_votes') + 1
    post_value.save()
    return HttpResponseRedirect(reverse("homepage"))


def add_post_view(request):
    if request.method == "POST":
        form = InputPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posts.objects.create(
                text=data.get("text"),
                boast=data.get("boast")
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = InputPostForm()
    return render(request, "add_post.html", {
        "title": "Ghost Post - Add Post",
        "form": form
    })
