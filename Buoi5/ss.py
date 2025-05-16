from faker import Faker
import random

fake = Faker()
def escape_single_quotes(value):
    return value.replace("'", "''") 
# Function to generate MaNV that matches the format 'Nv0[0-9][0-9]'
def generate_ma_nv(index):
    return f'Nv0{index:02d}'

# Function to generate MaDN that corresponds to MaNV
def generate_ma_dn(index):
    return f'Dn0{index:02d}'

# Function to generate a valid phone number from different networks (Viettel, Mobifone, Vinaphone)
def generate_vietnam_phone_number():
    # Define prefixes for each network
    viettel_prefixes = ['03', '09', '086']
    mobifone_prefixes = ['070', '076', '077', '078', '079']
    vinaphone_prefixes = ['081', '082', '083', '084', '085']
    
    # Randomly choose a network
    network_choice = random.choice(['Viettel', 'Mobifone', 'Vinaphone'])
    
    if network_choice == 'Viettel':
        prefix = random.choice(viettel_prefixes)
    elif network_choice == 'Mobifone':
        prefix = random.choice(mobifone_prefixes)
    else:
        prefix = random.choice(vinaphone_prefixes)
    
    return f'{prefix}{random.randint(1000000, 9999999)}'

# Mapping of streets to their corresponding districts
streets_and_districts = {
    'Đường Cao Thắng': 'Hải Châu',
    'Đường Lê Đình Lý': 'Hải Châu',
    'Đường Hùng Vương': 'Hải Châu',
    'Đường Lê Lợi': 'Hải Châu',
    'Đường 3.2': 'Hải Châu',
    'Đường Nguyễn Chí Thanh': 'Hải Châu',
    'Đường Phan Châu Trinh': 'Hải Châu',
    'Đường Tiểu La': 'Hải Châu',
    'Đường 2.9': 'Hải Châu',
    'Đường Quang Trung': 'Hải Châu',
    'Đường Đống Đa': 'Hải Châu',
    'Đường Nguyễn Du': 'Hải Châu',
    'Đường Lý Tự Trọng': 'Hải Châu',
    'Đường Hoàng Diệu': 'Hải Châu',
    'Đường Ông Ích Khiêm': 'Hải Châu',
    'Đường Nguyễn Hoàng': 'Hải Châu',
    'Đường Thái Phiên': 'Hải Châu',
    'Đường Lê Hồng Phong': 'Hải Châu',
    'Đường Hoàng Văn Thụ': 'Hải Châu',
    'Đường Yên Bái': 'Hải Châu',
    'Đường Trưng Nữ Vương': 'Hải Châu',
    'Đường Ngô Gia Tự': 'Hải Châu',
    'Đường Triệu Nữ Vương': 'Hải Châu',
    'Đường Bắc Đẩu': 'Hải Châu',
    'Đường Hải Hồ': 'Hải Châu',
    'Đường Pasteur': 'Hải Châu',
    'Đường Lê Đình Dương': 'Hải Châu',
    'Đường Nguyễn Văn Linh': 'Hải Châu',
    'Đường Lê Thanh Nghị': 'Hải Châu',
    'Đường Xô Viết Nghệ Tĩnh': 'Hải Châu',
    'Đường Trần Phú': 'Hải Châu',
    'Đường Bạch Đằng': 'Hải Châu',
    # Quận Thanh Khê
    'Đường Nguyễn Tất Thành': 'Thanh Khê',
    'Đường Thái Thị Bôi': 'Thanh Khê',
    'Đường Lê Độ': 'Thanh Khê',
    'Đường Trường Chinh': 'Thanh Khê',
    'Đường Hải Phòng': 'Thanh Khê',
    'Đường Điện Biên Phủ': 'Thanh Khê',
    'Đường Hà Huy Tập': 'Thanh Khê',
    'Đường Trần Cao Vân': 'Thanh Khê',
    'Đường Nguyễn Tri Phương': 'Thanh Khê',
    'Đường Lê Lợi': 'Thanh Khê',
    'Đường Hùng Vương': 'Thanh Khê',
    'Đường Lê Đình Lý': 'Thanh Khê',
    'Đường Duy Tân': 'Thanh Khê',
    'Đường Tiểu La': 'Thanh Khê',
    'Đường Nguyễn Phước Nguyên': 'Thanh Khê',
    'Đường Xô Viết Nghệ Tĩnh': 'Thanh Khê',
    'Đường 2.9': 'Thanh Khê',

    # Quận Liên Chiểu
    'Đường Nguyễn Lương Bằng': 'Liên Chiểu',
    'Đường Nguyễn Tất Thành': 'Liên Chiểu',
    'Đường Bàu Tràm': 'Liên Chiểu',
    'Đường Âu Cơ': 'Liên Chiểu',
    'Đường Đoàn Phú Thứ': 'Liên Chiểu',
    'Đường Nam Cao': 'Liên Chiểu',
    'Đường Lạc Long Quân': 'Liên Chiểu',
    'Đường Nguyễn Sinh Sắc': 'Liên Chiểu',
    'Đường Kinh Dương Vương': 'Liên Chiểu',
    'Đường Nguyên Chánh': 'Liên Chiểu',
    'Đường Trần Đình Tri': 'Liên Chiểu',
    'Đường Hoàng Văn Thái': 'Liên Chiểu',
    'Đường Tố Hữu': 'Liên Chiểu',
    'Đường Tôn Đức Thắng': 'Liên Chiểu',

    # Quận Sơn Trà
    'Đường Yết Kiêu': 'Sơn Trà',
    'Đường Lý Tử Tấn': 'Sơn Trà',
    'Đường Hoàng Sa': 'Sơn Trà',
    'Đường Lê Đức Thọ': 'Sơn Trà',
    'Đường Phan Bá Phiến': 'Sơn Trà',
    'Đường Trần Nhân Tông': 'Sơn Trà',
    'Đường Trương Định': 'Sơn Trà',
    'Đường Chu Huy Mân': 'Sơn Trà',
    'Đường Nại Hiên Đông': 'Sơn Trà',
    'Đường Dương Lâm': 'Sơn Trà',
    'Đường Lê Văn Duyệt': 'Sơn Trà',
    'Đường Dương Vân Nga': 'Sơn Trà',
    'Đường Lê Chân': 'Sơn Trà',
    'Đường Lý Đạo Hành': 'Sơn Trà',
    'Đường Ngô Quyền': 'Sơn Trà',
    'Đường Lê Văn Thứ': 'Sơn Trà',
    'Đường Võ Nguyên Giáp': 'Sơn Trà',
    'Đường Hồ Nghinh': 'Sơn Trà',
    'Đường Nguyễn Công Trứ': 'Sơn Trà',
    'Đường Võ Văn Kiệt': 'Sơn Trà',
    'Đường Lê Hữu Trác': 'Sơn Trà',
    'Đường Nguyễn Văn Thoại': 'Sơn Trà',
    'Đường Trần Hưng Đạo': 'Sơn Trà',
    'Đường Lê Văn Duyệt': 'Sơn Trà',

    # Quận Ngũ Hành Sơn
    'Đường Võ Nguyên Giáp': 'Ngũ Hành Sơn',
    'Đường Lê Quang Đạo': 'Ngũ Hành Sơn',
    'Đường Châu Thị Vĩnh Tế': 'Ngũ Hành Sơn',
    'Đường Phan Tứ': 'Ngũ Hành Sơn',
    'Đường Trần Văn Dư': 'Ngũ Hành Sơn',
    'Đường Hồ Xuân Hương': 'Ngũ Hành Sơn',
    'Đường Bà Huyện Thanh Quan': 'Ngũ Hành Sơn',
    'Đường Võ Như Hưng': 'Ngũ Hành Sơn',
    'Đường Hoài Thanh': 'Ngũ Hành Sơn',
    'Đường An Dương Vương': 'Ngũ Hành Sơn',
    'Đường Phạm Hữu Kính': 'Ngũ Hành Sơn',
    'Đường Lê Văn Hưu': 'Ngũ Hành Sơn',
    'Đường Hồ Huân Nghiệp': 'Ngũ Hành Sơn',
    'Đường Nguyễn Lữ': 'Ngũ Hành Sơn',
    'Đường Đoàn Khuê': 'Ngũ Hành Sơn',
    'Đường Trịnh Lỗi': 'Ngũ Hành Sơn',
    'Đường Nghiêm Xuân Yêm': 'Ngũ Hành Sơn',
    'Đường Minh Mạng': 'Ngũ Hành Sơn',
    'Đường Nguyễn Xiến': 'Ngũ Hành Sơn',
    'Đường Trường Sa': 'Ngũ Hành Sơn',
    'Đường Nguyễn Duy Trinh': 'Ngũ Hành Sơn',
    'Đường Mai Đăng Chơn': 'Ngũ Hành Sơn',
    'Đường Võ Chí Công': 'Ngũ Hành Sơn',
    'Đường Phạm Đức Nam': 'Ngũ Hành Sơn',
    'Đường Lê Quát': 'Ngũ Hành Sơn',

    # Quận Cẩm Lệ
    'Đường Trường Chinh': 'Cẩm Lệ',
    'Đường Tôn Đản': 'Cẩm Lệ',
    'Đường Lê Trọng Tấn': 'Cẩm Lệ',
    'Đường Lê Đại Hành': 'Cẩm Lệ',
    'Đường Xô Viết Nghệ Tĩnh': 'Cẩm Lệ',
    'Đường Thăng Long': 'Cẩm Lệ',
    'Đường Phạm Tứ': 'Cẩm Lệ',
    'Đường Phan Khôi': 'Cẩm Lệ',
    'Đường Lê Quang Định': 'Cẩm Lệ',
    'Đường Trần Nam Trung': 'Cẩm Lệ',
    'Đường Võ Chí Công': 'Cẩm Lệ',
}

vietnamese_surnames = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", 
    "Ngô", "Đinh", "Vũ", "Bùi", "Đặng", 
    "Hồ", "Nguyễn Văn", "Lý", "Nguyễn Thị", "Mai"
]

vietnamese_male_names = [
    "Huy", "Khang", "Bảo", "Minh", "Phúc", 
    "Anh", "Khoa", "Phát", "Đạt", "Khôi", 
    "Long", "Nam", "Duy", "Quân", "Kiệt", 
    "Thịnh", "Tuấn", "Hưng", "Hoàng", "Hiếu"
]

vietnamese_female_names = [
    "Trang", "Linh", "Phương", "Hương", "Thảo", 
    "Hà", "Huyền", "Ngọc", "Hằng", "Giang", 
    "Nhung", "Yến", "Nga", "Mai", "Thu", 
    "Hạnh", "Vân", "Hoa", "Hiền"
]
# Function to generate data for NhanVien table
def generate_nv_data(n):
    nv_data = []
    for i in range(1, n+1):
        ma_nv = generate_ma_nv(i)
        ma_dn = generate_ma_dn(i)  # MaDN corresponding to MaNV

        if random.choice([True, False]):  # Randomly choose gender
            # Male
            surname=random.choice(vietnamese_surnames)
            first_name = random.choice(vietnamese_male_names)
            # Ensure the middle name is different from the first name
            middle_name = random.choice([name for name in vietnamese_male_names if name != first_name])
        else:
            surname=random.choice(vietnamese_surnames)
            # Female
            first_name = random.choice(vietnamese_female_names)
            # Ensure the middle name is different from the first name
            middle_name = random.choice([name for name in vietnamese_female_names if name != first_name])
        
        ten_nv = f"{surname} {middle_name} {first_name}"  # Full name in the format: Họ + Tên đệm + Tên

        chuc_vu = random.choice(['Nhân viên giao hàng', 'Nhân viên thu ngân', 'Nhân viên bán hàng', 'Quản lý'])

        # Set BangCap based on ChucVu
        if chuc_vu == 'Nhân viên giao hàng':
            bang_cap = 'Bằng lái xe A4'
        elif chuc_vu == 'Nhân viên thu ngân':
            bang_cap = 'Tốt nghiệp Trung học phổ thông'
        else:
            bang_cap = random.choice(['Tốt nghiệp tiểu học', 'Cao đẳng', 'Đại học', 'Tốt nghiệp trung học cơ sở', 'Tốt nghiệp Trung học phổ thông'])

        # Generate a random address with street and corresponding district
        street = random.choice(list(streets_and_districts.keys()))
        district = streets_and_districts[street]
        dia_chi = f"{random.randint(1, 200)} {street}, Quận {district}, Đà Nẵng"

        # Generate a valid phone number from various networks
        sdt = generate_vietnam_phone_number()
        
        ngay_sinh = fake.date_of_birth(minimum_age=19, maximum_age=60).strftime('%Y-%m-%d')
        gioi_tinh = 'Nam' if ten_nv in vietnamese_male_names else 'Nữ'

        # Create SQL insert statement
        insert_statement = (
            f"INSERT INTO NhanVien (MaNV, TenNV, ChucVu, DiaChi, BangCap, SDT, MaDN, NgaySinh, GioiTinh) "
            f"VALUES ('{ma_nv}', N'{ten_nv}', N'{chuc_vu}', N'{dia_chi}', N'{bang_cap}', '{sdt}', '{ma_dn}', '{ngay_sinh}', N'{gioi_tinh}');"
        )
        nv_data.append(insert_statement)

    return nv_data

# Tạo 1000 dòng dữ liệu
generated_data = generate_nv_data(1000)

# Ghi dữ liệu SQL vào tệp nv_data.sql nếu chưa có
with open('D:/TKW/nv_data.sql', 'w', encoding='utf-8') as file:
    for statement in generated_data:
        file.write(statement + '\n')

# Kết nối đến cơ sở dữ liệu SQLite
import sqlite3
conn = sqlite3.connect('BTNHOM.db')
cursor = conn.cursor()

# Tạo bảng NhanVien nếu chưa tồn tại
cursor.execute('''
CREATE TABLE IF NOT EXISTS NhanVien
(
    MaNV CHAR(5) PRIMARY KEY,
    TenNV NVARCHAR(50) NOT NULL,
    ChucVu NVARCHAR(50),
    DiaChi NVARCHAR(100),
    BangCap NVARCHAR(50),
    SDT CHAR(10) UNIQUE,
    MaDN CHAR(5),
    NgaySinh DATE,
    GioiTinh NVARCHAR(10),

    -- Điều kiện CHECK cho MaNV theo mẫu 'Nv0%'
    CONSTRAINT CK_MaNV CHECK (MaNV LIKE 'Nv0%'),

    -- Điều kiện CHECK cho độ tuổi
    CONSTRAINT CK_Tuoi CHECK (strftime('%Y', 'now') - strftime('%Y', NgaySinh) >= 18)
);
''')

# Đọc và thực thi các câu lệnh SQL từ file nv_data.sql
with open('D:/TKW/nv_data.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

# Thực thi các câu lệnh SQL từ file
try:
    cursor.executescript(sql_script)
    print("Dữ liệu đã được thêm thành công!")
except sqlite3.Error as e:
    print(f"Lỗi khi thêm dữ liệu: {e}")

# Commit các thay đổi và đóng kết nối
conn.commit()
conn.close()
