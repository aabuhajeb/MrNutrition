from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('nutritionist/', views.nutritionist, name='nutritionist'),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),

    path('account/', views.accountSettings, name='account'),

    path('product-list/', views.productsList, name='productlist'),
    path('product-detail/<str:pk>/', views.productsDetail, name='productdetail'),
    path('product-create/', views.productsCreate, name='productcreate'),
    path('product-update/<str:pk>/', views.productsUpdate, name='productupdate'),
    path('product-delete/<str:pk>/', views.productsDelete, name='productdelete'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(
            template_name="store/password_reset.html"),
        name="reset_password"), #submit email form

    path('reset_password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="store/password_reset_sent.html"),
        name="password_reset_done"), #Email sent success message

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="store/password_reset_form.html"),
        name="password_reset_cofirm"), #Link to password Reset form in email

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="store/password_reset_done.html"),
        name="password_reset_complete"), #Password successfully changed message
]