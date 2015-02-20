from django.contrib import admin
from visualwords.models import VisualWord

import reversion

class VisualWordAdmin(reversion.VersionAdmin):
    list_display = ('word', 'uploaded_by', 'uploaded_on', 'approved', 'nsfw', 'admin_thumbnail')
    
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"
    list_filter = ('approved', 'nsfw', 'uploaded_by__username',)
    
    list_editable = ('approved', 'nsfw',)
    
    def admin_thumbnail(self, obj):
        if obj.url_thumb:
            return u'<img src="%s" class="thumb"/>' % (obj.url_thumb)
        elif obj.url_img:
            return u'<img src="%s" class="thumb"/>' % (obj.url_img)
        else:
            return ""
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
    class Media:  
        css = {
             'all': ('css/admin/thumbnails.css',)
        }

admin.site.register(VisualWord, VisualWordAdmin)
