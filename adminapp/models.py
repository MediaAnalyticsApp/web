from django.db import models


class Keywords(models.Model):
    name = models.CharField(max_length=255, unique=True)
    person = models.ForeignKey('Persons', on_delete=models.CASCADE)

    class Meta:
        db_table = "keywords"

    def __str__(self):
        return "{} ({})".format(self.name, self.person.name)


class Pages(models.Model):
    url = models.CharField(max_length=255, unique=True)
    site = models.ForeignKey('Sites', on_delete=models.CASCADE)
    found_date_time = models.DateTimeField(auto_now_add=True)
    last_scan_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "pages"

    def __str__(self):
        return "{} ({})".format(self.url, self.site.name)


class PersonPageRank(models.Model):
    person = models.ForeignKey('Persons', on_delete=models.CASCADE)
    page = models.ForeignKey(Pages, on_delete=models.CASCADE)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "person_page_rank"

    def __str__(self):
        return "{} ({} {})".format(self.rank, self.person.name, self.page.url)


class Persons(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "persons"

    def __str__(self):
        return self.name


class Sites(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "sites"

    def __str__(self):
        return self.name
