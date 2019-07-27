# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Cookie':'_T_WM=f150f7579128653b503da3fd9a2fa816; SUB=_2A25wPjlnDeRhGedG6FIU8C_KyTmIHXVTwUcvrDV6PUJbkdAKLWP5kW1NUVMAnAMhQZ4i5wUGQFLRTq7lCfbf2ojU; SUHB=0TPUE8CQgh9Hak; SCF=AtBQ1hUrSiUeCJtHCUovtNQQd4ru6T2DnDlDLnkkMwWXAvQfgDKPU_DhVXmndNwaVMhWptoCFjtIfp5MIbRSsmA.; SSOLoginState=1564100919'
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

# 搜索时长，即最后一条微博距离现在的天数
LAST_TWEET_FROM_NOW_IN_DAYS = 1
