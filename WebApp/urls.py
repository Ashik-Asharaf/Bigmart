from django.urls import path
from WebApp import views

urlpatterns=[
    path('home_pg',views.home_pg,name='home_pg'),
    path('about_pg/',views.about_pg,name='about_pg'),
    path('contact_pg/',views.contact_pg,name='contact_pg'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('product_pg/',views.product_pg,name='product_pg'),
    path('single/<int:pro_id>',views.single,name='single'),
    path('filter_cate/<cat>/',views.filter_cate,name='filter_cate'),
    path('reg_pg/',views.reg_pg,name='reg_pg'),
    path('save_reg/',views.save_reg,name='save_reg'),
    path('save_cart/',views.save_cart,name='save_cart'),

]