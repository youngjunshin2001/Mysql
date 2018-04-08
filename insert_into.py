#!/usr/bin/python
import psycopg2
import sys
import pprint
 
def main():
    conn_string = "host='localhost' dbname='adult_data' user='youngjun'"
    print ("Connecting to database\n    ->{}".format(conn_string))
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    print("Entering records")

    # cursor.execute("SELECT setval('id', 0)")

    # if adding more, delete this line
    cursor.execute("DELETE FROM adults;")
 
    counter = 0
    with open('data/adult.csv') as my_file:
        for line in my_file:
            counter += 1
            my_arguments = line.split(",")

            for i in range(len(my_arguments)):
                if my_arguments[i] == "?":
                    my_arguments[i] = "NULL"
                if i not in (0, 2, 4, 10, 11, 12):
                    my_arguments[i] = "'{}'".format(my_arguments[i].strip())

            my_query = "INSERT INTO adults (age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country, wage) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(*my_arguments)

            cursor.execute(my_query)

            if counter % 1000 == 0:
                print('.', end="")
                sys.stdout.flush()

    conn.commit()

    print("\nFinished!")

    
if __name__ == "__main__":
    main()
