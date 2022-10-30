import insertUtil as ut
import psycopg2


#Tạo kết nối với RDS PostgreSQL và thêm dữ liệu vào
#Đây là phần mình chỉnh sửa (lấy thông tin từ DB mình tạo thế vào)
conn = psycopg2.connect(database='covid19_postgres', user='postgres', password='1234567890', host='database-postgres.crizlomgyz2x.us-east-1.rds.amazonaws.com', port='5432')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')