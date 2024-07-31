import json

class simulator_data:
    def read_json_records(file_path=r'..\raw-data\store-raw-data.json'):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for record in data:
                yield record


# from time import sleep
# # file_path = r'..\raw-data\store-raw-data.json'
# if __name__ == "__main__":
#     for record in simulator_data.read_json_records():
#         sleep(1)
#         print(record["InvoiceNumber"])

