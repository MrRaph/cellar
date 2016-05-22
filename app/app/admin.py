from functools import update_wrapper

from django.contrib import admin
from django.contrib.admin.apps import AdminConfig


class WineAdminSite(admin.AdminSite):
    def get_urls(self):
        """
        Most of this is copy/pasted from AdminSite's get_urls method. I needed
        to skip over registering some of the URLs so I could move the "wine"
        models to the top level URL. That is:

            * Wine is at `/`
            * Winery is at `/winery`

        Any subsequent models registered in the wine app will have the raised
        URL level.
        """

        from django.conf.urls import url, include
        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level,
        # and django.contrib.contenttypes.views imports ContentType.
        from django.contrib.contenttypes import views as contenttype_views

        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            wrapper.admin_site = self
            return update_wrapper(wrapper, view)

        # Admin-site-wide views.
        urlpatterns = [
            url(r'^list/$', wrap(self.index), name='index'),
            url(r'^login/$', self.login, name='login'),
            url(r'^logout/$', wrap(self.logout), name='logout'),
            url(r'^password_change/$', wrap(self.password_change, cacheable=True), name='password_change'),
            url(r'^password_change/done/$', wrap(self.password_change_done, cacheable=True),
                name='password_change_done'),
            url(r'^jsi18n/$', wrap(self.i18n_javascript, cacheable=True), name='jsi18n'),
            url(r'^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$', wrap(contenttype_views.shortcut),
                name='view_on_site'),
        ]

        # Add in each model's views, and create a list of valid URLS for the
        # app_index
        valid_app_labels = []
        for model, model_admin in self._registry.items():
            # Skip over wine for now, we want to register it on the bottom of
            # the URL patterns.
            if model._meta.app_label == "wine":
                if model._meta.app_label not in valid_app_labels:
                    valid_app_labels.append(model._meta.app_label)
                continue

            urlpatterns += [
                url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]
            if model._meta.app_label not in valid_app_labels:
                valid_app_labels.append(model._meta.app_label)

        # If there were ModelAdmins registered, we should have a list of app
        # labels for which we need to allow access to the app_index view,
        if valid_app_labels:
            regex = r'^(?P<app_label>' + '|'.join(valid_app_labels) + ')/$'
            urlpatterns += [
                url(regex, wrap(self.app_index), name='app_list'),
            ]

        # Patch the wine models in.
        for model, model_admin in self._registry.items():
            if model._meta.app_label != "wine":
                continue

            urlre = r'^%s/' % model._meta.model_name

            # Wines get top billing!
            if model._meta.model_name == "wine":
                urlre = r'^'

            urlpatterns += [
                url(urlre, include(model_admin.urls)),
            ]

        return urlpatterns


class WineAdminAppConfig(AdminConfig):
    def ready(self):
        from django.contrib import admin
        from django.contrib.admin import sites

        custom_site = WineAdminSite()
        admin.site = custom_site
        sites.site = custom_site

        super(WineAdminAppConfig, self).ready()
