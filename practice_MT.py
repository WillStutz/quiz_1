import csv

infile = open('VendorList.csv','r')
csvfile = csv.reader(infile)
next(csvfile)

customer = {}

for x in csvfile:
    customer[x[1] + ' ' + x[2]] = {'Email':x[4],'Phone':x[5]}


print(customer)

outfile = open('practice.csv','w')
writer = csv.writer(outfile)

writer.writerow(['Name','Email','Phone'])

for record in customer:
    writer.writerow([record,customer[record]['Email'],customer[record]['Phone']])

outfile.close()