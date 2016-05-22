from django.test import TestCase

from .models import Wine, Winery


class TestWineFiltering(TestCase):
    def setUp(self):
        self.winery = Winery.objects.create(
            name="Test Winery",
            country="United States",
            region="DC")

    def test_in_cellar_filter_true(self):
        undrank_wine = Wine.objects.create(
            bottle_text="Nothing",
            wine_type="Red",
            year=2001,
            date_purchased="2016-01-01",
            winery=self.winery,
            store="Store",
            importer="Importer")
        drank_wine = Wine.objects.create(
            bottle_text="Nothing",
            wine_type="Red",
            year=2001,
            date_purchased="2016-01-01",
            winery=self.winery,
            store="Store",
            importer="Importer",
            date_consumed="2016-03-01")

        qs = Wine.objects.in_cellar()
        self.assertEqual(len(qs), 1)
        self.assertEqual(qs[0], undrank_wine)

    def test_in_cellar_filter_false(self):
        undrank_wine = Wine.objects.create(
            bottle_text="Nothing",
            wine_type="Red",
            year=2001,
            date_purchased="2016-01-01",
            winery=self.winery,
            store="Store",
            importer="Importer")
        drank_wine = Wine.objects.create(
            bottle_text="Nothing",
            wine_type="Red",
            year=2001,
            date_purchased="2016-01-01",
            winery=self.winery,
            store="Store",
            importer="Importer",
            date_consumed="2016-03-01")

        qs = Wine.objects.in_cellar(False)
        self.assertEqual(len(qs), 1)
        self.assertEqual(qs[0], drank_wine)
