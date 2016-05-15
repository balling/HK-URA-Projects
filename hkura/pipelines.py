import scraperwiki
from scrapy import log

class MorphIOPipeline(object):
    def process_item(self, item, domain):
        try:
            scraperwiki.sql.save(unique_keys=['link', 'last_updated'], data=item)
        except:
            log.msg('Failed to insert item: ' + item['link'])
        return item
