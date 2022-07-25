from django.contrib import admin
from .models import Banner, Event, Model_All, NavLink , Point


class NavlinkAdmin(admin.TabularInline):
    model = NavLink

class EventAdmin(admin.ModelAdmin):
   inlines = [NavlinkAdmin,]

admin.site.register(Event , EventAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display =  ('title' , 'banner_preview' , 'height' , 'width')
    readonly_fields = ('banner_preview',)

    def banner_preview(self, obj):
        return obj.banner_preview

    banner_preview.short_description = 'Banner Preview'
    banner_preview.allow_tags = True

admin.site.register(Banner, BannerAdmin)



class PointAdmin(admin.TabularInline):
    model = Point

class ModelAdmin(admin.ModelAdmin):
   inlines = [PointAdmin,]

admin.site.register(Model_All,ModelAdmin)