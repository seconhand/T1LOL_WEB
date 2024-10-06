from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#회원가입, 로그인, 로그아웃, 비밀번호 재설정 URL 설정
urlpatterns  = [
    path('signup/', views.signup, name='signup'),  # 괄호를 없앰
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]