print ("Puriwat Tatana") #Prepared by Puriwat
print ("*——————————*")
sn = (input("Enter Name:")) # input student name
sc = int(input("Enter Score:")) # input student score

score = sc

if (score == 100):
  grade = "Grade : A+"
elif ((score >= 80) and (score < 100)):
  grade = "Grade : A"
elif ((score >= 70) and (score < 80)):
  grade = "Grade : B"
elif ((score >= 60) and (score < 70)):
  grade = "Grade : C"
elif ((score >= 50) and (score < 60)):
  grade = "Grade : D"
elif ((score >= 0) and (score < 49)):
  grade = "Grade : F"
else:
  grade = "Grade : No Grade"

print ("*——————————*")
print (sn) 
print (grade)
print ("*——————————*")
