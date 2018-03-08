from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
def getsiteerroe(html):
    try:
        html = urlopen("https://www.w3schools.com/html/");
    except HTTPError as e:
        print(e);
    except URLError as e:
        print("url not found");
    else:
        print("all good");