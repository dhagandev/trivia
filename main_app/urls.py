from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('accounts/signup', views.signup, name='signup'),

    path('users', views.user_ranking, name='user_ranking'),
    path('users/<int:user_id>', views.user_profile, name='user_profile'),
    
    path('question', views.question, name='question'),
    path('question/<int:question_id>', views.question_display, name='question_display'),
    path('question/<int:question_id>/answer/<str:player_choice>', views.answer, name='answer'),

    path('accounts/signup', views.signup, name='signup'),
 ]