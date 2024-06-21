import csv
import string

input_file = open('russia-ukraine.csv', 'r')
output_file = open('russia-ukraineclean.csv', 'w')
data = csv.reader(input_file)
writer = csv.writer(output_file)
specials = ["'", "/", '"']

for line in data:
    for special in specials:
        line = [value.replace(special, '') for value in line]
    writer.writerow(line)

input_file.close()
output_file.close() 