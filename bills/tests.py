from django import forms
from django.test import TestCase
from django.urls import reverse

from clients.models import Client

from .forms import BillForm
from .models import Bill


class BillFormValidationTest(TestCase):

    def test_negative_quantity(self):
        """
        The form should be invalid if the quantity is <= 0.
        """
        client = Client.objects.create(name="Name", address="address")
        form = BillForm(data={
            'client': client,
            'item': 'Item',
            'quantity': -2,
            'rate': 100,
        })
        self.assertIs(form.is_valid(), False)

    def test_negative_rate(self):
        """
        The form should be invalid if the rate is <= 0.
        """
        client = Client.objects.create(name="Name", address="address")
        form = BillForm(data={
            'client': client,
            'item': 'Item',
            'quantity': 10,
            'rate': -0.1,
        })
        self.assertIs(form.is_valid(), False)


class CreateBillViewTest(TestCase):

    def test_create_bill_with_invalid_initial_client_id(self):
        """
        The create bill form should not crash if invalid initial client_id is given
        in the GET parameter.
        """
        client = Client.objects.create(name="Name", address="address")
        response = self.client.get(reverse('bills:create') + "?client_id=" + str(client.id + 100))
        self.assertEqual(response.status_code, 200)
