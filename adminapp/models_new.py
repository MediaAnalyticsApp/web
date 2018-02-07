from django.db import models


class Keywords(models.Model):
    name = models.CharField(max_length=255)
    person = models.ForeignKey('Persons', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "keywords"

    def __str__(self):
        return "{} ({})".format(self.name, self.person.name)


class Pages(models.Model):
    url = models.CharField(max_length=255)
    site = models.ForeignKey('Sites', models.DO_NOTHING)
    found_date_time = models.DateTimeField()
    last_scan_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pages"

    def __str__(self):
        return "{} ({})".format(self.url, self.site.name)


class PersonPageRank(models.Model):
    person = models.ForeignKey('Persons', models.DO_NOTHING)
    page = models.ForeignKey(Pages, models.DO_NOTHING)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "person_page_rank"

    def __str__(self):
        return "{} ({} {})".format(self.rank, self.person.name, self.page.url)


class Persons(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "persons"

    def __str__(self):
        return self.name


class Sites(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "sites"

    def __str__(self):
        return self.name
