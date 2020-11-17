from django.urls import path

import exampleapp.views

# admin.autodiscover()

urlpatterns = [
    # '',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    path('', exampleapp.views.index),
]
