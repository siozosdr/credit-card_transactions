__author__ = 'sokras'
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import csv

def read_file(file):
    with open(file, 'r') as rows:  # open the file
        fields = rows.readline()
        fields = fields.split(',')
        for row in csv.reader
        return fields, lines

def process_lines(lines):
    for l in lines:
        print a
def main():
    fields, lines = read_file("subscription_report.csv")
    print fields
    for l in lines:
        print l
main()
