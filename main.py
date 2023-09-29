import datetime

import cv2
import numpy as np

from Person import Person
from Shift import Shift


def shift_to_link(d_day, d_month, d_year, d_start_time, d_end_time):
    start = datetime.datetime(d_year, d_month, d_day, d_start_time, 0)
    end = datetime.datetime(d_year, d_month, d_day, d_end_time, 0)
    url = "https://calendar.google.com/calendar/event?action=TEMPLATE"
    url += "&text=" + "Event"
    url += "&dates=" + start.strftime("%Y%m%dT%H%M%SZ") + "/" + end.strftime("%Y%m%dT%H%M%SZ")
    return url


def divide_to_sub_pic(from_img):
    start_height = 167
    end_height = 200
    start_width = 9
    end_width = 68

    sub_img = [[[None for _ in range(2)] for _ in range(3)] for _ in range(7)]
    for shifts in range(3):
        for days in range(7):
            # for i in range(start_height, end_height):
            #     for j in range(start_width, end_width):
            #         from_img[i][j] = (92, 193, 203)
            sub_img[days][shifts][0] = from_img[start_height:end_height, start_width: end_width, :]
            start_width += 70
            end_width += 70
        start_width = 9
        end_width = 68
        start_height += 48
        end_height += 48

    start_width = 9
    end_width = 68
    start_height = 378
    end_height = 415

    for shifts in range(3):
        for days in range(7):
            sub_img[days][shifts][1] = from_img[start_height:end_height, start_width: end_width, :]
            # for i in range(start_height, end_height):
            #     for j in range(start_width, end_width):
            #         from_img[i][j] = (92, 193, 203)
            start_width += 70
            end_width += 70
        start_width = 9
        end_width = 68
        start_height += 48
        end_height += 48

    return sub_img


sean = Person("Sean", None, None)
artyom = Person("Artyom", None, None)
yelena = Person("Yelena", None, None)
amir = Person("Amir", None, None)
daniel = Person("Daniel", None, None)
david = Person("David", None, None)
dima = Person("Dima", None, None)
denis = Person("Denis", None, None)
ivgeny = Person("Ivgeny", None, None)
tamar = Person("Tamar", None, None)
empty = Person("empty", None, None)

employees = {
    "sean": sean,  # 2 1 0
    "artyom": artyom,  # 0 1 0
    "yelena": yelena,  # 3 1 0
    "amir": amir,  # 1 0 1
    "daniel": daniel,  # 1 1 1
    "david": david,  # 0 2 0
    "denies": denis,  # 0 0 0
    "dima": dima,  # 1 0 0
    "ivgeny": ivgeny,  # 0 2 1
    "tamar": tamar  # the other one 1 1 1
}


def add_pic_to_person(array, array2, array3, array4):
    sean.pic_example = cv2.resize(array[2][1][0], (32, 24))
    artyom.pic_example = cv2.resize(array[0][1][0], (32, 24))
    yelena.pic_example = cv2.resize(array[3][1][0], (32, 24))
    amir.pic_example = cv2.resize(array[1][0][1], (32, 24))
    daniel.pic_example = cv2.resize(array[1][1][1], (32, 24))
    david.pic_example = cv2.resize(array[0][2][0], (32, 24))
    denis.pic_example = cv2.resize(array[0][0][0], (32, 24))
    dima.pic_example = cv2.resize(array[1][0][0], (32, 24))
    ivgeny.pic_example = cv2.resize(array2[1][1][0], (32, 24))
    tamar.pic_example = cv2.resize(array2[2][2][0], (32, 24))
    sean.long_shift = cv2.resize(array2[4][2][1], (32, 24))
    david.long_shift = cv2.resize(array3[1][2][1], (32, 24))
    tamar.long_shift = cv2.resize(array2[3][2][1], (32, 24))
    denis.long_shift = cv2.resize(array[2][2][1], (32, 24))
    ivgeny.long_shift = cv2.resize(array[4][2][1], (32, 24))
    amir.long_shift = cv2.resize(array4[2][2][1], (32, 24))
    empty.pic_example = cv2.resize(array[2][0][1], (32, 24))


def find_worker(employee_name):
    return employees[employee_name]


def index_to_date(t_person, t_day, t_shift, long_shift):
    today = datetime.date.today()
    if t_day != 6:
        days_until_shift = (7 - t_day) + today.weekday()
        date = today + datetime.timedelta(days=days_until_shift)
        if t_shift == 0 and long_shift:
            start_time = 6
            end_time = 18
        elif t_shift == 0:
            start_time = 6
            end_time = 14
        elif t_shift == 1:
            start_time = 14
            end_time = 22
        elif t_shift == 2 and long_shift:
            start_time = 18
            end_time = 6
        else:
            start_time = 22
            end_time = 6
        shift_info = Shift(date.year, date.month, date.day, start_time, end_time)
        t_person.shifts.append(shift_info)
        print(
            f"shift of {shift_info.day}/{shift_info.month}/{shift_info.year} between {shift_info.start_time} to "
            f"{shift_info.end_time}")
        print(shift_to_link(shift_info.day, shift_info.month, shift_info.year, shift_info.start_time, shift_info.end_time))


if __name__ == '__main__':
    name = input()
    img = cv2.imread("example2.jpeg", -1)
    tamar_pic = cv2.imread("example1.jpeg", -1)
    img2 = cv2.imread("example3.jpeg", -1)
    img3 = cv2.imread("example4.jpeg", -1)
    initial = divide_to_sub_pic(img)
    initial2 = divide_to_sub_pic(tamar_pic)
    initial3 = divide_to_sub_pic(img2)
    initial4 = divide_to_sub_pic(img3)
    add_pic_to_person(initial, initial2, initial3, initial4)
    pic = cv2.imread("example2.jpeg", -1)
    arr = divide_to_sub_pic(pic)
    person = find_worker(name)
    for day in range(7):
        for shift in range(3):
            for position in range(2):
                arr[day][shift][position] = cv2.resize(arr[day][shift][position], (32, 24))
                mse = np.mean((arr[day][shift][position] - person.pic_example) ** 2)
                mse2 = None
                if person.long_shift is not None:
                    mse2 = np.mean((arr[day][shift][position] - person.long_shift) ** 2)
                threshold = 15
                if mse < threshold or (mse2 is not None and mse2 < threshold):
                    cv2.imshow("i", arr[day][shift][position])
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    if mse2 is not None:
                        is_long_shift = True
                    else:
                        is_long_shift = False
                    index_to_date(person, day, shift, is_long_shift)
