from django.db import models


class order(models.Model):
    """Model representing an order in the system.
    """

    user = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=10, default=1)

    def str(self):
        return f"{self.id} {self.user.username} - {self.status} ({self.total_amount})"
