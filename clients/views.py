from django.urls import reverse_lazy
from django.views import generic

from .forms import ClientForm
from .models import Client


class ClientList(generic.ListView):
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.order_by('name')


class ClientDetail(generic.DetailView):
    model = Client
    template_name = 'clients/client_detail.html'


class ClientCreate(generic.edit.CreateView):
    template_name = 'clients/client_form.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')

    def get_context_data(self, **kwargs):
        context = super(ClientCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Add client'
        return context


class ClientUpdate(generic.edit.UpdateView):
    template_name = 'clients/client_form.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')

    def get_context_data(self, **kwargs):
        context = super(ClientUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Edit client'
        return context


class ClientDelete(generic.edit.DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')
