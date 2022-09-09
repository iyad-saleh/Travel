from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from users import views as user_views
from .views import dashboard
from django.views.generic import TemplateView

urlpatterns =[
    path('i18n/',include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    # path('jet/', include('jet.urls')),
    # path('jet/dashboard/', include('jet.dashboard.urls','jet-dashboard')),
    
    path('staff/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('htmx/', include('common.urlsHtmx')),
    path('', include('blog.urls')),
    path('dashboard/', dashboard, name='dashboard' ),
    path('account/', include('account.urls')),
    path('companys/', include('company.urls')),
    path('expenses/', include('expense.urls')),
    path('employee/', include('employee.urls')),
    path('reservation/', include('reservation.urls')),
    path('passport/', include('passport.urls')),
    path('trip/', include('trip.urls')),
    path('guest/', include('guest.urls')),
    path('admin/', include('adminlte.urls')),
    prefix_default_language=False,

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
