from django.test import TestCase

# Create your tests here.


class IndexPageTest(TestCase):
    def test_root_url_resovles_to_index_page_view(self):
        # when
        response = self.client.get('/') #1
        
        # then
        self.assertEqual(response.status_code, 200) #2
        self.assertIn(response.content, 'Hello world!') #3