# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:56:36 2020

@author: Hamoon
"""
import pymysql.cursors
def load_data():
    """load data from sql server"""
    db = pymysql.connect('localhost', 'root', '', 'corona')
    cursor = db.cursor()  
    sql = 'select * from tweets where lang = "en"'
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

    except:
        print("unable to fetch data")
        
    db.close()
    
    data = []
    for i in range(len(results)):
        data.append(results[i][1])
    return data
