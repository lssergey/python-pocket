#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

# http://code.google.com/p/soc/wiki/PythonStyleGuide

# This is a small script that demonstrates the API. It lets the user easily
# add tags to any items that do not currently have tags.
#
# Strategy:
# - Use get() to retrieve all items. We specify the tags flag so that the
#   tags are included in the returned results.
# - We iterate over all the items and for any item that does not have any
#   tags, we allow the user to input a comma separated list of tags.
# - When the user provides a set of tags for an item, we send the tags to
#   RIL with send().
# - Because we send the new tags during iteration, the user can exit the
#   script at any time without losing any of the new tags.

# Note: Update test_configs.py with your valid credentials.

import optparse

import readitlater
import test_configs as configs

def main():
  # Command line options.
  parser = optparse.OptionParser('usage: %prog [options]')
  parser.add_option('--unread', dest='unread', action='store_true',
                    default=False, help='Only tag unread items')
  (opts, args) = parser.parse_args()

  # Get all items.
  api = readitlater.API(configs.RIL_APIKEY, configs.RIL_USERNAME,
                        configs.RIL_PASSWORD)
  items = api.get(tags=True, state=('unread' if opts.unread else None))
  list = items['list']

  # Iterate over items.
  for k, v in list.items():
    if 'tags' not in v:
      # Found an item without tags. Get new tags from user.
      print u'\n{0}\n{1}'.format(v['title'], v['url'])
      print u'Comma separated tags or Enter to skip: ',
      tags = raw_input()
      if tags != '':
        # Send the new tags to RIL.
        api.send(update_tags=[{'url': v['url'], 'tags': tags}])

if __name__ == '__main__':
  main()
