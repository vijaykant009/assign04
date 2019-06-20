"""Cloud Foundry test"""
from flask import Flask,render_template
import os
import pyodbc
import csv

app = Flask(__name__)

port = int(os.getenv("PORT", 5000))

@app.route('/')
def hello_world():
    con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:azurevijaydb.database.windows.net,1433;Database=Quakes;Uid=vijaykant009@azurevijaydb;Pwd={J@ik@nt009};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    query="Select mag,latitude from quake3 where mag >= 7"
    columns=['mag','latitude']
    dic=dict()
    cur=con.cursor()
    mem=[]
    cur.execute(query)
    result=list(cur.fetchall())
    for row in result:
        memdict=dict()
        for j,val in enumerate(row):
            memdict[columns[j]]=val
        mem.append(memdict)
    # print(mem)
    a=[1,2,3,4,5]
    # print(a)
    return render_template('chart.html',a=mem,chart="scatter")

# @app.route('/streaming.csv')
# def streaming():
#     result=[]
#     with open('streaming.csv') as csv_file:
        
#         csv_reader = csv.reader(csv_file, delimiter=',')
        
#         line_count = 0
#         for row in csv_reader:
#             result.append(row)
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(row)
#                 line_count += 1
#             print(f'Processed {line_count} lines.')
        
#     return tuple(result)



if __name__ == '__main__':
    app.run(port=port,debug=True)
