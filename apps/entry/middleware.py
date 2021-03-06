from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.entry.models import TeamMember

from apps.entry.urls import urlpatterns
from apps import config


class ValidateUser:
    def __init__(self, get_response):
        # One-time configuration and initialization.
        config.update_permissions()
        self.permissions = config.permissions
        self.update_permissions()
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        if str(request.path).__contains__('media') or str(request.path).__contains__('static') or str(request.path).__contains__('admin'):
            return response

        try:
            if str(request.path) == "/":
                return HttpResponseRedirect(reverse_lazy('entry:index'))
        except IndexError:
            print("INDEX ERROR")
            return response
        try:
            view = str(request.path).split('/')[2]
            app = str(request.path).split('/')[1]
        except IndexError:
            print("\nINDEX ERROR FROM PATH SPLITTING IN MIDDLEWARE:")
            print(request.path)
            print("\n")
            return HttpResponseRedirect(reverse_lazy('entry:index'))

        if view == "logout" or view == "login" or app == "media":
            return response

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('entry:login'))

        if request.user.teammember.position == "NA":
            return HttpResponseRedirect(reverse_lazy('entry:logout'))

        if view == 'entry':
            if self.valid_perms(view, request.user):
                return response
            else:
                return HttpResponseRedirect(reverse_lazy('entry:index'))

        return response

    def update_permissions(self):
        self.permissions = {}

        for each in config.permissions:
            self.permissions[each] = config.permissions[each]['minimum']

    def valid_perms(self, view, user):
        if view == '':
            view = 'index'

        reqlevel = 0
        for each in TeamMember.AVAILABLE_POSITIONS:
            if each[0] == self.permissions[view]:
                break
            else:
                reqlevel += 1

        actlevel = 0
        for each in TeamMember.AVAILABLE_POSITIONS:
            if each[0] == user.teammember.position:
                break
            else:
                actlevel += 1

        return actlevel >= reqlevel
