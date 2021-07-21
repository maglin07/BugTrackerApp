from django.db import models
from customuser.models import CustomUser


# Create your models here.
class TicketModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    date_filed = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    ticket_submitted = models.ForeignKey(CustomUser, related_name="ticket_submitted", on_delete=models.CASCADE, null=True) # noqa
    ticket_assigned = models.ForeignKey(CustomUser, related_name="ticket_assigned", on_delete=models.CASCADE, null=True) # noqa
    ticket_completed = models.ForeignKey(CustomUser, related_name="ticket_completed", on_delete=models.CASCADE, null=True) # noqa

    class ticket_status(models.TextChoices):
        New = 'N', ('New')
        InProgress = 'P', ('In Progress')
        Done = 'D', ('Done')
        Invalid = 'I', ('Invalid')

    status = models.CharField(
        max_length=10, choices=ticket_status.choices, default='New')

    def __str__(self):
        return self.title

