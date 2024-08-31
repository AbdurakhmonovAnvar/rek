from django.urls import path
from .views import AdverGetView, AdverCreateView, AdverUpdateView, AdverDeleteView

urlpatterns = [
    path('adver/', AdverGetView.as_view(), name='adver-get'),
    path('adver_post/', AdverCreateView.as_view(), name='adver-create'),
    path('adver/', AdverGetView.as_view(), name='adver-get'),
    path('adver_update/<int:pk>/', AdverUpdateView.as_view(), name='adver-update'),
    path('adver_delete/<int:pk>/', AdverDeleteView.as_view(), name='adver-delete'),
]
