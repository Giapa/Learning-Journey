import os

def create_folder(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

def create_files(directory,homepage):
    queue = directory + '/queue.txt'
    crawled = directory + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, homepage)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path , data):
    file = open(path,'w')
    try:
        file.write(data)
    finally:
        file.close()

def add_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

def delete_file_cont(path):
    with open(path ,'w'):
        pass

# File to set of items
def file_to_set(file_name):
    results = set()
    with open(file_name , 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

def set_to_file(links , path):
    delete_file_cont(path)
    for link in sorted(links):
        add_to_file(link)