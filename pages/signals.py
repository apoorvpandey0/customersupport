#This is the signal that will be sent
from django.db.models.signals import post_save,pre_delete
#This is the object which will send the signal
from .models import Issue
#This will receive the signal
from django.dispatch import receiver
from django.utils import timezone

#We need this to perform operations on Assignments table
from .models import Assignment
#We need this model for agent_selector
from users.models import Profile
#This is the selection algorithm
from .algorithms import agent_selector

#
#This function creates new profile for each user created
@receiver(post_save, sender=Issue)
def create_Assignment(sender, instance, created, **kwargs):
    if created:
        agent = agent_selector(issue = instance)
        Assignment.objects.create(issue=instance,agent = agent)
        if agent:
            agent.is_available=False
            agent.save()
        else:
            print("No Agents Available.")

@receiver(pre_delete, sender=Assignment)
def delete_Assignment(sender, instance,using, **kwargs):
    agent = instance.agent
    issue = Issue.objects.get(id=instance.issue.id)
    print(issue)
    issue.is_resolved=True
    issue.save()
    if agent:
        agent.is_available=True
        agent.available_since=timezone.now()
        agent.save()



#This function saves those newly created profiles
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
#     print("Save_Assignment function executed!")
