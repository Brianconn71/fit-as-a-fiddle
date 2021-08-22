from django.test import SimpleTestCase
from checkout.forms import OrderForm


class TestForms(SimpleTestCase):

    def setUp(self):
        # set up for tests
        self.form = OrderForm({
            "full_name": "",
            "email": "",
            "phone_number": "",
            "street_address1": "",
            "street_address2": "",
            "town_or_city": "",
            "postcode": "",
            "country": "",
            "county": "",
        })

    ''' test forms in checkout are configured'''
    def test_fullname_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("full_name", form.errors.keys())
        self.assertEqual(form.errors["full_name"][0],
                         "This field is required.")

    def test_email_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors["email"][0],
                         "This field is required.")

    def test_phone_number_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("phone_number", form.errors.keys())
        self.assertEqual(form.errors["phone_number"][0],
                         "This field is required.")

    def test_street_address1_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("street_address1", form.errors.keys())
        self.assertEqual(form.errors["street_address1"][0],
                         "This field is required.")

    def test_town_or_city_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("town_or_city", form.errors.keys())
        self.assertEqual(form.errors["town_or_city"][0],
                         "This field is required.")

    def test_country_is_required(self):
        form = self.form
        self.assertFalse(form.is_valid())
        self.assertIn("country", form.errors.keys())
        self.assertEqual(form.errors["country"][0],
                         "This field is required.")

    def test_form_fields(self):
        form = OrderForm()
        fields = []
        for field in form.fields:
            fields.append(field)
            print(field)
        self.assertEqual(fields,
                         ["full_name", "email", "phone_number",
                          "street_address1", "street_address2",
                          "town_or_city", "postcode", "country", "county"])
