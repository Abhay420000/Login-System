from django.urls import path
from .views import Login, SignUp, Welcome
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Welcome.as_view()), name='home_page'),
    path('login/', Login.as_view(), name='log_in'),
    path('sign_up/', SignUp.as_view(), name='sign_up'),
]
