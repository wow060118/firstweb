from django.conf.urls import url
from . import views
# 添加namespace 再url 拼接时通过namespace 访问
app_name = 'study'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<s_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<s_name>[a-zA-Z]+)/results/$', views.results, name='results'),
    url(r'^(?P<t_no>[0-9]+)/vote/$', views.vote, name='vote')
]
