#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/7/4 12:04
# @Author  : weather
# @Software: PyCharm
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# import argparse


def page_results(all_voc):
    chinese = []
    english = []
    for i, voc in enumerate(all_voc[:-1]):
        txt = voc.get_text()
        if i % 4 == 0:
            chinese.append(txt.replace(',', ' '))
        elif i % 4 == 1:
            english.append(txt)
    df = pd.DataFrame.from_dict({'中文': chinese, '英文': english})
    return df


def parser_page(url):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                   'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE '
    # }
    all_voc = None
    try:
        response = requests.get(url)
        html_doc = response.text.encode('utf-8')
        soup = BeautifulSoup(html_doc, 'html.parser')
        all_voc = soup.find_all('td')
    except:
        print(url + '  \n failed!')
    return all_voc


# def parser_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--base', type=str, help='base url for spider')
#     parser.add_argument('--max_pages', type=int, help='max pages')
#     parser.add_argument('-o','--output_name', type=str, help='output name')
#     args = parser.parse_args()
#     return args


def main():
    baseurl = 'https://www.letpub.com.cn/index.php?page=dict&level1=%E5%9C%B0%E7%90%83%E7%A7%91%E5%AD%A6&level2=%E5%9C%B0%E7%90%86%E5%AD%A6&k=&currentpage='
    max_pages = 971
    output_name = '地理学'
    results = []
    for i in range(1, max_pages + 1):
        url = baseurl + str(i)
        vocs = parser_page(url)
        if vocs is not None:
            res = page_results(vocs)
            results.append(res)
            print("{}/{} completed".format(i, max_pages))
            time.sleep(1.5)
        else:
            pass
    final = pd.concat(results, ignore_index=True)
    final.to_csv(output_name + '.csv', encoding='GB18030', index=None)


if __name__ == "__main__":
    # args = parser_args()
    main()
