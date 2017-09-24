# coding=utf-8

import logging
import os
import sys
import subprocess
import run_validator

if __name__ == '__main__':
    # change the work dir to the current filefold, and make the log filefold.
    os.chdir(sys.path[0])
    if not os.path.exists('log'):
        os.makedirs('log')
    logging.basicConfig(
            filename=r'log/ipproxy.log',
            format='%(asctime)s: %(message)s',
            level=logging.INFO
    )
    # create three process to run the crawl, flask server, and new kuaidaili seperately.
    subprocess.Popen(['python', 'run_crawl_proxy.py'])
    subprocess.Popen(['python', 'run_server.py'])
    subprocess.Popen(['python', 'kuaidailiproxy.py'])  # get the proxies through the PhantomJS
    run_validator.validator()  # run the validator spiders


