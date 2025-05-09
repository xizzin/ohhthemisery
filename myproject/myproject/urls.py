from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from hello.views import index
from hello.views import categories
from hello.views import profile
from hello.views import shopcart
from hello.views import productpage
from hello.views import aboutus
from hello.views import allprojects
from hello.views import result

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
    path('result', result, name='result')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
