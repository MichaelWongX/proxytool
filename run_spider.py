# -*- coding: utf-8 -*-

import os
import logging
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


def runspider(name):
    configure_logging(install_root_handler=False)
    process = CrawlerProcess(get_project_settings())
    process.settings.update(
        {'LOG_LEVEL': 'INFO',
         'LOG_FILE': 'log/%s.log' % name}
    )
    logging.basicConfig(
        level=logging.INFO,
        filename='log/spider.log',
        format='%(asctime)s %(levelname)s: %(message)s',
    )
    try:
        logging.info('runspider start spider:%s' % name)
        process.crawl(name)
        process.start()
    except Exception as e:
        logging.exception('runspider spider:%s exception:%s' % (name, e))

    logging.debug('finish this spider:%s\n\n' % name)


if __name__ == '__main__':
    """
    num = 12
    ls = ['xici','data5u','freeproxylists', 'gatherproxy', 'hidemy', 'ip181', 'kuaidaili', 'peuland', 'proxydb',
          'proxylistplus', 'proxyrox', 'sixsixip', 'usproxy']
    try:
        name = ls[num]
        runspider(name)
    except Exception as e:
        logging.exception('run_spider main exception msg:%s' % e)
    """
    try:
        name = sys.argv[1] or 'base'
        runspider(name)
    except Exception as e:
        logging.exception('run_spider main exception msg:%s' % e)