from django.test import TestCase

from adminapp.models import Persons


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Persons.objects.create(name='Vladimir Putin')

    def test_name_label(self):
        persons = Persons.objects.get(id=1)
        field_label = persons._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        persons = Persons.objects.get(id=1)
        max_length = persons._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
