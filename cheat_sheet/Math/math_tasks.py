#
# -------------------------  ЗАВДАННЯ - 1 (площі та периметра прямокутника)  ---------------------------
# region important

# Завдання 1: Обчислення площі та периметра прямокутника
# Напиши програму, яка:
#
# Запитує у користувача довжину та ширину прямокутника.
#
# Обчислює площу прямокутника за формулою:
# Площа = довжина * ширина
#
# Обчислює периметр прямокутника за формулою:
# Периметр = 2 * (довжина + ширина)
#
# Виводить результати на екран.

# ----------------------  РІШЕННЯ  -------------------------------------

# Запитуємо довжину і ширину
# length = int(input('Довжина прямокутника: - '))
# width = int(input('Ширина прямокутника: - '))
#
# # Обчислюємо площу прямокутника
# area_rect = length * width
#
# # Обчислюємо периметр прямокутника
# perimeter_rect = 2 * (length + width)
#
#
# print(f'Площа прямокутника: - {area_rect}')
# print(f'Периметр прямокутника: - {perimeter_rect}')

# endregion

# -------------------------  ЗАВДАННЯ - 2 (конвертація температури) ---------------------------

# region important

# Завдання 2: Конвертація температури
# Напиши програму, яка:
#
# Запитує у користувача температуру в градусах Цельсія.
#
# Конвертує її у градуси Фаренгейта за формулою:
# Фаренгейт = (Цельсій * 9/5) + 32
#
# Виводить результат на екран.

# --------------------------  РІШЕННЯ  ---------------------------------------------------

# temperature_cels = float(input('Введіть значення температури у Цельсіях: - '))
#
# # Конвертуємо у градуси за Фаренгейтом
# temperature_far = round(temperature_cels * 9 / 5 + 32)
#
# print(f'Температура у Фаренгейтах: - {temperature_far}')

# endregion

# -------------------------  ЗАВДАННЯ - 3 (Розрахунок часу подорожі) ---------------------------

# region important

# Завдання 3: Розрахунок часу подорожі
# Напиши програму, яка:
#
# Запитує у користувача відстань (у кілометрах) та середню швидкість (у км/год).
#
# Обчислює час подорожі за формулою:
# Час = відстань / швидкість
#
# Виводить результат у годинах та хвилинах (наприклад, 2.5 години = 2 години 30 хвилин).

# --------------------------  РІШЕННЯ  ---------------------------------------------------

# distance = float(input('Введіть відстань у км: - '))
# speed = float(input('Введіть середню швидкість (у км/год): - '))
#
# time = distance / speed
#
# # Перетворюємо час у години та хвилини
# hours = int(time)  # Отримуємо цілу частину (години)
# minutes = int((time - hours) * 60)  # Перетворюємо дробову частину у хвилини
#
# print(f'Час подорожі: - {hours} годин {minutes} хвилин')

# Підсумок-1:

# int() — найпростіший і найпоширеніший спосіб отримати цілу частину числа.
#
# math.floor() — корисний, якщо потрібно явно вказати округлення вниз.
#
# // — швидкий спосіб, але повертає число у форматі float.
#
# math.trunc() — відкидає дробову частину незалежно від знаку числа.
#
# round() — округлює число до найближчого цілого.
# Використовуй, якщо потрібно округлити число, а не просто відкинути дробову частину.

# Підсумок-2:
# round() використовуй, коли потрібно округлити число до найближчого цілого
# або до певної кількості знаків після коми.
#
# Для відкидання дробової частини краще використовувати
# int(), math.floor() або math.trunc().

# endregion


# -------------------------  ЗАВДАННЯ - 4 (Середнє значення та сума чисел) ---------------------------

# region important

# Завдання-4: Середнє значення та сума чисел
# Напиши програму, яка:
#
# Запитує у користувача три числа (не використовуючи списки).
#
# Обчислює суму цих чисел.
#
# Обчислює середнє значення цих чисел.
#
# Виводить результат у форматі:
#
# Copy
# Сума чисел: <сума>
# Середнє значення: <середнє>

# --------------------------  РІШЕННЯ  ---------------------------------------------------

# # Константа для кількості чисел
# NUM_COUNT = 3
#
# # Запитуємо у користувача три числа
# try:
#     num1 = float(input('Введіть перше число: - '))
#     num2 = float(input('Введіть друге число: - '))
#     num3 = float(input('Введіть третє число: - '))
# except ValueError:
#     print("Будь ласка, введіть коректні числа.")
#     exit()
#
# # Обчислюємо суму та середнє значення
# sum_nums = round(num1 + num2 + num3, 2)
# average_value = round(sum_nums / NUM_COUNT, 2)
#
# # Виводимо результати
# print(f'Сума чисел: - {sum_nums}, Середнє значення чисел: - {average_value}')
#
# endregion


# -------------------------  ЗАВДАННЯ - 5 (Площа прямокутника) ---------------------------

# region important

while True:
    try:
        # Запитуємо у користувача довжину та ширину прямокутника
        length = float(input('Введіть довжину: - '))
        width = float(input('Введіть ширину: - '))

        # Якщо введені дані коректні, виходимо з циклу
        break
    except ValueError:
        # Якщо виникла помилка, повідомляємо користувача
        print('Будь ласка, введіть коректні числа. Спробуйте ще раз.')


# Обчислюємо площу та периметр прямокутника
area_rectangle = round(length * width, 2)
perimeter_rectangle = round(2 * (length + width), 2)

# Виводимо результати
print(f'Площа прямокутника: {area_rectangle}')
print(f'Периметр прямокутника: {perimeter_rectangle}')
#

# endregion

# -------------------------  ЗАВДАННЯ - 6 (середнє арифметичне трьох чисел) ---------------------------

#  region important

# Задача:
# Напиши програму, яка обчислює середнє арифметичне трьох чисел. Користувач повинен ввести три числа, а програма має вивести результат у вигляді:
#
# Copy
# Середнє арифметичних чисел [число1], [число2], [число3] дорівнює [результат].

# --------------------------  РІШЕННЯ  ---------------------------------------------------

while True:

    try:
        a = float(input('Введіть число 1: - '))
        b = float(input('Введіть число 2: - '))
        break
    except ValueError:
        print(input('помилка'))
c = a + b
print(c)

#  endregion

# *--------------------------------------
word = 'Hello'
num = 9
flt = 8.2
logic = True
fun = 2j + 1
lst = [2, 3, 4]
tpl = (5, 6, 7)
plenty = {8, 9, 10}
dt = {'key': 'value'}

[print(type(i)) for i in [word, num, flt, logic, fun, lst, tpl, plenty, dt]]
