from django.db import models

# Create your models here.
class ApplicationStage(models.Model):
    stage_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)

class RubricItem(models.Model):
    rubric_item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)

class ApplicationStageTemplate(models.Model):
    stage_template_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    object = models.JSONField()

class ApplicationRubricTemplate(models.Model):
    rubric_template_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    object = models.JSONField()

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=255, null=False, blank=False)

class Position(models.Model):
    position_id = models.IntegerField(primary_key=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    position_name = models.CharField(max_length=255, null=False, blank=False)

class ApplicationForm(models.Model):
    form_id = models.IntegerField(primary_key=True)
    form_object = models.JSONField()

class JobOpening(models.Model):
    job_opening = models.IntegerField(primary_key=True)
    stage_template = models.ForeignKey('ApplicationStageTemplate', on_delete=models.CASCADE)
    rubric_template = models.ForeignKey('ApplicationRubricTemplate', on_delete=models.CASCADE)
    form = models.ForeignKey('ApplicationForm',on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    employee_panel = models.JSONField()