from django.urls import path
from order import views

app_name='order'

urlpatterns=[

	path('',views.index,name='index'),
	path('order',views.NewOrder.as_view(),name="order"),
	path('search/',views.search,name="search"),
	path('order/<int:pk>',views.OrderDetail.as_view(),name="order-detail"),
	path('order/<int:pk>/update',views.OrderUpdate.as_view(),name="order-update"),
	path('order/<int:pk>/delete',views.OrderDelete.as_view(),name="order-delete"),
	path('order/<int:pk>/approve',views.order_approve,name="order-approve"),
	path('order/<int:pk>/reject',views.order_reject,name="order-reject"),
	path('orders-download',views.orders_download,name="orders-download"),
	path('approved-download',views.approved_download,name="approved-download"),
	path('rejected-download',views.rejected_download,name="rejected-download"),	
	path('user/<int:pk>/orders',views.all_order_per_user,name="order_per_user"),
	path('add-supplier',views.NewSupplier.as_view(),name="supplier-add"),
		
	]