def can_vote(age, citizen, criminal_record):
    if age >= 18 and citizen and not criminal_record:
        print("Вы можете голосовать!")
    else:
        print("Вы можете голосовать!")

def get_age():
    while True:
        message = input("Введите ваш возраст: ")
        try:
            age = int(message)
            return age
        except ValueError:
            print("Введите числовое значение.")

def get_data(user_message):
    operator = input(user_message).lower()
    while operator not in ["да", "нет"]:
        print("Введен некорректный ответ")
        operator = input(user_message).lower()
    return True if operator == "да" else False

def main():
    age = get_age()
    citizen = get_data("Вы являетесь гражданином страны где сейчас находитесь (Да/Нет): ")
    criminal_record = get_data("У вас есть судимость (Да/Нет): ")
    can_vote(age, citizen, criminal_record)

main()