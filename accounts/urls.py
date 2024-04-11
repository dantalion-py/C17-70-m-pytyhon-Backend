from rest_framework import routers
from django.urls import path, include
from accounts import views
from rest_framework.documentation import include_docs_urls

administrator_router = routers.DefaultRouter()
doctor_router = routers.DefaultRouter()
patient_router = routers.DefaultRouter()
user_router = routers.DefaultRouter()

administrator_router.register(r'administrators', views.AdministratorView)
doctor_router.register(r'doctors', views.DoctorView)
patient_router.register(r'patients', views.PatientView)
user_router.register(r'users', views.UserView)

urlpatterns = [

    # API
    path('api/administator/',include(administrator_router.urls)),
    path('api/doctor/',include(doctor_router.urls)),
    path('api/patient/',include(patient_router.urls)),
    path('api/user/',include(user_router.urls)),

    # documentation
    path('doc/', include_docs_urls(title=f"API doc")),

    # views
    path('api/hello/', views.home, name="hello"),


]
