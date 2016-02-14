import random
import urllib.request

def download_web_url(url):
    x=random.randrange(1,1000)
    save_filename = str(x) + "_py_download_test.jpg"
    urllib.request.urlretrieve(url,save_filename)

for i in range(1,20):
    download_web_url("http://www.photohumor.com/joomla/images/Iran%20supports%20Hillary%202016.jpg")


