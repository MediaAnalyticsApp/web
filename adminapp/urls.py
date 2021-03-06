from django.urls import path, re_path
import adminapp.views as adminapp

urlpatterns = [
    path('main/', adminapp.main, name='main'),
    path('persons/read/', adminapp.PersonsListView.as_view(), name='persons'),
    path('persons/create/', adminapp.PersonCreateView.as_view(), name='person_create'),
    re_path(r'^persons/update/(?P<pk>\d+)/$', adminapp.PersonUpdateView.as_view(), name='person_update'),
    re_path(r'^persons/delete/(?P<pk>\d+)/$', adminapp.PersonDeleteView.as_view(), name='person_delete'),
    path('key_words/read/', adminapp.KeywordsListView.as_view(), name='key_words'),
    path('key_words/create/', adminapp.KeywordCreateView.as_view(), name='key_word_create'),
    re_path(r'^key_words/update/(?P<pk>\d+)/$', adminapp.KeywordUpdateView.as_view(), name='key_word_update'),
    re_path(r'^key_words/delete/(?P<pk>\d+)/$', adminapp.KeywordDeleteView.as_view(), name='key_word_delete'),
    path('sites/read/', adminapp.SitesListView.as_view(), name='sites'),
    path('sites/create/', adminapp.SiteCreateView.as_view(), name='site_create'),
    re_path(r'^sites/update/(?P<pk>\d+)/$', adminapp.SiteUpdateView.as_view(), name='site_update'),
    re_path(r'^sites/delete/(?P<pk>\d+)/$', adminapp.SiteDeleteView.as_view(), name='site_delete'),
    path('pages/read/', adminapp.PagesListView.as_view(), name='pages'),
    path('pages/create/', adminapp.PageCreateView.as_view(), name='page_create'),
    re_path(r'^pages/update/(?P<pk>\d+)/$', adminapp.PageUpdateView.as_view(), name='page_update'),
    re_path(r'^pages/delete/(?P<pk>\d+)/$', adminapp.PageDeleteView.as_view(), name='page_delete'),
    path('person_page_ranks/read/', adminapp.PersonPageRanksListView.as_view(), name='person_page_ranks'),
    path('person_page_ranks/create/', adminapp.PersonPageRankCreateView.as_view(), name='person_page_rank_create'),
    re_path(r'^person_page_ranks/update/(?P<pk>\d+)/$', adminapp.PersonPageRankUpdateView.as_view(),
            name='person_page_rank_update'),
    re_path(r'^person_page_ranks/delete/(?P<pk>\d+)/$', adminapp.PersonPageRankDeleteView.as_view(),
            name='person_page_rank_delete'),
    # path('sites/link/', adminapp.sites_link, name='site_link'),
    path('sites/export/', adminapp.export, name='export'),
    path('sites/link/', adminapp.SitesLinkView.as_view(), name='site_link'),
    path('sites/link/renew/', adminapp.links_renew, name='link_renew'),
    # path('pages/detail/', adminapp.PageDetail.as_view(), name='page_detail'),
    # path('pages/detail/(<int:page>/)', adminapp.PageDetail.as_view(), name='page_detail'),
    re_path(r'^pages/detail/(?P<page>\d+)?$', adminapp.PageDetail.as_view(), name='page_detail'),
    # re_path(r'^sites/detail/view/(?P<page>\d+)$', adminapp.SiteDetailView.as_view(), name='site_detail_view'),
    # path('sites/detail/view/page<int:page>/', adminapp.PagSiteDetailView.as_view(), name='site_detail_view_pag'),
    # re_path('sites/detail/view/(?P<pk>\d+)/$', adminapp.detail_renew, name='site_detail_view'),
]
