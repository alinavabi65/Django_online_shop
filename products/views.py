from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


def test_translation(request):
    result = _('hello')
    messages.success(request, 'This is success message.')
    messages.error(request, 'This is success message.')
    messages.warning(request, 'This is success message.')
    messages.info(request, 'This is success message.')
    return render(request, 'products/testhello.html')


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    # def get_success_url(self):
    #     return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        products = get_object_or_404(Product, id=product_id)
        obj.products = products

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)



