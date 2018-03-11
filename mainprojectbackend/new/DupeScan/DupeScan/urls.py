from django.conf.urls import include,url
from django.conf import settings
from django.contrib import admin
from feedback import views as webview
from signin import views as signinview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^home/',include('feedback.urls')),
    url(r'^',include('feedback.urls')),
    url(r'^signin/',include('signin.urls')),
    url(r'^signup/',include('signup.urls')),
    # url(r'^testmail/', webview.testmail),
    #url(r'^getuser/(?P<id>[0-9]+)/',signinview.detailView),
    #url(r'^activities/',signinview.activity)
    #url(r'^index.html/',include("webapp.urls")),
]