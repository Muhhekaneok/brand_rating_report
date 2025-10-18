from data_processing import read_items_from_csv
from reports import generate_report
from tabulate import tabulate

files = ["products1.csv", "products2.csv"]

data_iter = read_items_from_csv(files)
report_data, report_headers = generate_report("average-rating", data_iter)
print(tabulate(report_data,
               headers=report_headers,
               showindex=range(1, len(report_data) + 1)))

print("*" * 10)
print(report_data, report_headers)
print(report_data)
print(report_headers)