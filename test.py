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

async def connect_to_wss(socks5_proxy, user_id,device_id):
    if len(device_id)==0:
       print('没有设备id重新生成') 
       device_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, socks5_proxy))
    logger.info(device_id)


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
    tasks = [asyncio.ensure_future(connect_to_wss(i.split("$",2)[0], _user_id,i.split("$")[1])) for i in socks5_proxy_list]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    # # 运行主函数
    asyncio.run(main())
