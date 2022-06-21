# #SELECT * FROM public."Taluka Lavel Total"


# import psycopg2
# import psycopg2.extras
# from matplotlib import pyplot as plt
# import numpy as np
# #import seaborn as sb
# #import seaborn as sns

# hostname = 'localhost'
# database = 'demo'
# username = 'postgres'
# pwd = '12345'
# port_id = 5432

# values_x=[]
# values_y=[]

# values_xx=[]
# values_yy=[]

# values_xxx=[]
# values_yyy=[]

# try:
#     with psycopg2.connect(
#         host = hostname,
#         dbname = database,
#         user = username,
#         password = pwd,
#         port = port_id) as conn:
#         with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#             print('Executing the command')
#             cur.execute('SELECT * FROM public."Taluka Lavel Total"')
#             for record in cur.fetchall():
#                 values_x.append(record['hh_tot_tot'])
#                 values_y.append(record['hh_tot_g'])
#             print('Executed the command')

#             cur.execute('SELECT * FROM public."ST Taluka Lavel Total"')
#             for record in cur.fetchall():
#                 values_xx.append(record['hh_tot_tot'])
#                 values_yy.append(record['hh_tot_g'])
#             print('Executed the command')

#             cur.execute('SELECT * FROM public."SC Taluka Lavel Total"')
#             for record in cur.fetchall():
#                 values_xxx.append(record['hh_tot_tot'])
#                 values_yyy.append(record['hh_tot_g'])
#             print('Executed the command')

# except Exception as error:
#     print(error)

# plt.scatter(values_x, values_y, color = 'red')
# plt.scatter(values_xx, values_yy, color = 'Green')
# plt.scatter(values_xxx, values_yyy, color = 'Yellow')


# # Add title and axis names
# plt.title('Number of households with condition of census house as total as good vs Number of households with condition of census house as total as total')
# plt.xlabel('Number of households with condition of census house as total as good')
# plt.ylabel('Number of households with condition of census house as total as total')

# plt.legend(["General Population", "ST Population", "SC Population"])


# plt.show()




#SELECT * FROM public."Taluka Lavel Total"


import psycopg2
import psycopg2.extras
from matplotlib import pyplot as plt
import numpy as np
#import seaborn as sb
#import seaborn as sns

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '12345'
port_id = 5432

values_x=[]
values_y=[]

values_xx=[]
values_yy=[]

values_xxx=[]
values_yyy=[]

try:
    with psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('SELECT * FROM public."Taluka Lavel Total"')
            for record in cur.fetchall():
                # values_x.append(record['hh_tot_tot'])
                values_x.append(record['mslit_kero'])


            # cur.execute('SELECT * FROM public."SC Taluka Lavel Total"')
            # for record in cur.fetchall():
            #     # values_xxx.append(record['hh_tot_tot'])
            #     values_yyy.append(record['hh_tot_l'])

            cur.execute('SELECT * FROM public."ST Taluka Lavel Rural"')
            for record in cur.fetchall():
                # values_xx.append(record['hh_tot_tot'])
                values_yy.append(record['mslit_kero'])

            cur.execute('SELECT * FROM public."ST Taluka Lavel Urban"')
            for record in cur.fetchall():
                # values_xxx.append(record['hh_tot_tot'])
                values_y.append(record['mslit_kero'])

except Exception as error:
    print(error)

# plt.scatter(values_x, values_y, color = 'red')
plt.scatter(values_x, values_y, color = 'red')
plt.scatter(values_x, values_yy, color = 'Green')
# plt.scatter(values_x, values_yyy, color = 'yellow')


# Add title and axis names
# plt.suptitle('Taluka Wise', y=1.05, fontsize=18)
plt.title('Number of households main source of lighting electricity (Maharastra taluka wise)')

plt.xlabel('General Population main source of lighting electricity')
plt.ylabel('ST Rural & Urban main source of lighting electricity')

plt.legend(["Urban", "Rural"])

xpoints = ypoints = plt.xlim()
# print(xpoints)
plt.plot((0,100), (0,100))


#plt.xlim(0, 100)
#plt.ylim(0, 100)
plt.show()