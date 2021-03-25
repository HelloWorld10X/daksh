'''BMI CALCULATING PROGRAM'''
'''COMMAND LINE INTERACTIVE'''


weight = float(input("Write your weight in kgs here:")) #input should be in kgs
height = float(input("Write your height in cm here:"))  # input should be in cm here

metre_height = height/100    # for converting cm to metre as its necessary as its a formula

total_height = metre_height**2    # this is squaring of metre_height due to formula

BMI = weight/total_height         #FORMULA = weight/height squared

print(f"Your BMI is {BMI} and you are")


   #conditionals applied here

if BMI==18.5 or BMI<18.5:
    print(" underweight")

elif BMI>18.5 and BMI<25:
    print(" normal weighted")

elif BMI>25 and BMI<29:
    print(" overweighted ")

else:
    print(" on level of obesity consult a doctor")

'''this is for free and can be used without any credits THANK YOU'''