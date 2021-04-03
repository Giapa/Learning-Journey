import threading #for multithreading
from queue import Queue #for multithreading
from spider import Spider
from domain import *
from general import *

#change those to input for gui
PROJECT_NAME = 'kalovelo' #ALL CAPS=CONST
HOMEPAGE = 'https://kalovelo.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create threads. I kill the spiders when we main exits
def create_threads():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True #ensure that it dies when exit
        t.start()

# each link in queue is a new job ( todo list )
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#Check queue.txt and crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

#work work work work work, you see me i be work, work ,work 
# Do job of the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()