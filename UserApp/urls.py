from django.urls import path
from .views import HammaFoydalanuvchilar,BittaOdam
urlpatterns = [
    path('all_user/',HammaFoydalanuvchilar.as_view()),
    path('one/',BittaOdam.as_view())

]


#vmfeiuvnefiu