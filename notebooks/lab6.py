import threading
import time
import requests # pip install requests

img_urls = ['https://images.unsplash.com/photo-1504208434309-cb69f4fe52b0', 'https://images.unsplash.com/photo-1485833077593-4278bba3f11f', 'https://images.unsplash.com/photo-1593179357196-ea11a2e7c119', 'https://images.unsplash.com/photo-1526515579900-98518e7862cc', 'https://images.unsplash.com/photo-1582376432754-b63cc6a9b8c3', 'https://images.unsplash.com/photo-1567608198472-6796ad9466a2', 'https://images.unsplash.com/photo-1487213802982-74d73802997c', 'https://images.unsplash.com/photo-1552762578-220c07490ea1', 'https://images.unsplash.com/photo-1569691105751-88df003de7a4', 'https://images.unsplash.com/photo-1590691566903-692bf5ca7493', 'https://images.unsplash.com/photo-1497206365907-f5e630693df0', 'https://images.unsplash.com/photo-1469765904976-5f3afbf59dfb']

def lab5q1(URL):
    response = requests.get(URL)
    fileName = URL.rsplit('/', 1).pop()
    file = open(fileName + ".jpg", "wb")
    file.write(response.content)
    file.close()
    print('File ' + file.name + ' successfully saved. ')

def lab6q1():
    timer = time.perf_counter()
    for i in img_urls:
        lab5q1(i)
    timer = time.perf_counter() - timer
    print(f'{len(img_urls)} images downloaded in {timer} seconds. ')

def lab6q2():
    timer = time.perf_counter()
    for i in img_urls:
        t = threading.Thread(target=lab5q1, name=i, args=[i])
        t.start()

    t.join()
    timer = time.perf_counter() - timer
    print(f'{len(img_urls)} images downloaded in {timer} seconds. ')

lab6q1()
lab6q2()


