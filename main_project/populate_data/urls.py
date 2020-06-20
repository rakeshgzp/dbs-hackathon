from django.conf.urls import url,include
from django.urls import path
from populate_data import views
from .views import retrieve_id,update_id,customer_item,update_customer_ivalue,show_score

app_name = 'populate_data'
urlpatterns = [
path('uid/<str:uid>/',retrieve_id.as_view(),name="uid"),
path('update_uid',update_id.as_view(),name="Update_uid"),
path('view_customer_values/<str:uid>/',customer_item.as_view(),name="customer_item"),
# path('update_customer_ivalue',update_customer_ivalue.as_view(),name="update_customer_value"),
path('show_score/<str:uid>/',show_score.as_view(),name="show_score"),

]