from django.urls import include, path
from rest_framework import routers
from api.views import CategoryViewset,PostViewset

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewset)
router.register(r'posts', PostViewset)

urlpatterns = [
    path('',include(router.urls))
 
]
urlpatterns += router.urls

