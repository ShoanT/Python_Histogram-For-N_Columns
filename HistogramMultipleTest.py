'''
Created on 05-Feb-2020

@author: ShoanT

Name: Taware Shon Pravin
Reg. No.: 2019MVE006
Branch: ES & VLSI
Assignment No. 5, Question: 1

'''
import csv
import matplotlib.pyplot as plt

'''
Reading Data from CSV file
Sample CSV file attached
No. of columns in the data/csv file can be changed

'''
with open('test.csv', mode='r') as csv_file:
    
    csv_content = csv.DictReader(csv_file)
    
    col_name = csv_content.fieldnames
    a={} #array for storing data read w.r.t. header with header names
    h=[] #array for storing data w.r.t header without header names

    
    for row in csv_content: #Reading data from CSV file and storing in array
        for header, value in row.items():
            temp = float(value)
            try:
                a[header].append(temp)
            except KeyError:
                a[header] = [temp]
                
                
    for col in col_name:#Storing data without header name
        try:
            h.append(a[col])
        except KeyError:
            h = [a[col]]

    

    plt.hist(h, bins=10) #bins is the number of division on x-axis
    plt.ylabel("Frequency")
    plt.xlabel("Elements")
    plt.legend(col_name)
    plt.title("Histogram Representation")
    plt.show()  
