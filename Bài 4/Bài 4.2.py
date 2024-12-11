print("NGUYEN HONG DANG")
print("MSSV: 235752021610021")
print("#############################")
######################################​
S = input("Nhập chuỗi S: ")

# Duyệt qua từng ký tự trong chuỗi
for char in S:
    # Kiểm tra nếu ký tự không phải là dấu cách hoặc dấu tab
    if char != " " and char != "\t":
        print(char)
