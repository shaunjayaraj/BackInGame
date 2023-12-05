list_cache = []
requests = []



fifo_count = 0

def fifo(page_number):
    #first in first out
    if(len(list_cache < 8):
        list_cache.append(page_number)
    else:
        list_cache[fifo_count] = page_number
        if (fifo_count < 7):
            fifo_count = fifo_count + 1
        else:
            fifo_count = 0

cache_miss_strategy = fifo

freq_dict = {}

def lfu(page_number):
    list_cache.append(page_number)
    

def assign_cache_miss_strategy(option):
    if option == 1:
        cache_miss_strategy = fifo
    else:
        cache_miss_strategy = lfu

def acceptRequests(page_number):
    requests.append(page_number)


def getPage(page_number):
    if page_number in list_cache:
        return hit(page_number)
    else:
        return miss(page_number)
    
def hit(page_number):
    print('hit')
    return page_number

def miss(page_number):
    print('miss')
    cache_miss_strategy(page_number)
    return -1

def processRequests():
    for request in requests:
        getPage(request)
    
