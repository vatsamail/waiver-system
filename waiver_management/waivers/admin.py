from django.contrib import admin
from .models import WaiverType, Project, Domain, Module, ErrorCode, Waiver, Approver, WaiverApproval

admin.site.register(WaiverType)
admin.site.register(Project)
admin.site.register(Domain)
admin.site.register(Module)
admin.site.register(ErrorCode)
admin.site.register(Waiver)
admin.site.register(Approver)
admin.site.register(WaiverApproval)