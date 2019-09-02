hour = input("Type the hours you worked:")
rate = input("what is your hourly rate?")
try:
    pay = float(hour) * float(rate)
    print("Your pay is", pay)
    if(pay>10):
        print("not bad!")
except Exception as e:
    print("Oops")
print("experiment git")
quit()

# testing git
