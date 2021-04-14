import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-5NGP8N8;"
                      "Database=SalesBotPOC;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()