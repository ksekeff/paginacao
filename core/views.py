from django.views.generic import ListView

from .models import Produto


class IndexListView(ListView):
    model = Produto
    template_name = 'index.html'
    paginate_by = 10
    ordering = 'id'


