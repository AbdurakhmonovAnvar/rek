from django.urls import path
from .views import AdverGetView, AdverCreateView, AdverUpdateView, AdverDeleteView, StreetView, RegionView, \
    AdverTypeView, AdverGetFilter, RandomAdver
from . import views

urlpatterns = [
    path('api/v1/adver/', AdverGetView.as_view(), name='adver-get'),  # elonlarni list qilib yuboradi get
    path('api/v1/random_adver/', RandomAdver.as_view(), name='adver-random'),  # elonlarni random get
    path('api/v1/adver_post/', AdverCreateView.as_view(), name='adver-create'),  # elonlarni post qilsa bo'ladi
    # path('adver/', AdverGetView.as_view(), name='adver-get'),
    path('api/v1/adver_update/<int:pk>/', AdverUpdateView.as_view(), name='adver-update'),  # userni postini o'zgartiradi put
    path('api/v1/adver_delete/<int:pk>/', AdverDeleteView.as_view(), name='adver-delete'),  # delete qiladi delete
    path('api/v1/get_street/<int:pk>/', StreetView.as_view(), name='get-street'), # shaharlarni olish list qilib qaytaradi get
    path('api/v1/get_region/', RegionView.as_view(), name='get-region'), # viloyatlarni olish list qilib qaytaradi get
    path('api/v1/adver_type/', AdverTypeView.as_view(), name='get-adver-type'), # Elonni turi get
    path('api/v1/filter/', AdverGetFilter.as_view(), name='get-adver-filter'), # filter bilan get qiladi
    # path('home/', views.home, name='home'),
]
