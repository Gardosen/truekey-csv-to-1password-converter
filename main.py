import csv
import os
import sys


def convert_csv(index_mapper_list, file_data, delimiter=','):
    converted_file = open(os.path.join(os.getcwd(), file_data+'-export.csv'), mode='w')
    converted_file_writer = csv.writer(converted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    f = open(os.path.join(os.getcwd(), file_data))
    csvFile = csv.DictReader(f, delimiter=delimiter)
    converted_file_writer.writerow(['title', 'website', 'username', 'password'])
    for row in csvFile:
        converted_file_writer.writerow([row[index_mapper_list.get('title')], row[index_mapper_list.get('website')],
                                        row[index_mapper_list.get('username')], row[index_mapper_list.get('password')]])


if __name__ == '__main__':
    true_key_row_to_1_password_mapper = {"title": "name", "website": "url", "username": "login", "password": "password"}

    convert_csv(true_key_row_to_1_password_mapper, sys.argv[1])


