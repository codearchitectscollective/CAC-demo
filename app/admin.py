from django.contrib import admin
from .models import Post
from .models import News
from .models import Featured
from .models import Trending


admin.site.register(Post)
admin.site.register(News)
admin.site.register(Featured)
admin.site.register(Trending)

