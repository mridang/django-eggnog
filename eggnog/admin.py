from django.contrib import admin

from eggnog.models import *

class UpdateAdmin(admin.ModelAdmin):
    """
    Administration interface for the package updates.
    """
    list_display = ('cheeseshop', 'updateable', 'installed', 'available', 'checked')
    ordering = ['-checked']
    list_per_page = 100
    search_fields = ['package']
    readonly_fields = ['package', 'installed', 'available', 'checked']
    exclude = None
    max_num = 0

    def has_add_permission(self, request, obj=None):
        """
        Disable adding.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Disable deleting.
        """
        return False

    def get_actions(self, request):
        """
        Removes all the bulk actions as there are none.
        """
        return []

admin.site.register(Update, UpdateAdmin)
