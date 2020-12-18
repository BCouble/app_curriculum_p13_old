from django.urls import path
from curry.apps.zvitae.views import ZvitaeCreate, ZvitaeDelete, ZvitaeUpdate, ZvitaeView, ZvitaeDisplay, CstateCreate, \
    CstateDisplay, CstateUpdate, CstateDelete, AddressCreate, AddressUpdate, AddressDelete

app_name = 'zvitae'

urlpatterns = [
    path('zview/', ZvitaeView.as_view(), name='zview'),
    path('zv-add/', ZvitaeCreate.as_view(), name='zvitae-add'),
    path('zv-detail/', ZvitaeDisplay.as_view(), name='zvitae-detail'),
    path('zv-up/<int:pk>/', ZvitaeUpdate.as_view(), name='zvitae-update'),
    path('<int:pk>/zv-delete/', ZvitaeDelete.as_view(), name='zvitae-delete'),
    path('cs-add/', CstateCreate.as_view(), name='cstate-add'),
    path('cs-detail/', CstateDisplay.as_view(), name='cstate-detail'),
    path('cs-up/<int:pk>/', CstateUpdate.as_view(), name='cstate-up'),
    path('<int:pk>/cs-delete/', CstateDelete.as_view(), name='cstate-delete'),
    path('address-add/', AddressCreate.as_view(), name='address-add'),
    path('address-up/<int:pk>/', AddressUpdate.as_view(), name='address-up'),
    path('<int:pk>/add-delete/', AddressDelete.as_view(), name='address-delete'),
]
