from django.db import models

# Create your models here.

class Ticket (models.Model):
                state_choices = [
                        ('open', 'open'),
                        ('progress', 'progress'),
                        ('pending', 'pending'),
                        ('done', 'done'),
                ]



                state = models.CharField(choices=state_choices, max_length =256, default = "open")
                title = models.CharField(max_length= 256)
                description = models.TextField()

                priority_choices = [
                        (3, 'high'),
                        (2, 'medium'),
                        (1, 'low'),

                ]
                priority = models.IntegerField(choices = priority_choices, default=2)

                created = models.DateTimeField(auto_now_add = True)
                update = models.DateTimeField(auto_now = True)

                def __str__(self):
                        return self.title