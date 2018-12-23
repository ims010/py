import csv

data_time = []

# with open('sys.csv', 'r') as data_file:
#     csv_data = csv.reader(data_file)

#     # next(csv_data)  # to skip the first line or bad data

#     # print(list(csv_data))
#     for line in csv_data:
#         data_time.append(f"{line[0]} -> {line[19]}")  # fstrings, for string format, .format()

# for item in data_time:
#     print(item)

# ************** Using DictReader *****************************

with open('sys.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # for item in csv_data:
    #     print(item)

    # next(csv_data)  # to skip the first line or bad data

    # print(list(csv_data))
    for line in csv_data:
        data_time.append(f"{line['Date']} -> {line['% Processor Time']}")  # fstrings, for string format, .format()

for item in data_time:
    print(item)
