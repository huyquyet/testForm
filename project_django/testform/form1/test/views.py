from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from form1.forms import CreateForm, EditForm
from form1.test.models import Information


class CreateFormView(CreateView):
    model = Information
    form_class = CreateForm
    template_name = 'test/createForm.html'

    # def post(self,  *args, **kwargs):
    #     return True

    def dispatch(self, request, *args, **kwargs):
        return super(CreateFormView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('form1:index')

    def form_valid(self, form):
        form.save()
        return super(CreateFormView, self).form_valid(form)


class DetailView(ListView):
    model = Information
    context_object_name = 'form'
    template_name = 'test/detailForm.html'

    # def get_context_data(self, **kwargs):
    #     context = super(DetailView, self).get_context_data(**kwargs)
    #     context['form'] = self.object.all()
    #     return context


class EditView(UpdateView):
    model = Information
    form_class = EditForm
    # fields = ['last_name']
    template_name = 'test/editForm.html'
    context_object_name = 'form_edit'

    def dispatch(self, request, *args, **kwargs):
        return super(EditView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('form1:detail_form')

    def form_valid(self, form):
        form.save()
        return super(EditView, self).form_valid(form)


class DeleteView(DeleteView):
    model = Information
    context_object_name = 'delete_form'
    template_name = 'test/deleteForm.html'
    success_url = reverse_lazy('form1:detail_form')
