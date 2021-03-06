from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
]
