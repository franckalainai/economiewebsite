from django.urls import path
from . import views

urlpatterns = [
    path('reseauxsoins/', views.reseaux, name='reseauxsoins'),
    path('medicamentscmu/', views.medicaments, name='medicamentscmu'),
    path('centrecmu/', views.centrecmu, name='centrecmu'),

    path('mission/', views.mission, name='mission'),
    path('edit-mission/<int:pk>', views.editMission, name='editmission'),
    path('delete-mission/<int:pk>', views.deleteMission, name='deletemission'),
    path('detail-mission/<str:slug>', views.detailMission, name="detail-mission"),

    # cabinet
    path('cabinet/', views.cabinet, name='cabinet'),
    path('edit-cabinet/<int:pk>', views.editCabinet, name='editcabinet'),
    path('delete-mission/<int:pk>', views.deleteCabinet, name='deletecabinet'),
    path('detail-cabinet/<str:slug>', views.detailCabinet, name="detail-cabinet"),

    # orgaigramme
    path('organigramme/', views.organigramme, name='organigramme'),
    path('edit-organigramme/<int:pk>', views.editOrganigramme, name='editorganigramme'),
    path('delete-organigramme/<int:pk>', views.deleteOrganigramme, name='deleteorganigramme'),
    path('detail-organigramme/<str:slug>', views.detailOrganigramme, name="detail-organigramme"),

    # tutel
    path('tutel/', views.tutel, name='tutel'),
    path('edit-tutel/<int:pk>', views.editTutel, name='edittutel'),
    path('delete-tutel/<int:pk>', views.deleteTutel, name='deletetutel'),
    path('detail-tutel/<str:slug>', views.detailTutel, name="detail-tutel"),

    # ecole
    path('ecole/', views.ecole, name='ecole'),
    path('edit-ecole/<int:pk>', views.editEcole, name='editecole'),
    path('delete-ecole/<int:pk>', views.deleteEcole, name='deleteecole'),
    path('detail-ecole/<str:slug>', views.detailEcole, name="detail-ecole"),


     # organisation
    path('organisation/', views.organisation, name='organisation'),
    path('edit-organisation/<int:pk>', views.editOrganisation, name='editorganisation'),
    path('delete-organisation/<int:pk>', views.deleteOrganisation, name='deleteOrganisation'),
    path('detail-organisation/<str:slug>', views.detailOrganisation, name="detail-organisation"),

    # biographie
    path('biographie/', views.biographie, name='biographie'),
    path('edit-biographie/<int:pk>', views.editBiographie, name='editbiographie'),
    path('delete-biographie/<int:pk>', views.deleteBiographie, name='deletebiographie'),
    path('detail-biographie/<str:slug>', views.detailBiographie, name="detail-biographie"),
    
    # produit

    
    path('produit/', views.produit, name='produit'),
    path('edit-produit/<int:pk>', views.editProduit, name='editproduit'),
    path('delete-produit/<int:pk>', views.deleteProduit, name='deleteproduit'),
    path('detail-produit/<str:slug>', views.detailProduit, name="detail-produit"),
    
]