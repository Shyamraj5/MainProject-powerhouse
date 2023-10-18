from django.contrib import admin
from . models import *
# Register your models here.
class AdminResponseAdmin(admin.ModelAdmin):
    list_display = ('response', 'service')  # Add other fields you want to display in the admin list view

    actions = ['get_responses_for_user']

    def get_responses_for_user(self, request, queryset):
        # Get the user from the request
        user = request.user

        # Filter responses based on the user's service
        filtered_responses = queryset.filter(service__user=user)

        # Do something with the filtered responses, e.g., print or process them
        for response in filtered_responses:
            print(response.response)

    get_responses_for_user.short_description = "Get Responses for User"

admin.site.register(AdminResponse,AdminResponseAdmin)