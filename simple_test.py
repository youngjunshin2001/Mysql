#!/usr/bin/python
import psycopg2
import sys
import pprint
import csv
 
def main():
	with open('select.py', 'r') as my_file:
		for line in my_file:
			print(line, end="")

 
if __name__ == "__main__":
	main()
