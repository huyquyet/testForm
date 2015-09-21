from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CreateFormView.as_view(), name="create_form"),
    # url(r'^test/', include('form1.test.urls'))
    url(r'^detail/$', views.DetailView.as_view(), name="detail_form"),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.EditView.as_view(), name="edit_form"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeleteView.as_view(), name="delete_form"),
]
