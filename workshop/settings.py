BOT_NAME = 'workshop'

SPIDER_MODULES = ['workshop.spiders']
NEWSPIDER_MODULE = 'workshop.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
