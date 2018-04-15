#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

测试登录接口

"""

import argparse
import json
import traceback

from colorama import Fore, Style

from .utils import HttpUtil


def login(requests, config_path):
    try:
        with open(config_path, 'r') as f:
            config_json = json.loads(f.read())
            remote_url = config_json.get('base_url')
            if str(remote_url).endswith('/'):
                remote_url += 'api/login/'
            else:
                remote_url += '/api/login/'
            account = config_json.get('account')
            if account and account.get('username') and account.get('password'):
                post_data = {'username': account.get('username'), 'password': account.get('password')}
                return requests.post(remote_url, json=post_data)
            return None
    except:
        traceback.print_exc()
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test Login API')
    parser.add_argument('--config', type=str, default='config.json', help='config json path')
    args = parser.parse_args()
    client = HttpUtil()
    res = login(client.requests, args.config)

    if res is None:
        print(Fore.RED + 'Network Error')
    else:
        print(Fore.GREEN + str(res.status_code))
        print(res.text)
    print(Style.RESET_ALL)
