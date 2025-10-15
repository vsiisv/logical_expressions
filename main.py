def can_vote(age, citizen, criminal_record):
    if age >= 18 and citizen and not criminal_record:
        print("You can vote!")
    else:
        print("You can't vote!")

age = 18
citizen = True
criminal_record = False

can_vote(age, citizen, criminal_record)