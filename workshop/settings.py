BOT_NAME = 'workshop'

SPIDER_MODULES = ['workshop.spiders']
NEWSPIDER_MODULE = 'workshop.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

# # Enable Spidermon

SPIDERMON_ENABLED = True

EXTENSIONS = {
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}

SPIDERMON_SPIDER_CLOSE_MONITORS = {
    "workshop.monitors.SpiderCloseMonitorSuite"
}

# # Spidermon builtin monitor settings
SPIDERMON_MIN_ITEMS = 30
# SPIDERMON_ADD_FIELD_COVERAGE = True
# SPIDERMON_FIELD_COVERAGE_RULES = {
#     "dict/title": 0.4,  # Expected 40% coverage for field_1
#     "dict/link": 1.0,  # Expected 100% coverage for field_2
#     "dict/rating": 0.8,  # Expected 80% coverage for parent field_3
# }
