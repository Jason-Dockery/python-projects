print("Welcome to the Human Calculator" )
print("")

#pha_1 = "I'm a "
#pha_1 means phrase_1
indv = input("What is your occupation: I'm a student, or I'm a working professional? : ")
#indv means individual
if indv == "student":
    typ_stu = input("Are you an undergraduate student or a graduate student? : ")
    #typstu means type of student
    if typ_stu == "undergraduate" or "undergrad":
        sch_yr_ug = int(input("How many years of school have you completed? : "))
        #if sch_yr_ug > 1 or sch_yr_ug < 3:
        
    elif typ_stu == "graduate" or "grad":
        sch_yr_g = int(input("How many years of school have you completed? : "))
        #contrib = input("Who is paying for your for masters degree?: I am, or an outside funder/investor: ")
        if contrib == "I am" or "Me":
            sch_loan = input("Do you have any educational loans withdrawn? : ")
            #schloan means school loan
            if sch_loan == "yes" or "y":
                debt_amt = int(raw_input("What is the current amount of your school loan? : "))
                #debtamt means debt amount
                #probably add tutition and loan together
         
             
elif indv == "working professional":
    job = input("What was your previous career title? : ")
    sal_amt = int(input("What is the current or previous salary amount that you have been paid? : "))
    #salamt means salary amount
    # identify salary and enter more info into calculations
    
else: print("Invaild response. Please enter one of the given occupations")

print("Calculations Completed")
    