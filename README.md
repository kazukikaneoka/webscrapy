# webscrapy

A web scraping tool to extract and collect data from a website

## Installing & Uninstalling Dependencies Using Virtualenv

```
$ virtualenv venv # create virtualenv
$ source venv/bin/activate # activate virtualenv
$ pip3 install beautifulsoup4 && pip3 install requests # install dependencies
$ deactivate # deactivate virtualenv
$ rm -rf venv # uninstall dependencies
```

* You need to activate/deactivate virtualenv every time if you install the dependencies using virtualenv and you can keep your environment clean

## Installing & Uninstalling Dependencies Using setup.py

```
$ python3 setup.py install --user --prefix= --record dependencies.txt # install dependencies
$ cat dependencies.txt | xargs rm -rf # uninstall dependencies
```

* You can install dependencies by setup.py if you want to install dependencies in your environment as default

## How To Run

`$ python3 webscrapy.py [URL] ['HTML_TAG'] [-mnh]`

* URL is the website that you want to extract data from
* HTML_TAG is the data in the website that you want to collect
* Need to use single quotes between HTML_TAG

### Options

```
-h, --help         show this help message and exit
-n, --next         scrape next urls (next urls = urls which has the same prefix with URL)
-m MAX, --max MAX  max number of next urls to scrape (max number of next urls = infinite when not using -m)
```

### Example

`$ python3 main.py https://www.xxxxx.com/aa/bbb/c/ '<h2 class="test">' -n -m 10`
