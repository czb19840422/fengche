from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def index(request):
    username = request.user
    return render_to_response('index.html',{'username':username})

