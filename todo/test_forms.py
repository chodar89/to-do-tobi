from django.test import TestCase
from .forms import ItemForm

# Create your tests here.

class TesToDoItemForm(TestCase):

    def test_can_create_an_item_with_jus_a_name(self):
        form = ItemForm({'name': 'Create Website'})
        self.assertTrue(form.is_valid())
        
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])