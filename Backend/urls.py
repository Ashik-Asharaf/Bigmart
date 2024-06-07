from django.urls import path
from Backend import views



urlpatterns=[
    path('index_pg/',views.index_pg,name='index_pg'),
    path('category_pg/',views.category_pg,name='category_pg'),
    path('display_cate/',views.display_cate,name='display_cate'),
    path('save_category/',views.save_category,name='save_category'),
    path('edit_cate/<int:cate_id>/',views.edit_cate,name='edit_cate'),
    path('update_category/<int:cate_id>/',views.update_category,name='update_category'),
    path('delete_cate/<int:cate_id>/',views.delete_cate,name='delete_cate'),
    path('login/',views.login,name='login'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('product_pg/',views.product_pg,name='product_pg'),
    path('display_product/',views.display_product,name='display_product'),
    path('save_product/',views.save_product,name='save_product'),
    path('edit_product/<int:pro_id>/',views.edit_product,name='edit_product'),
    path('update_product/<int:pro_id>/',views.update_product,name='update_product'),
    path('delete_product/<int:pro_id>/',views.delete_product,name='delete_product'),
    path('contact_data/', views.contact_data, name='contact_data'),
    path('delete_cont/<int:cont_id>/', views.delete_cont, name='delete_cont'),

]