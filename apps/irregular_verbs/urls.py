from django.urls import path

from .views import IrregularVerbList, IrregularVerbDetail

urlpatterns = [
    path('list/', IrregularVerbList.as_view(), name='irregular-verb-list'),
    path('<int:pk>/', IrregularVerbDetail.as_view())
]