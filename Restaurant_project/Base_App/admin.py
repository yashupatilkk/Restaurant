from django.contrib import admin
from .models import ItemList, BookTable, AboutUs, Items, Feedback  # Ensure Feedback is imported

# Prevent duplicate registration
if not admin.site.is_registered(ItemList):
    admin.site.register(ItemList)

if not admin.site.is_registered(BookTable):
    admin.site.register(BookTable)

if not admin.site.is_registered(AboutUs):
    admin.site.register(AboutUs)

if not admin.site.is_registered(Items):
    admin.site.register(Items)

if not admin.site.is_registered(Feedback):
    admin.site.register(Feedback)
