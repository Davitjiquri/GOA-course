"""for loop დახმარებით ეცადეთ, რომ სიტყვა დაპრინტოთ საპირისპირო მიმართულებით (სცადეთ და თუ არ გამოგივათ არაუშავს. )"""

world = 'akul'
reversed_world = ''
for i in world:
    reversed_world = i + reversed_world
    print(reversed_world)