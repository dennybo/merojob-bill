from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from clients.models import Client

from .forms import BillForm
from .models import Bill


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'bills/bill_form.html'
    model = Bill
    form_class = BillForm
    success_url = reverse_lazy('bills:list')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Add bill'
        return context

    def get_initial(self):
        initial = super(CreateView, self).get_initial()

        # Check if client is already given
        client_id = self.request.GET.get('client_id')
        if client_id:
            try:
                initial['client'] = Client.objects.get(id=client_id)
            except Client.DoesNotExist:
                pass
        return initial


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = 'bills/bill_form.html'
    model = Bill
    form_class = BillForm
    success_url = reverse_lazy('bills:list')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Edit bill'
        return context


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Bill
    success_url = reverse_lazy('bills:list')


class ListView(generic.ListView):
    template_name = 'bills/bill_list.html'
    context_object_name = 'bills'

    def get_queryset(self):
        return Bill.objects.order_by('-created')
