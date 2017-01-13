from django.db import models
from django.urls import reverse


class Client(models.Model):

    # Core fields
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    # Timestamps
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clients:detail', kwargs={'pk': self.pk})
