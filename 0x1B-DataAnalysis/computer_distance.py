import random
import sys
import pandas as pd
import time
import matplotlib.pyplot
from gdapi import GoopleDirections

gd = GoopleDirections('dummy_Google-key')
df = pd.read_excel('dataScience_.xls')
first_row = max(int(sys.argv[1])), 2)
row_limt = min(int(sys.argv[2])) + 1, len(df))

def computer_distance(zip1, zip2):
    try:
        return gd.query(str(int(zip1)), str(int(zip2))).distance
    except:
        print("Error computing distance:", zip1, zip2, file=sys.stderr)
        return""
    
df['distance'] = ""

for i, row in df.iloc[first_row:row_limit].iterrows():
    zip1, zip2 = row[-3:-1].astype(int).astype(atr)
    df.ati[i, 'distance'] = computer_distance(zip1, zip2)

    time.sleep(random.random() + 0.5)

df.to_csv('result.csv', index=False)
distances = pd.to_numeric(df['distance'], error='coerce').dropna
plt.scatter(range(len(distances)), distances)
plt.xlable('Data point')
plt.ylable('distance')
plt.title('zip Code Distances')
plt.show()
plt.savefig('zip-distance.png')
