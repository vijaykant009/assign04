"""Cloud Foundry test"""
from flask import Flask,render_template, request
import os
import pyodbc
import csv

app = Flask(__name__)

port = int(os.getenv("PORT", 5000))

@app.route('/')
def index():

    return render_template('index.html')



@app.route('/Search5', methods=['GET', 'POST'])
def Search5():

    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:azurevijaydb.database.windows.net,1433;Database=Quakes;Uid=vijaykant009@azurevijaydb;Pwd={J@ik@nt009};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = cnxn.cursor()
    cursor.execute("Select StateName,TotalPop from voting where TotalPop between '5000' and '10000'")
    row = cursor.fetchall()
    return render_template("view.html", row=row)



@app.route('/Search10', methods=['GET', 'POST'])
def Search10():
    
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:azurevijaydb.database.windows.net,1433;Database=Quakes;Uid=vijaykant009@azurevijaydb;Pwd={J@ik@nt009};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = cnxn.cursor()
    cursor.execute("Select StateName,TotalPop from voting where TotalPop between '10000' and '50000'")
    row = cursor.fetchall()
    return render_template("view.html", row=row)


# @app.route('/chart1',methods=['GET', 'POST'])
# def chart1():
# 	    #mag = request.form['mag1']
# 	    con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:azurevijaydb.database.windows.net,1433;Database=Quakes;Uid=vijaykant009@azurevijaydb;Pwd={J@ik@nt009};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# 	    query="Select Count(StateName),Registered from voting where Registered BETWEEN 2000 AND 5000"
# 	    columns=['StateName','Registered']
# 	    dic=dict()
# 	    cur=con.cursor()
# 	    mem=[]
# 	    cur.execute(query)
# 	    result=list(cur.fetchall())
# 	    for row in result:
# 	        memdict=dict()
# 	        for j,val in enumerate(row):
# 	            memdict[columns[j]]=val
# 	        mem.append(memdict)
# 	    a=[1,2,3,4,5]
# 	    return render_template('chart.html',a=mem,chart="bar")

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


@app.route('/chart5',methods=['GET', 'POST'])
def chart5():
   nvalue = int(request.form['nvalue'])
   con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:azurevijaydb.database.windows.net,1433;Database=Quakes;Uid=vijaykant009@azurevijaydb;Pwd={J@ik@nt009};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
   # a=nvalue #chnage this variable
   start=nvalue
   end=80
   age_interval=[0]
   val=start
   while val<end:
       val+=nvalue
       age_interval.append(val)
   mem=[]
   for i in range(0,len(age_interval)-1):
       #query="select (count(*)) as count from voting where age > "+str(age_interval[i])+" and age<"+str(age_interval[i+1])
       query="select count(*) as count from voting where ((voted/Totalpop)*100) >"+str(age_interval[i])+" and ((voted/Totalpop)*100)< "+str(age_interval[i+1])
       cur=con.cursor()
       cur.execute(query)
       result=list(cur.fetchall())
       vtt=str(age_interval[i])+"-"+str(age_interval[i+1])
       for row in result:
           memdict=dict()
           for j,val in enumerate(row):
               memdict["vtt"]=vtt
               memdict["States"]=val
               mem.append(memdict)
           print(mem)

   return render_template('chart2.html',a=mem,chart="pie")







port = os.getenv("PORT", 5000)

if __name__ == '__main__':
   app.run(debug="true",port=int(port))

