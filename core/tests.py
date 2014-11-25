from django.test import TestCase


class TestReproduceError(TestCase):
    def test_reproduce(self):
        from core.models import TestModel
        obj = TestModel(test_field=12222)
        obj.full_clean()
