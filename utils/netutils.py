import difflib
import random
import re
import socket

import requests
import urllib3

from utils.output_utils import print_err, print_inf, print_suc

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 判断字符串中有没有英文字母
def is_contain_en(inp):
    return bool(re.search('[a-z]', inp))


# 检测是否为cidr
def check_cidr(inp: str):
    inp = inp.replace('https://', '')
    inp = inp.replace('http://', '')
    if '/' in inp:
        if not is_contain_en(inp):
            return True
        else:
            return False


# 检测是否为url
def check_url(inp: str):
    if 'http' in inp:
        try:
            requests.get(url=inp, timeout=1)
            return True
        except Exception:
            return False
    return False


# 检测是否为域名
def check_dom(inp: str):
    if is_valid_domain(inp):
        return True
    return False


# 判断是否为域名
def is_valid_domain(domain):
    pattern = re.compile(
        r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
        r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
    )
    return True if pattern.match(domain) else False


# 检查是否为ip
def check_ip(inp):
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(inp):
        return True
    else:
        return False


init_headers = {'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                'Sec-Ch-Ua-Platform': 'Sec-Ch-Ua-Platform',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'I am a really really really really really really really windows normal device',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                }


def generate_random_str(randomlength=8):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


# 解析域名
def resolve_domain(domain):
    hostip = ''

    try:
        hostip = socket.gethostbyname(domain)
        print(hostip)
    except socket.error as e:
        return None
    return hostip


# 过滤掉不可用的包字段
def fixpackage(content: str):
    content = content.replace('\n', '')
    content = content.replace('\r', '')
    content = content.replace('\t', '')
    content = content.replace(' ', '')
    return content


# 获取本机ip
def getlocalip():
    try:
        url = 'https://ip.gs/ip'
        r = requests.get(url, headers=init_headers).text
        r = fixpackage(r)
        return r
    except Exception:
        print_err('获取本地ip错误 请手动输入本地对外ip')
        exit(0)


def str_sim(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()  # 计算文本相似度


def getproxy(checkurl='https://www.baidu.com', v=False):
    reet = {}
    r = requests.get('https://free-proxy-list.com/', headers=init_headers).text
    ree = re.findall('alt="(.*)" title="', r)  # 分离代理信息
    if v:
        print_inf('连接代理池中')
    st = True
    while st:
        try:
            reet['http'] = ree[random.randint(0, 9)]
            if '200' not in str(
                    requests.get(url=checkurl, proxies=reet, headers=init_headers, timeout=5,
                                 verify=False).status_code):
                st = False
            break

        except Exception:
            # print(reet)
            if v:
                print_err('更换')
    if v:
        print_suc('连接成功')
    return reet
