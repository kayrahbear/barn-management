from django.contrib import admin
from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Trainer)
admin.site.register(Horse)
admin.site.register(Lesson)
admin.site.register(Turnout)
admin.site.register(SuppsMeds)
admin.site.register(Feed)
