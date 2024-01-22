import pyodbc   


try:    
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=srvm4sql;DATABASE=RelojesITK_GCO;UID=m4prod;PWD=Obelix2014')
    print("Conexion exitosa")


except Exception as e:
    print(e)