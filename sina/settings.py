# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Cookie':' _T_WM=b182e9f582724811da5a02610f137063; SUB=_2A25wKv3GDeRhGedG6FIU8C_KyTmIHXVT1IOOrDV6PUJbkdANLVmnkW1NUVMAnKCcR91zofR3GVy25VWTBkM0Wzb0; SUHB=0xnDHMVjJty4Hz; SCF=Ar_0lT6VYntllVB1CDoSwJ_C07kS0nXnyZRUaAAXie7jtWkaj5el4DiNrHBGTIhNy9qTENEiXOPPCcKdHy4vIRg'
}

# 当前是单账号，所以下面的 CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 请不要修改

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None
}

ITEM_PIPELINES = {
    'sina.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sina'
