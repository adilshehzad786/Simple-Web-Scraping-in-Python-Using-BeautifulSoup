import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'viper-seo'
HOMEPAGE = 'https://www.olx.com.pk'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def create_job():

    for i in file_to_set(QUEUE_FILE):
        queue.put(i)
        queue.join()
        crawl()
def crawl():
    qlink=file_to_set(QUEUE_FILE)
    if len(qlink)>0:
        print(str(len(qlink))+ 'links in the queue')
        create_job()