# name = input("Enter your name:")
# print("Hello " + name)

# friends = ["Steven", "Hannes", "Aleks", "Kyle", "Struan", "Jan"]

# print(friends)

# fav_friend = input("Who is your favourite friend?")

# print(friends[fav_friend])

# def say_hi(name):
#    print("hello " + name)
# say_hi("Marlon")

# def cube(num):
#    return num*num*num
# result = cube(4)
# print(result)

#is_male = False
#is_tall = False

#if is_male and is_tall:
 #   print("You are a tall male")
#elif is_male and not is_tall:
 #   print("You are a short male")
#elif not is_male and is_tall:
 #   print("You are a tall female")
#else:
 #   print("you are neither tall or not a male")

#def max_num(num1, num2, num3):
 #   if num1 >= num2 and num1 >= num3:
  #      return num1
   # elif num2 >= num1 and num2 >= num3:
   #     return num2
   # else:
   #     return num3

#print(max_num(3,4,5))

#num1 = float(input("Enter the first number: "))
#op = input("Enter the operator: ")
#num2 = float(input("Enter the second number: "))

#if op == "+":
#    print(num1+num2)
#elif op == "-":
#    print(num1-num2)
#elif op == "*":
#    print(num1*num2)
#elif op == "/":
#    print(num1/num2)
#elif op == "^":
#    print(num1**num2)
#else:
#    print("Invalid operator!") #test comment

#monthConversions = {
 #   "Jan": "January",
#    "Feb": "February",
    #"Mar": "March",
   # "Apr": "April",
  #  "May": "May",
 #   "Jun": "June",
#    "Jul": "July",
    #"Aug": "August",
   # "Sep": "September",
  #  "Oct": "October",
 #   "Nov": "November",
#    "Dec": "December",
#}
#
#print(monthConversions.get("test", "Not a valid key"))

#i = 1
#while i <= 10:
 #   print(i)
#    i = i+1 # A shorthand to write this is "i += 1"
#
#print("Done with loop")

#secret_word = "Turing"
#guess_word = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess_word != secret_word and not (out_of_guesses):
#    if guess_count < guess_limit:
#        guess_word = input("Who is the Father of AI?: Alan ...")
#        guess_count += 1
 #        #print("That is not the correct :)") #This will print even if we enter the correct word. How to fix?
 #   else:
 #       out_of_guesses = True

#if out_of_guesses:
 #   print("You lose!")

# else:
   # print("You did it! The father of AI is Alan " +secret_word)

#for letter in "Marlon's Project":
#    print(letter)

friends = ["Jim", "Sarah", "Mike"]

#for friend in friends:
  #  print(friend)

#for index in range(len(friends)): #Another way of indexing friends list
  #  print(friends[index]) #See above

#for index in range(5): #Using a range of numbers from 0 to 5
 #   if index == 0:
 #       print("First iteration")
#    else:
 #       print("Not first iteration")

def raise_to_power(base_num, power_num): #this is a function "raise_to_power", base_num & power_num are the parameters
    result = 1 #variable, assigned a value of 1
    for index in range(power_num): #start of a for loop, named "index"
        result = result*base_num
    return result

print(raise_to_power(3,1)) #here you are calling the function "raise_to_power", and you are assigning a base number and power to it
