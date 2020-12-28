from scrapy.statscollectors import StatsCollector
from scrapy.utils.serialize import ScrapyJSONEncoder
import simplejson


class MyStatsCollector(StatsCollector):
    def _persist_stats(self, stats, spider):
        encoder = ScrapyJSONEncoder()
        with open("stats.json", "w") as file:
            data = encoder.encode(stats)
            #simplejson.dump(data, file, indent=4)
            file.write(simplejson.dumps(simplejson.loads(data), indent=4, sort_keys=True))
            #file.write(data, )
