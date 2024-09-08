from django.urls import path
from .views import AdverGetView, AdverCreateView, AdverUpdateView, AdverDeleteView, StreetView, RegionView, \
    AdverTypeView, AdverGetFilter
from . import views

urlpatterns = [
    path('adver/', AdverGetView.as_view(), name='adver-get'),  # elonlarni list qilib yuboradi
    path('adver_post/', AdverCreateView.as_view(), name='adver-create'),  # elonlarni post qilsa bo'ladi
    # path('adver/', AdverGetView.as_view(), name='adver-get'),
    path('adver_update/<int:pk>/', AdverUpdateView.as_view(), name='adver-update'),  # userni postini o'zgartiradi
    path('adver_delete/<int:pk>/', AdverDeleteView.as_view(), name='adver-delete'),  # delete qiladi
    path('get_street/<int:pk>/', StreetView.as_view(), name='get-street'),
    path('get_region/', RegionView.as_view(), name='get-region'),
    path('adver_type/', AdverTypeView.as_view(), name='get-adver-type'),
    path('filter/', AdverGetFilter.as_view(), name='get-adver-filter'),
    path('home/', views.home, name='home'),
]
