from django.db import models


class Persons(models.Model):
    Name = models.CharField(max_length=2048, unique=True)

    def __str__(self):
        return self.Name


class Keywords(models.Model):
    Name = models.CharField(max_length=2048, unique=True)
    PersonId = models.ForeignKey(Persons, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.Name, self.PersonId.Name)


class PageQuerySet(models.QuerySet):
    def all(self):
        return self.values(SiteID__Name).count()

    def use(self):
        return self.filter(LastScanDate__isnull=True).count()

    def not_use(self):
        return self.filter(LastScanDate__isnull=False).count()
# class SiteManager(models.Manager):
#     def get_queryset(self):
#         return SiteQuerySet(self.model, using=self._db)
#
#     def all(self):
#         return self.get_queryset().all()


class Sites(models.Model):
    Name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.Name


class Pages(models.Model):
    Url = models.CharField(max_length=2048, unique=True)
    FoundDateTime = models.DateTimeField(auto_now_add=True)
    LastScanDate = models.DateTimeField(blank=True, null=True)
    SitesId = models.ForeignKey(Sites, on_delete=models.CASCADE)

    objects = models.Manager()  # The default manager.
    site_objects = PageQuerySet.as_manager()

    def __str__(self):
        return "{} ({})".format(self.Url, self.SitesId.Name)


class PersonPageRank(models.Model):
    Rank = models.PositiveIntegerField(default=0)
    PagesId = models.ForeignKey(Pages, on_delete=models.CASCADE)
    PersonId = models.ForeignKey(Persons, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({} {})".format(self.Rank, self.PersonId.Name, self.PagesId.Url)


