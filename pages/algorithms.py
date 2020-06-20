#Python imports
import random

from users.models import Profile

def agent_selector(issue):
    type = issue.selection_mode
    if type == 1:
        #This Query will assign any available agent to the issue not considering anything else
        available_agents = Profile.objects.filter(is_available=True)
        if available_agents:
            return random.choice(available_agents)
    if type == 2:
        #This Query selects the least busy Agent in our system
        return Profile.objects.filter(is_available=True).order_by('available_since').first()
    if type == 3:
        #This Query assigns any Agent to the issue disregarding whether the Agent is lready assigned or not
        available_agents = Profile.objects.filter()
        if available_agents:
            return random.choice(available_agents)
    return None
