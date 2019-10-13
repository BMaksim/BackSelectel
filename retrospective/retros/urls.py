from django.urls import path
from retros import views

urlpatterns = [
    path('user/<str:pk>/<str:pas>', views.UsersDetail.as_view()),
    path('session/<str:pk>', views.SessionKey.as_view()),
    path('sessions/<str:pk>', views.SessionALl.as_view())
]
