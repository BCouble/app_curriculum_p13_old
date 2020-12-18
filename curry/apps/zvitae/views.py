from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from curry.apps.zvitae.forms import ZvitaeForm, CstateForm, AddressForm
from curry.apps.zvitae.models import Zvitae, CivilState, Address


@method_decorator(login_required, name='dispatch')
class ZvitaeView(ListView):
    """ View of curriculum """
    template_name = 'zvitae/zvitae.html'
    model = Zvitae
    context_object_name = 'zvitae'

    def get_context_data(self, **kwargs):
        """ Load context """
        context = super().get_context_data(**kwargs)
        context['zvitae'] = Zvitae.objects.filter(author_id=self.request.user)
        context['address'] = Address.objects.filter(zvitae_link_add=Zvitae.objects.filter(author_id=self.request.user).first())
        context['cstate'] = CivilState.objects.filter(zvitae_link_cs=Zvitae.objects.filter(author_id=self.request.user).first())
        return context

    def get_queryset(self):
        """ select Zvitae of user """
        return Zvitae.objects.filter(author_id=self.request.user)


@method_decorator(login_required, name='dispatch')
class ZvitaeDisplay(DetailView):
    """ load form for title and description """
    model = Zvitae

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ZvitaeForm()
        return context


@method_decorator(login_required, name='dispatch')
class ZvitaeCreate(CreateView):
    """ Create curriculum """
    model = Zvitae
    fields = ['title', 'description']
    success_url = reverse_lazy('zvitae:zview')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ZvitaeUpdate(UpdateView):
    """ Update curriculum """
    model = Zvitae
    context_object_name = 'zvitae'
    fields = ['title', 'description']
    success_url = reverse_lazy('zvitae:zview')


@method_decorator(login_required, name='dispatch')
class ZvitaeDelete(DeleteView):
    """ delete curriculum"""
    model = Zvitae
    context_object_name = 'zvitae'
    success_url = reverse_lazy('zvitae:zview')


@method_decorator(login_required, name='dispatch')
class CstateDisplay(DetailView):
    model = CivilState

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CstateForm()
        return context


@method_decorator(login_required, name='dispatch')
class CstateCreate(CreateView):
    model = CivilState
    fields = ['age', 'first_name', 'last_name', 'phone', 'linkedin', 'email', 'driving_licence']
    success_url = reverse_lazy('zvitae:zview')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zvitae_link_cs'] = Zvitae.objects.filter(author_id=self.request.user).first()
        return context

    def form_valid(self, form):
        form.instance.zvitae_link_cs = Zvitae.objects.filter(author_id=self.request.user).first()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CstateUpdate(UpdateView):
    model = CivilState
    context_object_name = 'cstate'
    fields = ['age', 'first_name', 'last_name', 'phone', 'linkedin', 'email', 'driving_licence']
    success_url = reverse_lazy('zvitae:zview')


@method_decorator(login_required, name='dispatch')
class CstateDelete(DeleteView):
    model = CivilState
    context_object_name = 'cstate'
    success_url = reverse_lazy('zvitae:zview')


# Address management
@method_decorator(login_required, name='dispatch')
class AddressDisplay(DetailView):
    model = Address

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddressForm()
        return context


@method_decorator(login_required, name='dispatch')
class AddressCreate(CreateView):
    model = Address
    context_object_name = 'address'
    fields = ['number', 'address', 'address2', 'city', 'postal_code']
    success_url = reverse_lazy('zvitae:zview')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zvitae_link_add'] = Zvitae.objects.filter(author_id=self.request.user).first()
        return context

    def form_valid(self, form):
        form.instance.zvitae_link_add = Zvitae.objects.filter(author_id=self.request.user).first()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AddressUpdate(UpdateView):
    model = Address
    context_object_name = 'address'
    fields = ['number', 'address', 'address2', 'city', 'postal_code']
    success_url = reverse_lazy('zvitae:zview')


@method_decorator(login_required, name='dispatch')
class AddressDelete(DeleteView):
    model = Address
    context_object_name = 'address'
    success_url = reverse_lazy('zvitae:zview')
