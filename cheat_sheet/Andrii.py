# region important
from typing import Any

# print(a := int(input("Enter any number:")), "\n", type(a))
# -------------------------------
# from typing import Any

# base = 5
# power = 3
#
# print(pow(base, power))
# -----------------------------

# print(a := 1_000_000)
# --------------------------------

# input_str = input("Enter any number:")
# input_int = int(input_str)
#
# print(input_int)
#
# print(type(input_int))
# ----------------------------------------------

# endregion

# `todo: region important and endregion

# a = float(input("Enter number:"))
# b = float(input("Enter number:"))
# pow_result = pow(a, b)
#
#
# print(pow_result, type(pow_result))

# ---------------------------------------------
#
# import math
#
# number = 32.655
# floored_number = math.floor(number)
# print(floored_number)

# -------------------------------------

#
# long_int = 1_000_000_000
#
# print(long_int)
#
# ------------------------------------

# ___floating-point numbers___

# average_price = 17.25

# print(average_price)  # 17.25

# print(dir(float), "\n", type(average_price))
# ==================================================

# ____конвертація чисел _________________________
# str_a = 14.5
# a_fast = int(str_a)
#
# print((a_fast), type(a_fast))  # 14 <class 'int'>
#
#
# str_b = "14.5"
# b_fast = float(str_b)
#
# print((b_fast), type(b_fast))  # 14.5 <class 'float'>

# ________округлення чисел________

# average_price = 17.25

# print((round(average_price)), type(average_price))  # 17 <class 'float'>
# print(
#     int(average_price), type(average_price), type(round(average_price))
# )  # 17 <class 'float'> <class 'int'>


# rate = 0.78

# print(round(rate))
# print(type(round(rate)))
# ==============================================================================

# -----------Комплексні числа--------------------
#
# complex_a = 3 + 5j
# complex_b = 4 + 7j
#
# summa = complex_a + complex_b
#
# print(summa, type(summa))  # (7+12j) <class 'complex'>

# =============================================================

# -------------Логічні значення----------------------
#
# is_authorized = True
# print(is_authorized)
#
# print(100 > 24)
# print(-5 >= 25)
# print(100 == 100)
# # print(100 === 100)  # немає такого оператору ===
#
# print("Long string" > "Long")
#
#
# print([1, 2, 3] == [1, 2, 3]) #True
# ===============================================================

# # ------------Конвертація в логічне значення----------
#
# db_is_available = False
#
# print(db_is_available, type(db_is_available))  #False <class 'bool'>
#
# #змінимо значення зміни "db_is_available" на False
# db_is_available = True
#
# print(db_is_available, type(db_is_available))  # True <class 'bool'>

# ---------------------------------Example--------------------------------
#
# print(bool(10))  # True
# print(bool(0))  # False
# print(bool("abc"))  # True
# print(bool([]))  # False
# print(bool([1, 2, 3]))  # True
# print(bool(None))  # False
# ===============================================================================

# ----------------------------Конвертація типів-----------------------

# "10" + 2  Помилка
# 5 + "10"  Помилка

# print(5 + int("10"))  #15
# print("Hell" + str("0"))  #Hell0


# bool_value = False
# int_value = 7
# print(bool_value + int_value)  # False=7, True=8
# print(int_value + bool_value)  # False=7, True=8

# -------------------Магічні оператори--------------------------
# int_num = 5
# float_num = 4.5
#
# print(int_num + float_num)  # 9
# print(int_num.__add__(float_num))  # NotImplemented
#
# print(float_num + int_num)  # 9.5
# print(float_num.__radd__(int_num))  # 9.5
# # ----------------------------------------------------------------
#
#
# int_num = 50
# float_num = 7.5
#
# print(int_num * float_num)  # 375.0
#
# print(int_num.__mul__(float_num))  # NotImplemented
#
# print(float_num.__rmul__(int_num))
#
# # ________________________ Магічні методи ____________________________
#
# print(str.__doc__)
# print(bool.__doc__)
# print(int.__doc__II)
# print(float.__doc__)
# # ----------------------------------------------------------------
#
# my_list: list[Any] = []
# print(help(list.__eq__))  # type: ignore    # Отримати допомогу щодо опису магічного методу класу


# # (пояснення щодо коду вище --
# # Пропозиція змінити my_list = [] на my_list: list[Any] = [] є рекомендацією
# додати явну інформацію про тип змінної.


# my_list: list[int] = []  # — список цілих чисел.
# my_list: list[str] = [] — список рядків.
# my_list: list[float] = [] — список чисел з плавающою крапкою.
#
#
# # =================================================================
# c = 256
# z = 256
#
# print(c is z)

# --------------------------------------------------------------
# 1234557