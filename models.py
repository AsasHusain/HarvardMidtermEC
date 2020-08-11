
import psycopg2

# create new instance

class User:
    
    username = ""
    password = ""
    
    def init(self,u,p):
        
        self.username = u
        self.password = p
        
# Create a DB class
class db:
    cur = ""
    conn = ""

    def __init__(self,server, username, password):

        self.conn = psycopg2.connect("host={} dbname=midterm_db user={} password={}".format(server,username,password))
        self.cur = self.conn.cursor()

    def add(self,user):
        
        insert_query = "INSERT INTO users VALUES (\'{}\',\'{}\')".format(user.username,user.password)
        self.cur.execute(insert_query)
        self.conn.commit()
    
    def validate(self,user):
        sel_query = "SELECT password FROM users WHERE username=\'{}\' ".format(user.username)
        self.cur.execute(sel_query)
        results = self.cur.fetchall()
        #print(results[0])
        if results[0][0] == user.password:
            return True
        else:
            return False

    
class Condo:
    database = ""

    def __init__(self,d):
        self.database = d 

    def get_total(self):
        sel_query = "SELECT * FROM condos "
        self.database.cur.execute(sel_query)
        results = self.database.cur.fetchall()
        return(len(results))

    def get_details(self,mls):
        sel_query = "SELECT * FROM condos WHERE mlsnum = {}".format(mls)
        print(sel_query)
        
        self.database.cur.execute(sel_query)
        results = self.database.cur.fetchall()
        return(results[0])
    
    



# create an init_app method; takes server, username, password and connects to DB
# create an add method that takes a user object and write the uname/password to the database table
# create a validate method that takes username/pw and compares to DB; true if correct else false

#SELECT password from users where username = 'username'
#in a row[] object; you will need to find the right field to check
#can't just compare row; it will probably be row[0][0] or something like that



# Create class Condo
