#!/usr/bin/python
import psycopg2
import sys
import pprint
import csv
 
def main():
	read_file = open('data/adult.csv', 'r')
	write_file = open('data/adult1.csv', 'w')

	for line in read_file:
		write_file.write(line.strip('"'))

	read_file.close()
	write_file.close()

 
if __name__ == "__main__":
	main()
