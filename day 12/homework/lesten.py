"""შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს, იქამდე უნდა შეეკითხოს სანამ პაროლი სწორი არ იქნება."""
passworld = 1
user_passworld = int(input())
while passworld != user_passworld:
    user_passworld = int(input())