
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi=weight/height**2
b= float("{:.2f}".format(bmi))
if b<18.5:
  print(f"Your BMI is {b}. You are underwait!")
elif 18.5<b<25:
  print(f"Your BMI is {b}. Your weight is normal!")
elif 25<b<30:
  print(f"Your BMI is {b}. You are slightly overweight!")
elif 30<b<35:
  print(f"Your BMI is {b}. You are obese!")
else:
  print(f"Your BMI is {b}. You are clinically obese!" )
