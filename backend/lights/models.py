from django.db import models

class Light(models.Model):
    Light_states = [(0,'OFF'), (1,'ON')]
    name = models.CharField(max_length=10, null=True)
    state = models.IntegerField(choices=Light_states, default=0)