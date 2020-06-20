from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from users.models import Profile

Choices  = (
    (1,'All Available'),
    (2,'Least Busy'),
    (3,'Random')
)

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField(default = timezone.now)
    end_time   = models.DateTimeField(blank=True,null=True)
    is_resolved = models.BooleanField(default = False,null=False)
    selection_mode = models.IntegerField(
                choices = Choices,
                help_text=_("Determines how the Agent will get selected for the issue."))
    def __str__(self):
        return self.title

class Assignment(models.Model):
    issue = models.ForeignKey(Issue,on_delete = models.CASCADE,null=True)
    agent = models.ForeignKey(Profile,on_delete = models.SET_NULL,null=True)
    created = models.DateTimeField(default = timezone.now)
