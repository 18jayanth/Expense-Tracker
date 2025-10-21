from django.contrib import admin
from tracker.models import *

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"



admin.site.register(CurrentBalance)

@admin.action(description="Mark selected Expenses as Credit")
def make_credit(modeladmin, request, queryset):
    for q in queryset:
        obj = TrackingHistory.objects.get(id = q.id)
        if obj.amount < 0:
            obj.amount = obj.amount * -1
            obj.save()
    queryset.update(expense_type="CREDIT")


admin.site.disable_action("delete_selected")

@admin.action(description="Make it in Debit")

def make_debit(modeladmin, request, queryset):
    for q in queryset:
        obj = TrackingHistory.objects.get(id = q.id)
        if obj.amount > 0:
            obj.amount = obj.amount * -1
            obj.save()

    queryset.update(expense_type = "DEBIT")
class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "amount",
        "current_balance",
        "expense_type",
        "description",
        "created_at",
        "display_age"
    ]

    actions = [make_credit , make_debit]

    def display_age(self , obj):
        if obj.amount > 0:
            return "Postive"
        return "Negative"
    


    search_fields = ['expense_type', 'description']
    list_filter = ['expense_type']
    ordering = ['-expense_type']



admin.site.register(TrackingHistory, TrackingHistoryAdmin)