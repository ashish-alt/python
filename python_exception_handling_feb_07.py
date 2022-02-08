##var=10/0
##print(var)

##try:
##    var=10/0
##    print(var)
##except:
##    print("sorry")

##try:
##    var="A"+10
##    print(var)
##except:
##    print("sorry")

##Exception - ZeroDivisionError,ArthimeticError, IndexError

##try:
##    var="A"+10
##    print(var)
##except TypeError:
##    print("welcome to error page")
##except:
##    print("sorry")


##try:
##    var="A"+10
##    print(var)
##except TypeError as ex:
##    print(ex)
##except ZeroDivisionError as ex:
##    print(ex)
##except:
##    print("sorry")

##try:
##    var="A"+10
##    print(var)
##except TypeError as ex:
##    print(ex)
##except ZeroDivisionError as ex:
##    print(ex)
##except:
##    print("sorry")

##try:
##    var ="A"+10
##    print(var)
##except Exception as ex:
##    print(ex)
##else:
##    print("india")
##finally:
##    print("welcome to family")
    
##try:
##    var = 10
##    if var > 5:
##        raise IndexError
##except IndexError:
##    print("sorry")

##try:
##    var = 10
##    if var>5:
##        raise IndexError("my own raising of the error")
##except IndexError as ex:
##    print(ex)

##try:
##    var = 10
##    if var>5:
##        raise MlabError
##except MlabError:
##    print("error and ex")

##class MlabError(Exception):
##    pass
##try:
##    var = 10
##    if var>5:
##        raise MlabError
##except MlabError:
##    print("error and ex")

##class MlabError(Exception):
##    ex_msg = "User Defined Message"
##try:
##    var = 10
##    if var>5:
##        raise MlabError
##except MlabError as ex:
##    print(ex.ex_msg)


##sqlite3 (python), mysql,oracle,mongo,psql
##sqlite3, sqlconnector, cx_oracle, pymongo,psycopg2

import sqlite3

##connection = sqlite3.connect("mlab.db")
###query = """CREATE TABLE student ("name" text, "age" integer)"""
###query = """INSERT INTO student ("name","age") values("dhoni",44)"""
##query = """ select * from student"""
##execution = connection.execute(query)
##data = execution.fetchall()
##print(data)
##connection.commit()
##connection.close()

##def My_DB_Execution(query,db):
##    connection = sqlite3.connect(db)
##    execution = connection.execute(query)
##    data = execution.fetchall()
##    print(data)
##    connection.commit()
##    connection.close()
###query = """CREATE TABLE student ("name" text, "age" integer)"""
###query = """INSERT INTO student ("name","age") values("dhoni",44)"""
##query = """ select * from student"""
##My_DB_Execution(query,"mlab.db")

##def My_DB_Execution(query,db="mlab.db"):
##    connection = sqlite3.connect(db)
##    execution = connection.execute(query)
##    data = execution.fetchall()
##    if len(data)>0:
##        return data
##    connection.commit()
##    connection.close()
###query = """CREATE TABLE student ("name" text, "age" integer)"""
##query = """INSERT INTO student ("name","age") values("dhoni",44)"""
####query = """ select * from student"""
##my_output = My_DB_Execution(query)
##if my_output != None:
##    print(my_output)


##def My_DB_Execution(query,db="mlab.db"):
##    try:
##        connection = None
##        connection = sqlite3.connect(db)
##        execution = connection.execute(query)
##        data = execution.fetchall()
##        if len(data)>0:
##            return data
##    except Exception as ex:
##        print(ex)
##    finally:
##        if connection != None:
##            connection.commit()
##            connection.close()
###query = """CREATE TABLE student ("name" text, "age" integer)"""
##query = """INSERT INTO student ("name","age") values("dhoni",44)"""
####query = """ select * from student"""
##my_output = My_DB_Execution(query)
##if my_output != None:
##    print(my_output)






















































