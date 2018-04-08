#!/usr/bin/python
import psycopg2
import sys
import pprint
 
def main():
    conn_string = "host='localhost' dbname='adult_data' user='youngjun'"
    # print the connection string we will use to connect
    print ("Connecting to database\n    ->{}".format(conn_string))
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
 
    my_query = input("sql> ")

    # execute our Query
    cursor.execute(my_query)
 
    # retrieve the records from the database
    records = cursor.fetchall()

    my_file = open("result.csv", "w")
 
    for record in records:
        my_record = list(record)
        
        for i in range(len(my_record)):
            if type(my_record[i]) == str:
                my_record[i] = my_record[i].strip()
            else:
                my_record[i] = str(my_record[i])

        my_csv_line = ",".join(my_record) + "\n"
        my_file.write(my_csv_line)

    my_file.close()

 
if __name__ == "__main__":
    main()
