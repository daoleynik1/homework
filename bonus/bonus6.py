m = int(input("pls enter your weight in kilograms "))
h = int(input("pls enter your height in santimetres "))
index = round(m*100/h**2, 1)
print("\n")
if index <= 15:
        print("Very severely underweight")
        
elif index <= 16:
        print("Severely underweight")
        
elif index <= 18.5:
        print ("Underweight")
        
elif index <= 25:
        print ("Normal")
        
elif index >= 30:
        print ("Overweight")
        
elif index >= 35:
        print ("Obese Class I (Moderately obese)")
        
elif index >= 35.9:
        print ("Obese Class II (Severely obese)")
        
elif index >= 40:
        print ("Obese Class III (Very severely obese)")
