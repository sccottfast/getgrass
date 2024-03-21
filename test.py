# -*- coding: utf-8 -*-
# @Time     :2023/12/26 17:00
# @Author   :ym
# @File     :main.py
# @Software :PyCharm
import asyncio
import random
import ssl
import json
import time
import uuid
import sys
from loguru import logger
from websockets_proxy import Proxy, proxy_connect

async def connect_to_wss(socks5, user_id,device_id):
    device_id_new = str(uuid.uuid3(uuid.NAMESPACE_DNS, socks5_proxy))
    print("设备编号",device_id_new)
    socks5_proxy=''
    device_id=''
    if socks5 in '$':
      socks5_proxy_array =socks5.split(",",2)
      socks5_proxy=socks5_proxy_array[0]
      device_id=socks5_proxy_array[1]
    else:
      socks5_proxy=socks5
      device_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, socks5_proxy))
    print(device_id)
    print(socks5_proxy)

async def main():
    _user_id = sys.argv[1]
    proxy = sys.argv[2]
    proxyNum = sys.argv[3]
    print('_user_id',_user_id)
    print('代理',proxy)
    print('代理数量',proxyNum)
    # TODO 修改代理列表
    socks5_proxy_list =proxy.split(",",int(proxyNum))
    print('代理',socks5_proxy_list)
    tasks = [asyncio.ensure_future(connect_to_wss(i, _user_id)) for i in socks5_proxy_list]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    # # 运行主函数
    asyncio.run(main())
