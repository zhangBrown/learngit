from django.contrib import admin
from apitest.models import Apitest, Apistep, Apis


# Register your models here.
class ApistepAdmin(admin.TabularInline):
    list_display = [
        "api_name", "api_url", "api_param", "api_method", "api_except_result",
        "api_status", "create_time", "id", "apitest"
    ]
    model = Apistep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = [
        "apitest_name", "apitester", "apitest_result", "create_time", "id"
    ]
    inlines = [ApistepAdmin]


admin.site.register(Apitest, ApitestAdmin)


class ApisAdmin(admin.ModelAdmin):
    list_display = ["api_name", "api_url", "api_param", "api_method", "api_except", "api_status",
                    "create_time", "id", "product",
    ]


admin.site.register(Apis)