from django.urls import path
from .views import AdverGetView, AdverCreateView, AdverUpdateView, AdverDeleteView, StreetView, RegionView, \
    AdverTypeView, AdverGetFilter, RandomAdver
from . import views

urlpatterns = [
    path('api/v1/adver/', AdverGetView.as_view(), name='adver-get'),  # elonlarni list qilib yuboradi
    path('api/v1/random_adver/', RandomAdver.as_view(), name='adver-random'),  # elonlarni list qilib yuboradi
    path('api/v1/adver_post/', AdverCreateView.as_view(), name='adver-create'),  # elonlarni post qilsa bo'ladi
    # path('adver/', AdverGetView.as_view(), name='adver-get'),
    path('api/v1/adver_update/<int:pk>/', AdverUpdateView.as_view(), name='adver-update'),  # userni postini o'zgartiradi
    path('api/v1/adver_delete/<int:pk>/', AdverDeleteView.as_view(), name='adver-delete'),  # delete qiladi
    path('api/v1/get_street/<int:pk>/', StreetView.as_view(), name='get-street'),
    path('api/v1/get_region/', RegionView.as_view(), name='get-region'),
    path('api/v1/adver_type/', AdverTypeView.as_view(), name='get-adver-type'),
    path('api/v1/filter/', AdverGetFilter.as_view(), name='get-adver-filter'),
    path('home/', views.home, name='home'),
]
