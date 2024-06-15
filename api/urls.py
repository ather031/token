from django.urls import path
from api import views

urlpatterns = [
    path('login',                                               views.LoginView.as_view()),
    path('logout',                                              views.LogoutView.as_view()),
    path('refresh',                                             views.RefreshView.as_view()),
    path('current',                                             views.CurrentUserView.as_view()),
    path('changepassword',                                      views.UserChangePasswordView.as_view()),
    path('role',                                                views.RoleListView.as_view()),
    path('role/<int:pk>/',                                      views.RoleDetailView.as_view()),
    path('permission',                                          views.PermissionListView.as_view()),
    path('user',                                                views.UserListView.as_view()),
    path('user/<int:pk>/',                                      views.UserDetailView.as_view()),
]
