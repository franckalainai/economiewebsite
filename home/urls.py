from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('organigramme-meps', views.orga, name='orga'),
    path('strures-sous-tutelles', views.sousTutelles, name='structures-sous-tutelles'),
    path('ecoles-specialisees', views.ecolesSpeciales, name='ecoles-speciales'),
    path('decret-organisation', views.decretOrga, name='decret-organisation'),

    path('get-faq', views.get_faq, name="get-faq"),
    path('equipe-cabinet', views.equipe, name="equipe"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)