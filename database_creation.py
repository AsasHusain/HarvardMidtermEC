import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=midterm_db user=postgres password=admin")
cur = conn.cursor()


with open('C:\\Users\\asash\\Desktop\\Midterm_Working_Files\\static\\data\\midterm.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(spamreader)
    cur.execute("DELETE FROM condos WHERE 1=1;")
    for row in spamreader:
        row[10] = row[10].replace("\'","`")
        insert_query = "INSERT INTO condos VALUES ({},{},{},{},'{}',{},{},{},{},\'{}\',{})".format\
                       (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        cur.execute(insert_query)
        #print(insert_query)
    conn.commit()
