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
import mycontext as my
from django.db.models import Sum, Count
from django.template.loader import render_to_string
from django.http import JsonResponse


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
    fields = '__all__'

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

    def get_queryset(self):
        qweryset = super().get_queryset()
        print(Pages.site_objects.all())
        print(qweryset)
        return qweryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        print(self.object_list[0].Url)
        context.update(my.page)

        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def sites_link(request):

    all = Pages.objects.all().values('SitesId__Name').annotate(Count('Url'))
    not_use = Pages.objects.filter(LastScanDate__isnull=True).values('SitesId__Name').annotate(Count('Url'))
    use = Pages.objects.filter(LastScanDate__isnull=False).values('SitesId__Name').annotate(Count('Url'))

    all_link = zip(all, not_use,  use)

    content = {
        'all_link': all_link,
    }

    return render(request, 'adminapp/site_detail.html', content)


def links_renew(request):
    all = Pages.objects.all().values('SitesId__Name').annotate(Count('Url'))
    not_use = Pages.objects.filter(LastScanDate__isnull=True).values('SitesId__Name').annotate(Count('Url'))
    use = Pages.objects.filter(LastScanDate__isnull=False).values('SitesId__Name').annotate(Count('Url'))

    all_link = zip(all, not_use,  use)

    content = {
        'all_link': all_link,
    }

    result = render_to_string('adminapp/includes/inc_detail.html', content)
    return JsonResponse({'result': result})
