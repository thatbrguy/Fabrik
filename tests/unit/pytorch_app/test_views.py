import json
import os
import unittest
import torch 
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import Client


class UploadTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_pt_import(self):
        sample_file = os.path.join(settings.BASE_DIR, 'example','pytorch', 'test.pt')
        response = self.client.post(reverse('pytorch-import'), {'path': sample_file})
        # Ideally we would want to use the below lines instead, refer to docs
        #sample_file = open(os.path.join(settings.BASE_DIR, 'example','pytorch', 'test.pt'), 'rb')
        #response = self.client.post(reverse('pytorch-import'), {'file': sample_file})
        response = json.loads(response.content)
        self.assertEqual(response['result'], 'success')