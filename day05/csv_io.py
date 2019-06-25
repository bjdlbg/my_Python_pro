
import csv
try:
    with open("python.csv","r",encoding="utf8") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row[1])
except FileNotFoundError as error:
    print(error)
#
# try:
#
#     with open("python.csv","w",newline="") as f2:
#         csv_writer=csv.writer(f2)
#         csv_writer.writerow(["id","name","age"])
#         csv_writer.writerow([6,"����",22])
#         csv_writer.writerow([7,"����",21])
#         csv_writer.writerow([8,"�������",20])
# except Exception as e:
#     print(e)