from django.conf.urls import url
from svn import views

urlpatterns = [
    url(r'^user/$',views.svn_user),
    url(r'^perm/$',views.svn_perm),
    url(r'^server/$',views.svn_server),
    url(r'^backup/$',views.svn_backup),
    url(r'^fwq/$',views.svn_fwq),
]
