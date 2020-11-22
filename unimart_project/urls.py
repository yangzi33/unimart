from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from market import views as market_views

# Debug mode
from django.conf import settings
from django.conf.urls.static import static

# REST API
from rest_framework import routers

# Configuring routers
router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'users', user_views.GroupViewSet)


urlpatterns = [
    path('', include('market.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


# debug mode
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
