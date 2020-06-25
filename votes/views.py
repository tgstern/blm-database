from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .us_state_abbrev import *
import requests

# index view
def index(request):
    if request.method == "GET":
        context = {
            "locator": False,
        }
        return render(request, "votes/index.html", context)
    if request.method == "POST":
        if request.POST["state"] == "":
            return HttpResponseRedirect(reverse("index"))
        else:
            reps = None
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]
            zipcode = request.POST["zip"]
            if address and city and state and zipcode:
                params = {
                    "key": "__API_KEY__",
                    "address": address + city + state + zipcode,
                }
                req = requests.get("https://www.googleapis.com/civicinfo/v2/representatives", params=params)
                if req.status_code == 200:
                    r = req.json()
                    reps = []
                    for i in range(2, len(r["offices"])):
                        reps.append(r["offices"][i])
                    for office in reps:
                        office.update(person=[])
                        for i in office["officialIndices"]:
                            office["person"].append(r["officials"][i])
                    
            context = {
                "restaurants": Link.objects.filter(state=state, type="r"),
                "emails": Link.objects.filter(state=state, type="e"),
                "donate": Link.objects.filter(state=state, type="d"),
                "locator": True,
                "state": abbrev_us_state[state],
                "city": city,
                "reps": reps,
            }

            return render(request, "votes/index.html", context)

# learn view
def learn(request):
    context = {
        "learn": Link.objects.filter(type="l"),
    }
    return render(request, "votes/learn.html", context)

# remember view
def remember(request):
    context = {
        "memorials": Link.objects.filter(type="m"),
    }
    return render(request, "votes/remember.html", context)

# about view
def about(request):
    context = {
        "sources": Link.objects.filter(type="s"),
    }
    return render(request, "votes/about.html", context)

# send message
def send(request):
    Message.objects.create(text=request.POST["text"])
    return HttpResponseRedirect(reverse("about"))
    