from django.urls import path
from .views import AdverGetView, AdverCreateView, AdverUpdateView, AdverDeleteView, StreetView, RegionView, \
    AdverTypeView

urlpatterns = [
    path('adver/', AdverGetView.as_view(), name='adver-get'),
    path('adver_post/', AdverCreateView.as_view(), name='adver-create'),
    path('adver/', AdverGetView.as_view(), name='adver-get'),
    path('adver_update/<int:pk>/', AdverUpdateView.as_view(), name='adver-update'),
    path('adver_delete/<int:pk>/', AdverDeleteView.as_view(), name='adver-delete'),
    path('get_street/<int:pk>/', StreetView.as_view(), name='get-street'),
    path('get_region/', RegionView.as_view(), name='get-region'),
    path('adver_type/', AdverTypeView.as_view(), name='get-adver-type'),
    path('adver_type/', AdverTypeView.as_view(), name='get-adver-type'),
]
