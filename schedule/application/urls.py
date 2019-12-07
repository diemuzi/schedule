from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.sitemaps import views
from django.urls import include
from django.urls import path

# from django.views.generic import TemplateView
# from login.sitemaps import LoginStaticSitemap

# Sitemaps
sitemaps = {
    #    'login-static': LoginStaticSitemap
}

# URL Patterns
urlpatterns = [
    # robots.txt
    # path('robots.txt', TemplateView.as_view(template_name='random/robots.txt')),

    # sitemap.xml
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}, name='sitemap'),

    # sitemap-<section>-static.xml (for example - sitemap-login-static.xml)
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

# Static Content
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# i18n URL Patterns
urlpatterns += i18n_patterns(
    # Schedule URLs
    path('', include('roster.urls')),
    path('login/', include('login.urls')),

    # Django Registration / Password URLs
    path('', include('django.contrib.auth.urls'))
)

# Error Pages
# handler400 = Error400.as_view()
# handler403 = Error403.as_view()
# handler404 = Error404.as_view()
# handler500 = Error500.as_view()

# Debug Settings
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
