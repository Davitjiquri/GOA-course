"""1) მომხმარებელს შემოატანინეთ ტესტში მიღებული ქულა, თუ ქულა მეტია 90 - ზე და ნაკლებია 100 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა სრულიად. თუ მიღებული ქულა მეტია 70 - ზე და  ნაკლებია 80 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით, თუ მიღებული ქულა მეტია 40 -  ზე და ნაკლებია 70 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 500 ლარტით, ხოლო თუ მიღებული ქულა ნაკლებია 40 ზე, მაგ შემტხვევაში დაპრინტეთ, ტქვენ არ დაგიფინანსდებათ სწავლის პროცესი"""

grade = int(input("enter your grade : "))


if grade >= 90 and grade<=100:
    print("Your studies will be fully funded")

elif grade >= 70 and grade <= 80:
    print("You will be financed with 1500 GEL")

elif grade >= 40 and grade <= 70:
    print("Your will be finansed 500 GEL")

if grade < 40:
    print("Your studies will not be finansed")