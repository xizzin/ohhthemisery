from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from hello.views import index
from hello.views import *

app_name = 'hello'
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index),
    path('categories.html', categories),
    path('profile.html', profile),
    path('shopcart.html', shopcart),
    path('allproducts_page.html', productpage),
    path('aboutus.html', aboutus),
    path('allproducts_base.html', allprojects),
    path('result', result, name='result'),
    path('api/', include('api_shop.urls')),
    path('login/', login_user, name='login_page'),
    path('registration/', registration_user, name='registration_page'),
    path('logout/', logout_user, name='logout_page')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
