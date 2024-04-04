"""მოსწავლეს შემოატანინეთ სკოლის ტესტში მიღებული ნიშანი, თუ ეს მიღებული ნიშანი უდრის 10 - ს, მაგ შემთხვევაში მასწავლებელმა, მშობელთან შეაქოს მოსწავლე, თუ მიღებული ნიშანი უდრის 8 -ს ან 9 - ს, მაგ შემთხვევაში, მასწავლებელმა, მშობელს პატარა შენიშვნა მისცეს. თუ მიღებული ქულა უდრის 5  - ს მაგ შემთხვევაში, მასწავლებელმა, მშობელს მისცეს შენიშვნა, ხოლო თუ მიღებული ნიშანი ნაკლებია 5 ზე, მაგ შემთხვევაში, მასწავლებელმა გააგდოს მოსწავლე სკოლიდან"""

grade = int (input("enter your grade"))

if grade == 10:
    print("Your child is a genious")

elif grade == 8 or grade == 9:
    print("Your child is smart but sometime they zome out")

elif grade == 5:
    print("Your child doesn't listen at all")

if grade < 5:
    print("Your child has been expelled")