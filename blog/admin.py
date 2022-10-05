from django.contrib import admin
from .models import BlogPost, BlogDetail, NftPost, NftDetail, NftImage

admin.site.register(BlogPost)
admin.site.register(BlogDetail)
admin.site.register(NftDetail)
admin.site.register(NftPost)
admin.site.register(NftImage)