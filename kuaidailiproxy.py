from selenium import webdriver
from time import sleep
from sql import SqlManager
import config
from proxy import Proxy
from time import sleep


def init_phantomjs_driver(*args, **kwargs):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
               'Connection': 'keep-alive'
               }

    for key, value in headers.items():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/48.0.2564.116 Safari/537.36'
    driver = webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400, 1000)
    return driver


class Proxies:
    """"
    a class object to get proxies from kuaidaili
    """
    baseurl1 = 'http://www.kuaidaili.com/free/inha/%d/'
    baseurl2 = 'http://www.kuaidaili.com/free/intr/%d/'

    def __init__(self):
        self.driver = init_phantomjs_driver()
        self.sql = SqlManager()
        self.sql.init_proxy_table(config.free_ipproxy_table)
        # self.urls = [Proxies.baseurl1 % i for i in range(1,5)]
        self.urls = [Proxies.baseurl1 % i for i in range(1, 11)] + [Proxies.baseurl2 % i for i in range(1, 11)]

    def run(self):
        for url in self.urls:
            self.get_proxy(url)

    def get_proxy(self, url):
        """
         get the list of proxies from the url using phantomjs
        :param driver: phantomjs driver
        :param url: url link of the page
        :return: a list contains the proxies
        """

        self.driver.get(url)
        sleep(2)
        if 'HTTP' not in self.driver.title:
            return []
        else:
            tbody = self.driver.find_element_by_tag_name('tbody')
            content = tbody.text.split('\n')
            proxies = []
            for line in content:
                tt = line.split()
                tmp = tt[0:4]
                tmp.append(''.join(tt[4:7]))
                proxies.append(tmp)

            for proxy in proxies:
                tmp = Proxy()
                tmp.set_value(
                    ip=proxy[0],
                    port=proxy[1],
                    country=proxy[4],
                    anonymity=proxy[2],
                    source='kuaidaili',
                )
                self.add_proxy(tmp)

    def add_proxy(self, proxy):
        """if in the testing mode, the spider will print out the proxy instead of inserting to the database"""
        if not config.TestMode:
            self.sql.insert_proxy(config.free_ipproxy_table, proxy)
        else:
            print(proxy)


if __name__ == "__main__":
    while True:
        try:
            kuaidaili = Proxies()
            kuaidaili.run()
        except:
            pass
        sleep(1200)
