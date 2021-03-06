#!/usr/bin/env python
# coding: utf-8

# In[25]:


import config
import json
import requests
api_key = config.API_key
import time 
import datetime
import mysql.connector
from mysql.connector import errorcode
import pandas as pd



# In[26]:

#creates connection, all functions will start by calling this
def connect():
    global cnx
    cnx = mysql.connector.connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = 'mushroom')
    global cursor
    cursor = cnx.cursor()


# In[9]:
#two functions used to create a new db

#sub_table function
def sub_db_create(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def create_db(db_name):
    global cnx
    cnx = mysql.connector.connect(
    host = config.host,
    user = config.user,
    passwd = config.password)
    global cursor
    cursor = cnx.cursor()
    try:
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            sub_db_create(cursor, db_name)
            print("Database {} created successfully.".format(db_name))
            cnx.database = db_name
        else:
            print(err)
            exit(1)
    cursor.close()
    cnx.close()



#pass in a SELECT * FROM colleges and it returns results in a pandas dataframe
def query(query_string):
    connect()
    cursor = cnx.cursor()
    
    cursor.execute(query_string)
    results = cursor.fetchall()
    #close out db connection
    cursor.close()
    cnx.close()
    return results


#pass in a SELECT * FROM colleges and it returns results in a pandas dataframe
def query_to_df(query_string):
    connect()
    cursor = cnx.cursor()
    
    cursor.execute(query_string)
    
    df = pd.DataFrame(cursor.fetchall())
    df.columns = [x[0] for x in cursor.description]
    
    cursor.close()
    cnx.close()
    return df

#pass in a create table statement will, if table does not exist it will be created
def create_table(query):
    connect()
    
    try:
        print("Creating a new table")
        cursor.execute(query)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

    cursor.close()
    cnx.close()
    
#takes a list of tuples and adds them to the db    
def db_insert(tuple_list):
    connect()
    insert_statement = """INSERT IGNORE INTO wiki_mush(
                    name,
                    hymeniumType,
                    capShape,
                    whichGills,
                    stipeCharacter,
                    sporePrintColor,
                    ecologicalType,
                    howEdible)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.executemany(insert_statement, tuple_list)
    cnx.commit()
    cursor.close()
    cnx.close()
    
#takes results_dict and converts to list of tuples then inserts into the db
def mush_to_tup(results_dict):
    list_of_tuples = []
    for i in results_dict:
        temp_tuple = ()
        temp_tuple = (i['name'],
              i['hymeniumType'],
              i['capShape'],
              i['whichGills'],
              i['stipeCharacter'],
              i['sporePrintColor'],
              i['ecologicalType'],
              i['howEdible'])
        list_of_tuples.append(temp_tuple)
    db_insert(list_of_tuples)
