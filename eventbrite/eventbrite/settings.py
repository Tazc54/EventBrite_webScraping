# Scrapy settings for eventbrite project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Googlebot'

SPIDER_MODULES = ['eventbrite.spiders']
NEWSPIDER_MODULE = 'eventbrite.spiders'

FEEDS = {'items.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': ['event_name', 'event_start_date', 'event_start_time', 'event_end_date', 'event_end_time',
                   'event_category', 'event_format', 'event_organizer', 'event_location', 'event_url', 'event_image',
                   'event_location_type'],
        'indent': 4,
}}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'eventbrite (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
IMAGES_RESULT_FIELD = 'event_image'
IMAGES_EXPIRES = 30
IMAGES_STORE = r'C:\Users\alemancx\Documents\eventbrite\eventbrite\eventbrite\images'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 7
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
ROTATING_PROXY_LIST_PATH = r'C:\Users\alemancx\Documents\eventbrite\eventbrite\eventbrite\list.txt'

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'eventbrite.middlewares.EventbriteSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'eventbrite.middlewares.EventbriteDownloaderMiddleware': 543,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 700,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.logstats.LogStats': 500,
#    'scrapy.extensions.telnet.TelnetConsole': None,

}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1
#    'eventbrite.pipelines.EventbritePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 7
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#  LOGGING SETTINGS
LOG_FILE = 'log.txt'
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'WARNING'

#  UA SETTINGS
RANDOM_UA_TYPE = 'desktop.random'

#  STATS
STATS_CLASS = 'eventbrite.MyStatsCollector.MyStatsCollector'
