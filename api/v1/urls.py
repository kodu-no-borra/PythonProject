from django.urls import path, include

urlpatterns = [
    path('app1/', include('api.v1.app1.urls')),  # ручки app1
    path('app2/', include('api.v1.app2.urls')),  # ручки app2
]