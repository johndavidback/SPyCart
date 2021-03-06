from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^SPyCart/', include('SPyCart.foo.urls')),
    
    (r'^$', 'SPyCart.cart.views.index'),
    (r'^catalog/$', 'SPyCart.cart.views.catalog'),
    (r'^product/(?P<product_id>\d+)/$', 'SPyCart.cart.views.product'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
