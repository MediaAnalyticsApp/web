from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.models import User
from .models import Persons, Keywords, Sites, Pages, PersonPageRank
# from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
import mycontext as my
from django.db.models import Count
from django.template.loader import render_to_string
from django.http import JsonResponse
from .resources import PagesResource
# from django.shortcuts import get_object_or_404
from .forms import PagesForm


def main(request):
    title = 'Главная админ'

    context = {'title': title}

    return render(request, 'adminapp/main.html', context)


class PersonsListView(ListView):
    model = Persons
    template_name = 'adminapp/objects.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonCreateView(CreateView):
    model = Persons
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:persons')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonUpdateView(UpdateView):
    model = Persons
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:persons')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonDeleteView(DeleteView):
    object = ''
    model = Persons
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('myadmin:persons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class KeywordsListView(ListView):
    model = Keywords
    template_name = 'adminapp/objects.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.key_word)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class KeywordCreateView(CreateView):
    model = Keywords
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:key_words')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.key_word)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class KeywordUpdateView(UpdateView):
    model = Keywords
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:key_words')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.key_word)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class KeywordDeleteView(DeleteView):
    model = Keywords
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('myadmin:key_words')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.key_word)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SitesListView(ListView):
    model = Sites
    template_name = 'adminapp/objects.html'
    # fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.site)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SiteCreateView(CreateView):
    model = Sites
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:sites')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.site)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SiteUpdateView(UpdateView):
    model = Sites
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:sites')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.site)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SiteDeleteView(DeleteView):
    model = Sites
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('myadmin:sites')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.site)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PagesListView(ListView):
    model = Pages
    template_name = 'adminapp/objects.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.page)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PageCreateView(CreateView):
    model = Pages
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:pages')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.page)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PageUpdateView(UpdateView):
    model = Pages
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:pages')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.page)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PageDeleteView(DeleteView):
    object = ''
    model = Pages
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('myadmin:pages')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.page)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonPageRanksListView(ListView):
    model = PersonPageRank
    template_name = 'adminapp/objects.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person_page_rank)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonPageRankCreateView(CreateView):
    model = PersonPageRank
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:person_page_ranks')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person_page_rank)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonPageRankUpdateView(UpdateView):
    model = PersonPageRank
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('myadmin:person_page_ranks')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person_page_rank)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonPageRankDeleteView(DeleteView):
    object = ''
    model = PersonPageRank
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('myadmin:person_page_ranks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(my.person_page_rank)
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SitesLinkView(ListView):
    model = Pages
    template_name = 'adminapp/site_detail.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        every = Pages.objects.all().values('site_id__name').annotate(Count('url'))
        not_use = Pages.objects.filter(last_scan_date__isnull=True).values('site__name').annotate(Count('url'))
        use = Pages.objects.filter(last_scan_date__isnull=False).values('site__name').annotate(Count('url'))

        all_every = Pages.objects.all().count()
        all_not_use = Pages.objects.filter(last_scan_date__isnull=True).count()
        all_use = Pages.objects.filter(last_scan_date__isnull=False).count

        if all_every == all_not_use:
            use = [{'url__count': 0} for i in range(all_every)]

        if all_every == all_use:
            not_use = [{'url__count': 0} for i in range(all_every)]

        all_link = zip(every, not_use, use)

        link = {
            'all_every': all_every,
            'all_not_use': all_not_use,
            'all_use': all_use,
            'all_link': all_link,
        }

        context.update(link)

        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# def sites_link(request):
#
#     every = Pages.objects.all().values('site_id__name').annotate(Count('url'))
#     not_use = Pages.objects.filter(last_scan_date__isnull=True).values('site_id__name').annotate(Count('url'))
#     use = Pages.objects.filter(last_scan_date__isnull=False).values('site_id__name').annotate(Count('url'))
#
#     all_every = Pages.objects.all().count()
#     all_not_use = Pages.objects.filter(last_scan_date__isnull=True).count()
#     all_use = Pages.objects.filter(last_scan_date__isnull=False).count
#
#     all_link = zip(every, not_use,  use)
#
#     content = {
#         'all_every': all_every,
#         'all_not_use': all_not_use,
#         'all_use': all_use,
#         'all_link': all_link,
#     }
#
#     return render(request, 'adminapp/site_detail.html', content)


def links_renew(request):

    if request.is_ajax():
        every = Pages.objects.all().values('site_id__name').annotate(Count('url'))
        not_use = Pages.objects.filter(last_scan_date__isnull=True).values('site__name').annotate(Count('url'))
        use = Pages.objects.filter(last_scan_date__isnull=False).values('site__name').annotate(Count('url'))

        all_every = Pages.objects.all().count()
        all_not_use = Pages.objects.filter(last_scan_date__isnull=True).count()
        all_use = Pages.objects.filter(last_scan_date__isnull=False).count

        if all_every == all_not_use:
            use = [{'url__count': 0} for i in range(all_every)]

        if all_every == all_use:
            not_use = [{'url__count': 0} for i in range(all_every)]

        all_link = zip(every, not_use, use)

        content = {
            'all_every': all_every,
            'all_not_use': all_not_use,
            'all_use': all_use,
            'all_link': all_link,
        }

        result = render_to_string('adminapp/includes/inc_detail.html', content)
        return JsonResponse({'result': result})


def export(request):
    pages_resource = PagesResource()
    queryset = Pages.objects.all()
    dataset = pages_resource.export(queryset)
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pages.csv"'
    return response


class SiteDetail(ListView):
    model = Pages
    template_name = 'adminapp/site_detail_view.html'
    fields = '__all__'

    # def get_queryset(self):
    #     # self.site = get_object_or_404(Sites, pk=self.kwargs['pk'])
    #     qwe = Pages.objects.filter(site__pk=self.kwargs['pk']).order_by('url')
    #     # print(qwe)
    #     return qwe
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site = Sites.objects.all()
        context['site'] = site
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def detail_renew(request, pk):

    if request.is_ajax():

        site = Sites.objects.all()
        object_list = Pages.objects.filter(site=pk)
        content = {
            'site': site,
            'object_list': object_list,
        }

        result = render_to_string('adminapp/includes/inc_detail_view.html', content)
        return JsonResponse({'result': result})


def site_detail_view(request):
    page = Pages.objects.all()
    form = PagesForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['site']:
            page = page.filter(site=form.cleaned_data['site'])
        if form.cleaned_data['ordering_url']:
            page = page.order_by(form.cleaned_data['ordering_url'])
        if form.cleaned_data['ordering_found']:
            page = page.order_by(form.cleaned_data['ordering_found'])
        if form.cleaned_data['ordering_last']:
            page = page.order_by(form.cleaned_data['ordering_last'])
    context = {'object_list': page, 'site': form}
    return render(request, 'adminapp/site_detail_view.html', context)
