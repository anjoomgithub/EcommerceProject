from django.urls import path, include
from . import views
app_name='ecommerce'
urlpatterns = [
    path('',views.allprodCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allprodCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]