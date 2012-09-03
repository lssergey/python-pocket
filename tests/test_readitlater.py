#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

# http://code.google.com/p/soc/wiki/PythonStyleGuide

import logging
import unittest

import readitlater
import test_configs as configs

'''Before running the tests, update test_configs.py with valid credentials.
'''

class TestAPI(unittest.TestCase):
  def setUp(self):
    self.api = readitlater.API(configs.RIL_APIKEY, configs.RIL_USERNAME,
                   configs.RIL_PASSWORD)

  def test_auth_valid_creds(self):
    self.assertTrue(self.api.auth())

  def test_auth_invalid_creds(self):
    api = readitlater.API(configs.RIL_APIKEY, 'invalid_user', 'invalid_password')
    self.assertRaises(readitlater.AuthError, api.auth)

  def test_add(self):
    self.assertTrue(self.api.add(
      'http://google.com/', 'Google'))

  def test_send_new(self):
    data = [{'url': 'http://google.com',
         'title': 'Google',
         'ref_id': '123456709'},
        {'url': 'http://ideashower.com',
         'title': 'The Idea Shower'}]
    self.assertTrue(self.api.send(new=data))

  def test_send_read(self):
    data = [{'url': 'http://google.com'},
        {'url': 'http://ideashower.com'}]
    self.assertTrue(self.api.send(read=data))

  def test_send_update_title(self):
    data = [{'url': 'http://google.com',
         'title': 'Google'},
        {'url': 'http://ideashower.com',
         'title': 'The Idea Shower'}]
    self.assertTrue(self.api.send(update_title=data))

  def test_send_update_tags(self):
    data = [{'url': 'http://google.com',
         'tags': 'comma,seperated,list'},
        {'url': 'http://ideashower.com',
         'tags': 'ideas,developer,nate weiner'}]
    self.assertTrue(self.api.send(update_tags=data))

  def test_get(self):
    items = self.api.get()
    list = items['list']
    # Search items for the previously added ones.
    found = False
    for k, v in list.items():
      if v['url'] == 'http://google.com':
        found = True
        break
    self.assertTrue(found)

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG, filename='test.log')
  testsuite = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
  unittest.TextTestRunner(verbosity=2).run(testsuite)
