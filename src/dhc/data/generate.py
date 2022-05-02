
from asyncio import wait_for
import pandas as pd
import multiprocessing
import time
from dhc.data.random_data import RandomData
from dhc.data.template_data import TemplateData

randomData = RandomData()

def generate_data(index):
  id = randomData.get_id()
  created_at = randomData.get_date()
  updated_at = randomData.get_date()
  name = randomData.get_name()
  description = randomData.get_desc(seed=5)
  meta_data = randomData.get_desc(seed=6)
  price = randomData.get_price()
  lat = randomData.get_lag()
  lng = randomData.get_lng()
  code = '-'.join(randomData.get_str(k=4, ntokens=5))
  status = randomData.get_status()
  data = TemplateData(id=id, code=code, description=description,name=name, meta_data=meta_data, price=price, lat=lat, lng=lng, created_at=created_at, updated_at=updated_at, status=status)
  return data.to_dict()

def generate_dataset():
  print('Init words')
  randomData.init_words()
  time.sleep(3)
  print('Start pools')
  pool = multiprocessing.Pool(processes=4)
  count = 100000
  outputs_async = pool.map_async(generate_data, [i for i in range(0, count)])
  outputs = outputs_async.get()
  print("Output - dict:")
  print("- Count: {}".format(len(outputs)))
  df = pd.DataFrame(outputs)
  print("Data Table:")
  print("- Count: {}".format(len(df)))
  # print(df)
  df.to_csv('data.csv', sep=',', encoding='utf-8')
