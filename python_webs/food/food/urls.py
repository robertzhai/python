from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import current_datetime , hours_ahead

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'food.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^recipe/', include('recipe.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d+)/$', hours_ahead),
)
