import csv


def get_csv_data(csv_path):
    variable_file = open(str(csv_path), "rt")
    data_set = csv.reader(variable_file)
    for row in data_set:
        column = list(i for i in row)
    columns = [column[i:i+1] for i in range(12)]
    return columns

# print(get_csv_data(os.getcwd()+'/story_id.csv'))