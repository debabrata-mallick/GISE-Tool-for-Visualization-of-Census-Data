import psycopg2
import psycopg2.extras
from matplotlib import pyplot as plt
import numpy as np

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '12345'
port_id = 5432

values_x=[]
values_y=[]

try:
    with psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            print('Executing the command')

            # cur.execute('SELECT * FROM public."Taluka Lavel Total"')
            # cur.execute('SELECT * FROM public."Taluka Lavel Rural"')
            # cur.execute('SELECT * FROM public."Taluka Lavel Urban"')

            # cur.execute('SELECT * FROM public."SC Taluka Lavel Total"')
            # cur.execute('SELECT * FROM public."SC  Taluka Lavel Rural Remove 0 Value Row"')
            # cur.execute('SELECT * FROM public."SC Taluka Lavel Urban Remove 0 Value Row"')

            # cur.execute('SELECT * FROM public."ST Taluka Lavel Total"')
            # cur.execute('SELECT * FROM public."ST Taluka Lavel Rural Remove 0 Value Row"')
            cur.execute('SELECT * FROM public."ST Taluka Lavel Urban Remove 0 Value Row"')


            for record in cur.fetchall():
                values_x.append(record['hh_tot_g'])
            print('Executed the command')
except Exception as error:
    print(error)



#print([i for i in range(1,100,4)])
a = np.array(values_x)
fig, ax = plt.subplots(figsize =(10, 7))
arr=ax.hist(a, bins = [i for i in range(1,100,5)],alpha=0.9, color='g', label='mag of g',histtype='bar',ec='black')
plt.xticks([i for i in range(1,100,5)])
my_bins=[i for i in range(1,100,5)]
print(len(arr[0]))
for i in range(len(arr[0])):
    plt.text(arr[1][i],arr[0][i],str(arr[0][i]))

# Add title and axis names
plt.title('Percentage of Good condition houses among ST Taluka Lavel Urban houses')
plt.xlabel('Percentage of Good Condition Houses')
plt.ylabel('Count of Taluka')

plt.show()
