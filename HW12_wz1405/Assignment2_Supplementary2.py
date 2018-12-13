
import glob
from functools import reduce
from sklearn.cluster import KMeans

import datetime as dt  
import io 
import os

# import geopandas as gpd

# import math
# from math import cos, log
import pylab as pl
import numpy as np
import pandas as pd


puidata= os.getenv("PUIDATA")
if puidata is None:
    os.environ["PUIDATA"] = "%s/PUIdata"%os.getenv("HOME")
    
try:
    import ipywidgets as widgets
    hasWidgets = True
except ImportError:
    hasWidgets = False

import urllib.request as url


try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if os.getenv ('PUIDATA') is None:
    print ("Must set env variable PUIdata")

df94 = pd.read_csv(os.getenv("PUIDATA") + "/zbp94totals.txt")
df95 = pd.read_csv(os.getenv("PUIDATA") + "/zbp95totals.txt")
df96 = pd.read_csv(os.getenv("PUIDATA") + "/zbp96totals.txt")
df97 = pd.read_csv(os.getenv("PUIDATA") + "/zbp97totals.txt")
df98 = pd.read_csv(os.getenv("PUIDATA") + "/zbp98totals.txt")
df99 = pd.read_csv(os.getenv("PUIDATA") + "/zbp99totals.txt")
df00 = pd.read_csv(os.getenv("PUIDATA") + "/zbp00totals.txt")
df01 = pd.read_csv(os.getenv("PUIDATA") + "/zbp01totals.txt")
df02 = pd.read_csv(os.getenv("PUIDATA") + "/zbp02totals.txt")
df03 = pd.read_csv(os.getenv("PUIDATA") + "/zbp03totals.txt")
df04 = pd.read_csv(os.getenv("PUIDATA") + "/zbp04totals.txt")
df05 = pd.read_csv(os.getenv("PUIDATA") + "/zbp05totals.txt")
df06 = pd.read_csv(os.getenv("PUIDATA") + "/zbp06totals.txt")
df07 = pd.read_csv(os.getenv("PUIDATA") + "/zbp07totals.txt")
df08 = pd.read_csv(os.getenv("PUIDATA") + "/zbp08totals.txt")
df09 = pd.read_csv(os.getenv("PUIDATA") + "/zbp09totals.txt")
df10 = pd.read_csv(os.getenv("PUIDATA") + "/zbp10totals.txt")
df11 = pd.read_csv(os.getenv("PUIDATA") + "/zbp11totals.txt")
df12 = pd.read_csv(os.getenv("PUIDATA") + "/zbp12totals.txt")
df13 = pd.read_csv(os.getenv("PUIDATA") + "/zbp13totals.txt")
df14 = pd.read_csv(os.getenv("PUIDATA") + "/zbp14totals.txt")

df941 = df94.rename(columns={'est':'est94'})
df951 = df95.rename(columns={'est':'est95'}) 
df961 = df96.rename(columns={'est':'est96'})
df971 = df97.rename(columns={'est':'est97'})
df981 = df98.rename(columns={'EST':'est98','ZIP':'zip'})
df991 = df99.rename(columns={'EST':'est99','ZIP':'zip'})
df001 = df00.rename(columns={'EST':'est00','ZIP':'zip'})
df011 = df01.rename(columns={'EST':'est01','ZIP':'zip'})
df021 = df02.rename(columns={'EST':'est02','ZIP':'zip'})
df031 = df03.rename(columns={'est':'est03','ZIP':'zip'})
df041 = df04.rename(columns={'est':'est04','ZIP':'zip'})
df051 = df05.rename(columns={'est':'est05','ZIP':'zip'})
df061 = df06.rename(columns={'est':'est06'})
df071 = df07.rename(columns={'est':'est07'})
df081 = df08.rename(columns={'est':'est08'})
df091 = df09.rename(columns={'est':'est09'})
df101 = df10.rename(columns={'est':'est10'})
df111 = df11.rename(columns={'est':'est11'})
df121 = df12.rename(columns={'est':'est12'})
df131 = df13.rename(columns={'est':'est13'})
df141 = df14.rename(columns={'est':'est14'})

df942 = df941[['zip','est94']]
df952 = df951[['zip','est95']]
df962 = df961[['zip','est96']]
df972 = df971[['zip','est97']]
df982 = df981[['zip','est98']]
df992 = df991[['zip','est99']]
df002 = df001[['zip','est00']]
df012 = df011[['zip','est01']]
df022 = df021[['zip','est02']]
df032 = df031[['zip','est03']]
df042 = df041[['zip','est04']]
df052 = df051[['zip','est05']]
df062 = df061[['zip','est06']]
df072 = df071[['zip','est07']]
df082 = df081[['zip','est08']]
df092 = df091[['zip','est09']]
df102 = df101[['zip','est10']]
df112 = df111[['zip','est11']]
df122 = df121[['zip','est12']]
df132 = df131[['zip','est13']]
df142 = df141[['zip','est14']]