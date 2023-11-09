from django.urls import path, include
from django.contrib import admin
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from backend.cooke import set_cookie, show_cookie
from backend.views import PartnerUpdate, RegisterAccount, LoginAccount, ProductInfoView, ShopView, CategoryView, \
    BasketView, ContactView, OrderView, PartnerOrders, ContactViewSet, TaskViewGet

app_name = 'backend'
urlpatterns = [
    path('task/<task_id>', TaskViewGet.as_view()),
path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    # path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    # path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    # path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/contactsviewset/<int:pk>',
         ContactViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('user/contactsviewset',
         ContactViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('setcookie', set_cookie),
    path('getcookie', show_cookie),
    # path('user/password_reset', reset_password_request_token, name='password-reset'),
    # path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
    path('admin/', admin.site.urls),
]
