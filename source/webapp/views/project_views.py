from django.db.models import Q

from webapp.forms import SimpleSearchForm
from django.views.generic import ListView, TemplateView, FormView

from webapp.models import Project


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'projects'
    paginate_by = 10
    paginate_orphans = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Project.objects.all()
        #
        # is_admin = self.request.GET.get('is_admin', None)
        # if not is_admin:
        #     data = Task.objects.filter('-created_at')
        # form = SimpleSearchForm(data=self.request.GET)
        # if form.is_valid():
        #     search = form.cleaned_data['search']
            # if search:
            #     data = data.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return data.order_by('-created_at')