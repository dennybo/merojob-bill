from django.db import models

from clients.models import Client


class Bill(models.Model):

    # Core fields
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    quantity = models.IntegerField()
    rate = models.FloatField()

    # Timestamps
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'

    def __str__(self):
        return "{client}: {item}".format(client=self.client, item=self.item)

    def total(self):
        return self.quantity * self.rate
