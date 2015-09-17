from generate import *
import random
import csv

generator = SpecificCurve(0, 2.0, 70.0)
data = generator.generate_data(200)

csvfile = file("csv_test.csv", "wb")
writer = csv.writer(csvfile)
writer.writerows(data)
