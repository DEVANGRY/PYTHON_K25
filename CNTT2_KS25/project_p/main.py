from tabulate import tabulate
from datetime import datetime
from service import handle_calc_avg,display_list_student
import service.student_service
print(handle_calc_avg())
print(display_list_student(1))
print(service.student_service.display_list_student(1))

attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)},
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]

print(tabulate(attendance_book,headers= "keys" , tablefmt="grid"))

print((datetime.strptime("8:30","%H:%M") - datetime.strptime("10:00","%H:%M")).total_seconds())
