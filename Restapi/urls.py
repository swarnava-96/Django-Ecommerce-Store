from django.urls import path
from django.conf.urls import url

from . api import UserList, UserDetail, profiles

urlpatterns = [
    
    url(r'^api/users_list/$', UserList.as_view(), name="user_list"),
    url(r'^api/users_list/(?P<employee_id>\d+)$', UserDetail.as_view(), name="user_list"),
    url(r'^api/profiles/$', profiles.as_view(), name="profiles"),
    

]