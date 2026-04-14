#Trench crusade is a miniature skirmish game where succes rolls are made using two or more dice, where the sum of 2 dice have to equal 7 or more. With 3 dice, 3 dice are rolled, 
#and the two largest numbers are summed. 4 likewise with 4 dice. With -1 dice, 3 dice are rolled, and the two lowest numbers are summed. 

# 2 dice
#Creating a list containing all possible dicerolls with one dice. 
one_dice = []

for x in range(1,7):
    one_dice.append(x)

#creating a list, containing all possible dicerolls with two dice
two_dice = []

for x in one_dice:
    for y in range(1,7):
        two_dice.append([x,y])

#looping through the possible rolls with two dice, adding them and counting the number that are equal two or higher than 7.
total_rolls_2_dice = 0 
rolls_7_or_more_2_dice = 0

for x in two_dice:
    total_rolls_2_dice = total_rolls_2_dice + 1
    if sum(x) >= 7:
           rolls_7_or_more_2_dice = rolls_7_or_more_2_dice +  1

percentage_succes_2_dice = rolls_7_or_more_2_dice/total_rolls_2_dice

print(f'When rolling 2 dice, {rolls_7_or_more_2_dice}, out of {total_rolls_2_dice} have a sum of 7 or more, and the chance of succes = {round(percentage_succes_2_dice*100,1)}%')

# 3 dice
three_dice = []

for x in two_dice:
    for y in range(1,7):
        z = x + [y]
        three_dice.append(z)
        
        
rolls_above_7_3_dice = 0
total_rolls_3_dice = 0
        
for x in three_dice:
    z = sorted(x)
    total_rolls_3_dice = total_rolls_3_dice + 1
    if sum(z[-2:]) >= 7:
           rolls_above_7_3_dice = rolls_above_7_3_dice +  1

percentage_succes_3_dice = rolls_above_7_3_dice/total_rolls_3_dice

print(f'When rolling 3 dice, {rolls_above_7_3_dice}, out of {total_rolls_3_dice} have a sum of 7 or more, and the chance of succes = {round(percentage_succes_3_dice*100,1)}%')

# 4 dice
four_dice = []

for x in three_dice:
    for y in range(1,7):
        z = x + [y]
        four_dice.append(z)

rolls_above_7_4_dice = 0
total_rolls_4_dice = 0
        
for x in four_dice:
    z = sorted(x)
    total_rolls_4_dice = total_rolls_4_dice + 1
    if sum(z[-2:]) >= 7:
           rolls_above_7_4_dice = rolls_above_7_4_dice +  1

percentage_succes_4_dice = rolls_above_7_4_dice/total_rolls_4_dice

print(f'When rolling 4 dice, {rolls_above_7_4_dice}, out of {total_rolls_4_dice} have a sum of 7 or more, and the chance of succes = {round(percentage_succes_4_dice*100,1)}%')

# Minus 1 dice
total_rolls_minus_1_dice = 0
rolls_above_7_minus_1_dice= 0

for x in three_dice:
    z = sorted(x)
    total_rolls_minus_1_dice = total_rolls_minus_1_dice + 1
    if sum(z[0:2]) >= 7:
           rolls_above_7_minus_1_dice = rolls_above_7_minus_1_dice +  1

percentage_succes_minus_1_dice = rolls_above_7_minus_1_dice/total_rolls_minus_1_dice

print(f'When rolling -1 dice, {rolls_above_7_minus_1_dice} out of {total_rolls_minus_1_dice}, have a sum of 7 or more, and the chance of succes = {round(percentage_succes_minus_1_dice*100,1)}%')


# Minus 2 dice
total_rolls_minus_2_dice = 0
rolls_above_7_minus_2_dice= 0

for x in four_dice:
    z = sorted(x)
    total_rolls_minus_2_dice = total_rolls_minus_2_dice + 1
    if sum(z[0:2]) >= 7:
           rolls_above_7_minus_2_dice = rolls_above_7_minus_2_dice +  1

percentage_succes_minus_2_dice = rolls_above_7_minus_2_dice/total_rolls_minus_2_dice

print(f'When rolling -2 dice, {rolls_above_7_minus_2_dice} out of {total_rolls_minus_2_dice}, have a sum of 7 or more, and the chance of succes = {round(percentage_succes_minus_2_dice*100,1)}%')

