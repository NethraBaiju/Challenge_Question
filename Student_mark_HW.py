sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 74
sub5 = 88

Total_Marks = sub1+sub2+sub3+sub4+sub5
print("Total Marks = ",sub1+sub2+sub3+sub4+sub5,"/ 500")

Percentage = Total_Marks/5
print("Percentage = ",Percentage,"%")

if Percentage > 100:
    print("Incorrect Value")

elif Percentage >= 90 and Percentage <= 100:
    print("Grade = A+")
    print(" Passed ")

elif Percentage >= 80 and Percentage <= 90:
    print("Grade = A")
    print(" Passed ")

elif Percentage >= 70 and Percentage <= 80:
    print("Grade = B")
    print(" Passed ")

elif Percentage >= 60 and Percentage <= 70:
    print("Grade = C")
    print(" Passed ")

elif Percentage >= 50 and Percentage <= 60:
    print("Grade = D")
    print(" Passed ")

else:
    print("Grade = F")
    print(" FAILED ")
