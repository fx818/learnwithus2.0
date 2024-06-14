from django.contrib import admin
from .models import Registration,techblogs,OTP,verifiedEmail
# Register your models here.
admin.site.register(Registration)


# from chatgpt for custom user
# component/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'skill1', 'skill2', 'skill3', 'country', 'linkedin', 'activitypoint','profile_pic')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'gender', 'skill1', 'skill2', 'skill3', 'country', 'linkedin', 'activitypoint','profile_pic'),
        }),
    )

    # Display the new fields in the admin list view
    list_display = ('username', 'email','country', 'linkedin')
    list_filter = ('gender', 'country')

admin.site.register(CustomUser, CustomUserAdmin)


class techblogsAdmin(admin.ModelAdmin):
    list_display = ('username', 'title','description')

admin.site.register(techblogs,techblogsAdmin)



admin.site.register(OTP)
admin.site.register(verifiedEmail)