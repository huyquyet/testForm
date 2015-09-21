from django.conf.urls import include, url
from form1 import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^test/', include('form1.test.urls'))

]
