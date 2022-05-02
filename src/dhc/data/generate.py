import os.path
import pandas as pd
import multiprocessing
import time
from dhc.data.random_data import RandomData
from dhc.data.template_data import TemplateData

randomData = RandomData()
cols = ['code', 'description', 'name', 'meta_data',
                                   'price', 'lat', 'lng', 'created_at', 'updated_at', 'status']


def generate_data(index):
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
    data = TemplateData(code=code, description=description, name=name, meta_data=meta_data,
                        price=price, lat=lat, lng=lng, created_at=created_at, updated_at=updated_at, status=status)
    return data.to_dict()


def generate_dataset():
    print('Init words')
    randomData.init_words()
    time.sleep(3)
    print('Start pools')
    pool = multiprocessing.Pool(processes=4)
    count = 10
    outputs_async = pool.map_async(generate_data, [i for i in range(0, count)])
    outputs = outputs_async.get()
    print("Output - dict:")
    print("- Count: {}".format(len(outputs)))

    if os.path.isfile('data.csv'):
        existing_df = pd.read_csv('data.csv', sep=',', encoding='utf-8')
        existing_df = existing_df.drop(existing_df.columns[0], axis = 1)
    else:
        existing_df = pd.DataFrame(columns=cols)
    new_df = pd.DataFrame(outputs, columns=cols, index=range(len(existing_df), len(existing_df) + len(outputs) ))
    df = pd.concat([existing_df, new_df], ignore_index=True)


    print("Data Table:")
    print("- Count: {}".format(len(df)))
    df.to_csv('data.csv', sep=',', encoding='utf-8')
