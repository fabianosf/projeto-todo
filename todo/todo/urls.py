from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')), # url principal da pagina
    path('accounts/', include('accounts.urls')), # pagina de registro .. o django lê isso depois o outro
    path('accounts/', include('django.contrib.auth.urls')), # login logout do django
    
   
]
