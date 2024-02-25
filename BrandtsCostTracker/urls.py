from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # URL for uploading an invoice
    path('upload/', views.upload_invoice, name='upload_invoice'),
    
    # URL to view a list of all items
    path('items/', views.view_items, name='view_items'),
    
    # URL to view a single item's price history
    path('items/<int:item_id>/', views.view_item_detail, name='view_item_detail'),
    
    # URL to view an invoice image
    path('invoice/<int:invoice_id>/', views.view_invoice_image, name='view_invoice_image'),
    
    # URL for the homepage or dashboard
    path('', views.index, name='index'),
    
    # Add other URLs as needed for additional functionality
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



