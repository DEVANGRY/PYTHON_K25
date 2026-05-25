branch_count = int(input("Nhập s lượng chi nhánh: "))
month_count = 3

text = ""

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        text += f"Chi nhánh {branch}, tháng {month}: {revenue} trieu đông \n"

print(text)