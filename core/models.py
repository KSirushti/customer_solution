from django.db import models

class UseCase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class TargetSchema(models.Model):
    use_case = models.ForeignKey(UseCase, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50)

class SourceCatalog(models.Model):
    source_system = models.CharField(max_length=100)
    source_field = models.CharField(max_length=100)
    description = models.TextField()

class FieldMapping(models.Model):
    target_field = models.CharField(max_length=100)
    source_field = models.CharField(max_length=100)
    source_system = models.CharField(max_length=100)
    transformation = models.CharField(max_length=255)

class Certification(models.Model):
    use_case = models.ForeignKey(UseCase, on_delete=models.CASCADE)
    certified = models.BooleanField(default=False)
    issues = models.TextField(blank=True)
