message = "Привет, я Макс"
print(message)
message = "Я з України"
print(message)

name = "Roboert"
message = f"Hello, {name} would you like to learn Python today"
print ( message)

famous_person = "Muhammed Ali"
cutata = "Если тебе снится, что ты сможешь меня побить, лучше просто проснись и извинись."
message = f"{famous_person} once said, {cutata}"
print (message)

NAME = "Chubaka"
NAME = "\n\t  " + NAME + "  \t\n"
#print(NAME)
print(NAME.lstrip())   # видалити пропуски зліва
print(NAME.rstrip())   # видалити пропуски зправа
print(NAME.strip())    # видалити пропуски с обох сторін
#Максим Литвинюк
#13.30 18.02.2023
name1 = "Max Litviniuk"
country = "Germany"
index = "59063"
town = "Hamm"
steet = "MunsterStaSSe"
number = "36"
print(name1)
print(country)
print(index)
print(town)
print(steet)
print(number)
#Програма друкуює нам Имя, Країну, Індекс, Місто, Вулицю там номер

meters = 1000

inches = meters * 39.37
feet = meters * 3.28
miles = meters * 0.00062
yards = meters * 1.09

print("Дистанція у метрах: {:.2f}".format(meters))
print("Дистанція у дюймах: {:.2f}".format(inches))
print("Дистанція у футах: {:.2f}".format(feet))
print("Дистанція у милях: {:.2f}".format(miles))
print("Дистанція у ярдах: {:.2f}".format(yards))

total_seconds = 5 * 24 * 60 * 60 + 12 * 60 * 60 + 30 * 60 + 45
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Total duration: {:>10} hours, {:>10} minutes, {:>10} seconds".format(hours, minutes, seconds))




celsius = 25.0

# перетворення в градуси Фаренгейта
fahrenheit = 32 + 9/5 * celsius
print("Температура в градусах Фаренгейта: {:^15.2f}".format(fahrenheit))

# перетворення в градуси Кельвіна
kelvin = celsius + 273.15
print("Температура в градусах Кельвіна: {:^15.2f}".format(kelvin))



num = 6259

digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10

sum_of_digits = sum([digit1, digit2, digit3, digit4])

print(f"{digit1} + {digit2} + {digit3} + {digit4} = {sum_of_digits}")



import math

lat1, lon1 = 39.9075000, 116.3972300

lat2, lon2 = 50.4546600, 30.5238000

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

distance = 6371.032 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
print("{:>10.3f}".format(distance))





