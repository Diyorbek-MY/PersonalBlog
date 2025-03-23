from django.contrib import admin
from django.urls import path, include
from main import views  # ✅ Import views from 'main' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # ✅ Homepage
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('new/', views.create_post, name='create_post'),
    
    # ✅ Authentication Routes
    path('accounts/', include('django.contrib.auth.urls')),  # Django built-in auth
    path('signup/', views.signup, name='signup'),  # Signup Page
]
