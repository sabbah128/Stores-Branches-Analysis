import json
from time import sleep


file_path = r'D:\Stores-Branches-Analysis\raw-data\store-raw-data.json'
# file_path = r'.\raw-data\store-raw-data.json'

def read_json_records(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for record in data:
            yield record

if __name__ == "__main__":
    for record in read_json_records(file_path):
        sleep(1)
        print(record)

