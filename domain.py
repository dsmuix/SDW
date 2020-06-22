# -*- coding: utf-8 -*-

import requests
import os
import time
from colorama import Fore, Style

ascii = """
  #####  ######  #     # 
 #     # #     # #  #  # 
 #       #     # #  #  # 
  #####  #     # #  #  # 
       # #     # #  #  # 
 #     # #     # #  #  # 
  #####  ######   ## ##                 

 Search domain by word | @dsmuix                        
"""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    clear()
    print(Fore.LIGHTYELLOW_EX + ascii)
    print("[?] - Example: facebook")
    domain_name = input("[?] - Word to search: ")

    try:
        domain_request = requests.get(f'https://api.domainsdb.info/v1/domains/search?domain={domain_name}')
        domain_response = domain_request.json()

        infos = ['domain', 'country', 'isDead']
        
        for infos in domain_response['domains']:
            print(Fore.LIGHTYELLOW_EX + '\n[!] Domain:', infos['domain'])
            print(Fore.LIGHTYELLOW_EX + '[!] Country:', infos['country'])
            print(Fore.LIGHTYELLOW_EX + '[!] Offline:', infos['isDead'])
            print(Fore.LIGHTYELLOW_EX +
                  '[!] Created in:', infos['create_date'])

    except ConnectionError:
        print("[x] - Connection error")
        time.sleep(1)
        menu()


menu()
