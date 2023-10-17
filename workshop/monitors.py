from spidermon import Monitor, MonitorSuite, monitors
from spidermon.contrib.scrapy.monitors.monitors import ItemCountMonitor, FieldCoverageMonitor, PeriodicExecutionTimeMonitor

@monitors.name('Item count basic')
class ItemCountBasicMonitor(Monitor):

    @monitors.name('Minimum number of items')
    def test_minimum_number_of_items(self):
        item_extracted = getattr(
            self.data.stats, 'item_scraped_count', 0)
        minimum_threshold = 30

        msg = 'Extracted less than {} items'.format(
            minimum_threshold)
        self.assertTrue(
            item_extracted >= minimum_threshold, msg=msg
        )


class SpiderCloseMonitorSuite(MonitorSuite):

    monitors = [
        ItemCountBasicMonitor,
        # ItemCountMonitor,
        # FieldCoverageMonitor,
    ]
