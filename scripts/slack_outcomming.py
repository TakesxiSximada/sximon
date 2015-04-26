#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
import requests


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='http://localhost:6543/outcomming')
    args = parser.parse_args(argv)

    res = requests.post(args.host, {
        'token': 'XXXXXXXXXXXXXX',
        'team_id': 'T0001',
        'team_domain': 'example',
        'channel_id': 'channel_1',
        'channel_name': 'test_channel',
        'timestamp': '123456.01234',
        'user_id': 'U42134121',
        'user_name': 'sximada',
        'text': 'message message message message message',
        'trigger_word': 'google',
        })
    import ipdb; ipdb.set_trace()
    pass

if __name__ == '__main__':
    sys.exit(main())
