from django.contrib import admin
from blog.models import submitform
from blog.models import contactmdl
from blog.models import topposts
admin.site.register(topposts)
admin.site.register(contactmdl)

admin.site.register(submitform)
# Register your models here.
