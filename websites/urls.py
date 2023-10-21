from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "websites"
router = DefaultRouter()
router.register(r'dinner_options', views.DinnerOptionViewSet)
urlpatterns = [
    path("", views.index, name="index"),
    path("healthcheck/", views.healthcheck, name="healthcheck"),
    path("thanks/", views.thanks, name="thanks"),
    path('api/', include(router.urls)),
    path('dinner_options/', views.dinner, name='dinner'),
    path('dinner_results/', views.dinner_results, name='dinner_results')
]
