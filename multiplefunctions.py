class multiplefunctions():
     def SubFields():
         print("Subfields in AI are:")
         print("Machine Learning")
         print("Neural Networks")
         print("Vision")
         print("Robotics")
         print("Speech Processing")
         print("Natural Language Processing")
             
     def OddEven():
         num=int(input("Enter the number"))
         if(num%2==1):
             print(num ,"is a Odd Number")
         else:
             print(num ,"is a Even number")
            
     def Elegible():
         Gender=input("Enter the Gender")
         age=int(input("Enter the age"))
         if(Gender=="Male" and age >=21):
             print("ELIGIBLE")
         else:
             print("NOT ELIGIBLE")
                
     def percentage():
         Subject1=98
         Subject2=87
         Subject3=95
         Subject4=95
         Subject5=93
         Total=Subject1+Subject2+Subject3+Subject4+Subject5
         Percentage=Total/5
         print("Subject1=",Subject1)
         print("Subject2=",Subject2)
         print("Subject3=",Subject3)
         print("Subject4=",Subject4)
         print("Subject5=",Subject5)
         print("Total=",Total)
         print(f"Percentage={Percentage:.14f}")
         
     def triangle():
         Height=32
         Breadth=34
         print("Height:",Height)
         print("Breadth:",Breadth)
         print("Area Formula:(Height*Breadth)/2")
         Area=Height*Breadth/2
         print("Area of Triangle :",Area)
         Height1=2
         Height2=4
         Breadth=4
         print("Height1:",Height1)
         print("Height2:",Height2)
         print("Breadth:",Breadth)
         print("Perimeter formula=Height1+Height2+Breadth")
         Perimeter=Height1+Height2+Breadth
         print("Perimeter of triangle:",Perimeter)
            
