from django.urls import path
from .views import AllHistory

urlpatterns = [
    path('hammatolov/', AllHistory.as_view())

]
#vfnuevbie