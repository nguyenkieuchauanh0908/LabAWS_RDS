import insertUtil as ut
import MySQLdb


#Tạo kết nối với RDS Aurora MySQL và thêm dữ liệu vào
#Đây là phần mình chỉnh sửa từ bạn (lấy thông tin từ DB mình tạo thế vào)
conn = MySQLdb.connect(host='database-aurora.cluster-cnpnxtxbi6ci.us-east-1.rds.amazonaws.com', user='admin', passwd='1234567890', db='covid19_aurora', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')


