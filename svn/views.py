from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def svn_user(request):
    username = request.user
    return render_to_response('svnuser.html', {'username':username})


@login_required(login_url="/login/")
def svn_perm(request):
    username = request.user
    return render_to_response('svnperm.html', {'username':username})

@login_required(login_url="/login/")
def svn_server(request):
    username = request.user
    return render_to_response('svnserver.html', {'username':username})

@login_required(login_url="/login/")
def svn_backup(request):
    username = request.user
    return render_to_response('svnbackup.html', {'username':username})

@login_required(login_url="/login/")
def svn_fwq(request):
    username = request.user
    return render_to_response('svnfwq.html', {'username':username})