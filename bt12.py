import datetime

birth_day = int(input("Nhap ngay sinh: "))
birth_month = int(input("Nhap thang sinh: "))
birth_year = int(input("Nhap nam sinh: "))

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

age_day = abs(current_day - birth_day)
age_month = abs(current_month - birth_month)
age_year = abs(current_year - birth_year)

print(f"Tuoi cua ban chinh xac la {age_year} tuoi, {age_month} thang, {age_day} ngay")
