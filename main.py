
'''An unknown number of freinds go to the restaurant together. They eat and drink exactly the same amount. 
 Finally, the bill arrives. The total amount is written on the bill. 
Every person has random amounts of money. Each one pays this random amount of money until the total is satisfied. 
The app should calculate how much money each person paid too much or too little with respect to the average amount.   '''

#1.they eat and drink exactly same amount
#2 one of the main input to the app is total amount
#3.Every person pays a random amount. No one pays so much that the restaurant ends up with more money than the total.
#People could either owe some money or be owed some money



print("Welcome To Manage Your Money App ")

# take user input for total amount and number of people
while True:
    try:
        total_amount = float(input("Enter the total amount of the Bill: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        number_of_people = int(input("Enter the total number of people: "))
        if number_of_people <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")


amount_paid = []


# calculate total amount paid and the average amount
total_paid = sum(amount_paid)
average_paid = total_paid / number_of_people

# ask each person how much they paid and then append the list
for i in range(number_of_people):
    while True:
        try:
            amount = float(input("Enter the amount paid by person " + str(i + 1) + ": €"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    amount_paid.append(amount)
  
# calculate total amount paid and the average amount
total_paid = sum(amount_paid)
average_paid = total_paid / number_of_people

# check if the total amount paid matches the bill
if total_paid != total_amount:
    print("Error: The total amount paid does not match the bill.")

else: 
# create a list to store the differences between each person's payment and the average payment

 difference = []


# calculate the difference for each person and append it to the list
for i in range(number_of_people):
    diff = amount_paid[i] - average_paid
    difference.append(diff)


# show who paid less, who paid the exact amount, and who paid more
for i in range(number_of_people):
    if difference[i] > 0:
        print("Person {} paid €{:.2f} too much.".format(i + 1, difference[i]))
    elif difference[i] < 0:
        print("Person {} paid €{:.2f} too little.".format(i + 1, -difference[i]))
    else:
        print("Person {} paid the exact amount.".format(i + 1))


                