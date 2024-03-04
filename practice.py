import psycopg2
import psycopg2.extras

hostname='localhost'
database='newdb'
username='postgres'
pwd='Tanzo@9830055804'
port_id = 5432
try:
	conn= psycopg2.connect(host=hostname,dbname=database,user=username,password=pwd,port=port_id)

	print("Connection is established")
	cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	cur.execute('drop table if exists employee')

	create_script='''create table if not exists employee(
				id int primary key,
		 		name varchar(40) not null,
		 		salary int,
				dept_id varchar(30))'''

	cur.execute(create_script)

	insert_script='insert into employee values(%s,%s,%s,%s)'
	insert_values=[(1,'James',1200,'D1'),(2,'Robin',1500,"D3"),(3,'Xavier',2000,'D2')]
	for record in insert_values:
		cur.execute(insert_script, record)

	cur.execute('Select * from employee')
	for record in cur.fetchall():
		#print(record[1],record[2])
		#print(record)
		print(record['name'],record['salary']) #possible because cursor is dict cursor

	update_script = 'update employee set salary = salary + (salary*0.5)'
	cur.execute(update_script)

	cur.execute('Select * from employee')

	for record in cur.fetchall():
		print(record['name'],record['salary']) 



	cur.execute('''SELECT jsonb_path_query_array(details, '$.store.book[*].author') 
			AS all_authors FROM pathex''')
	print(cur.fetchall())
	conn.commit()
except Exception as error:
	print(error)

finally:
	conn.close()

	print("Connect is closed")

