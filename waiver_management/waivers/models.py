from django.db import models
from django.contrib.auth.models import User

class WaiverType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ErrorCode(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Approver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    waiver_type = models.ManyToManyField(WaiverType)
    domain = models.ManyToManyField(Domain)

    def __str__(self):
        return self.user.username

class Waiver(models.Model):
    type = models.ForeignKey(WaiverType, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    error_code = models.ForeignKey(ErrorCode, on_delete=models.CASCADE)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type.name} Waiver for {self.error_code.code}"

class WaiverApproval(models.Model):
    waiver = models.ForeignKey(Waiver, on_delete=models.CASCADE)
    approver = models.ForeignKey(Approver, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Approval for {self.waiver}"

