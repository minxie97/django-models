from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack

class SnacksTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester', email='tester@email.com', password='pass')
        self.snack = Snack.objects.create(
            name = 'Test Snack', purchaser = self.user, description='this is a test')

    def test_string_rep(self):
        self.assertEqual(str(self.snack), 'Test Snack')
        
    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'Test Snack')

    def test_user(self):
        self.assertEqual(f'{self.user.username}', 'tester')
        self.assertEqual(f'{self.user.email}', 'tester@email.com')
        
    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', "this is a test")

    def test_list_page_status_code(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        response = self.client.get(reverse("snack_list"))
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_detail_page_status_code(self):
        response = self.client.get(reverse("snack_detail", kwargs={'pk': self.snack.pk}))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        response = self.client.get(reverse("snack_detail", kwargs={'pk': self.snack.pk}))
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "base.html")