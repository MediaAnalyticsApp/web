import authapp.views as authapp
from django.urls import path, re_path
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,\
#     password_reset_complete, password_change_done
# from django.conf.urls import url


urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('change/', authapp.change_password, name='change'),
    path('password-reset/', authapp.password_reset, name='password_reset'),
    path('password-reset/done/', authapp.password_reset_done, name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', authapp.password_reset_confirm,
            name='password_reset_confirm'),
    path('password-reset/complete/', authapp.password_reset_complete, name='password_reset_complete'),
]
