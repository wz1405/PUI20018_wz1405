import os
import urllib.request as url
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if os.getenv ('PUIDATA') is None:
    print ("Must set env variable PUIdata")

url94 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp94totals.zip"
url95 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp95totals.zip"
url96 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp96totals.zip"
url97 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp97totals.zip"
url98 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp98totals.zip"
url99 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp99totals.zip"
url00 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp00totals.zip"
url01 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp01totals.zip"
url02 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp02totals.zip"
url03 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp03totals.zip"
url04 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp04totals.zip"
url05 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp05totals.zip"
url06 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp06totals.zip"
url07 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp07totals.zip"
url08 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp08totals.zip"
url09 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp09totals.zip"
url10 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp10totals.zip"
url11 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp11totals.zip"
url12 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp12totals.zip"
url13 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp13totals.zip"
url14 = "https://github.com/fedhere/PUI2018_fb55/raw/master/HW12_fb55/zbp14totals.zip"

urllib.urlretrieve(url94, "zbp94totals.zip")
urllib.urlretrieve(url95, "zbp95totals.zip")
urllib.urlretrieve(url96, "zbp96totals.zip")
urllib.urlretrieve(url97, "zbp97totals.zip")
urllib.urlretrieve(url98, "zbp98totals.zip")
urllib.urlretrieve(url99, "zbp99totals.zip")
urllib.urlretrieve(url00, "zbp00totals.zip")
urllib.urlretrieve(url01, "zbp01totals.zip")
urllib.urlretrieve(url02, "zbp02totals.zip")
urllib.urlretrieve(url03, "zbp03totals.zip")
urllib.urlretrieve(url04, "zbp04totals.zip")
urllib.urlretrieve(url05, "zbp05totals.zip")
urllib.urlretrieve(url06, "zbp06totals.zip")
urllib.urlretrieve(url07, "zbp07totals.zip")
urllib.urlretrieve(url08, "zbp08totals.zip")
urllib.urlretrieve(url09, "zbp09totals.zip")
urllib.urlretrieve(url10, "zbp10totals.zip")
urllib.urlretrieve(url11, "zbp11totals.zip")
urllib.urlretrieve(url12, "zbp12totals.zip")
urllib.urlretrieve(url13, "zbp13totals.zip")
urllib.urlretrieve(url14, "zbp14totals.zip")


