from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1
    show_change_link = True


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "menu", "parent", "url", "named_url")
    list_filter = ("menu",)
    search_fields = ("title", "url", "named_url")
