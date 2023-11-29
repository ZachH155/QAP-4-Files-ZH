#Program used to enter and calculate new insurance policy info for its customers
#Zachary Hulan
#November 18 - 24

import datetime as dt

#CON_STANTS
NEXT_POLICY_NUM = 1944
BASIC_PREMIUM = 869.00
ADDTIONAL_CAR_DIS = 0.25
EXTRA_LIABILITY_COVER = 130.00
GLASS_COVER = 86.00
LOANER_CAR_COVER = 58.00
HST = 0.15
PROCESSING_MONTHLY_FEE = 39.99

#def functions
def Discount(Value1, Value2):
    return Value1 * Value2


#lists = []

listProvince = ["NL", "ON", "QC", "NS", "NB", "MB", "BC", "PEI", "SK", "AB"]
listYesNo = ["Y", "YES", "N", "NO"]
listPayment = ["Full", "Monthly", "Down", "Down Pay"]
listClaimscost = [0]
listClaimsdate = [0]

print("------------------------------------------")

#input("")

custName = input("Customers first and last name:  ").title()
print()
custAddress = input("Customers home address:  ")
print()
custCity = input("Customers city name:  ").title()



#validation for provinces
print()
custProvince = input("Customers province name (abbreviated):  ").upper()
while True:
    if custProvince == listProvince[0]:       
        break
    elif custProvince == listProvince[1]:       
        break
    elif custProvince == listProvince[2]:      
        break
    elif custProvince == listProvince[3]:
        break
    elif custProvince == listProvince[4]:
        break
    elif custProvince == listProvince[5]:
        break
    elif custProvince == listProvince[6]:
        break
    elif custProvince == listProvince[7]:
        break
    elif custProvince == listProvince[8]:
        break
    elif custProvince == listProvince[9]:
        break
    else:
        print()
        print("INPUT VALID CANADIAN PROVINCE")
        print()
        custProvince = input("Customers province name (abbreviated):  ").upper()

print()
custPostal = input("Customers postal code:  ").upper()
print()
custPhonenum = input("Customers phone number:  ")



#validation for insured cars number
print()
try:
    insuredCars = int(input("Number of insured cars:  "))
except:
    print()
    print("ENTER A NUMBER")
    print()
    insuredCars = ""
    while True:
        if insuredCars == "":
            try:
                insuredCars = int(input("Number of insured cars:  "))
            except:
                print()
                print("ENTER A NUMBER")
                print()
            else:
                break


#validation for liability
print()
extraLiability = input("Add extra liability of up to $1,000,000? (Y/N):  ").upper()
while True:
    if extraLiability == listYesNo[0] or extraLiability == listYesNo[1]:
        extraLiability = EXTRA_LIABILITY_COVER
        break
    elif extraLiability == listYesNo[2] or extraLiability == listYesNo[3]:
        extraLiability = 0
        break
    else:
        print()
        print("INPUT Y OR N (yes or no)")
        print()
        extraLiability = input("Add extra liability of up to $1,000,000? (Y/N):  ").upper()


#validation for glass coverage
print()
glassCoverage = input("Add Glass Coverage? (Y/N):  ").upper()
while True:
    if glassCoverage == listYesNo[0] or glassCoverage == listYesNo[1]: 
        glassCoverage = GLASS_COVER
        break   
    elif glassCoverage == listYesNo[2] or glassCoverage == listYesNo[3]:
        glassCoverage = 0
        break
    else:
        print()
        print("INPUT Y OR N (yes or no)")
        print()
        glassCoverage = input("Add Glass Coverage? (Y/N):  ").upper()


#validation for loaner car
print()
loanerCar = input("Add Loaner Car? (Y/N):  ").upper()
while True:
    if loanerCar == listYesNo[0] or loanerCar == listYesNo[1]:
        loanerCar = LOANER_CAR_COVER
        break
    elif loanerCar == listYesNo[2] or loanerCar == listYesNo[3]:
        loanerCar = 0
        break
    else:
        print()
        print("INPUT Y OR N (yes or no)")
        print()
        loanerCar = input("Add Loaner Car? (Y/N):  ").upper()


#validation for payment type
print()
paymentType = input("Enter Payment Type (Full, Monthly, or Down Pay):  ").title()
downPay = ""
loopstooper = False
while loopstooper == False:
    if paymentType == listPayment[0]:
        downPay = 0
        break
    elif paymentType == listPayment[1]:
        downPay = 0
        break
    elif paymentType == listPayment[2] or paymentType == listPayment[3]:
        paymentType = "Monthly + Down Pay"

        #validation for down payment
        print()
        try:
            downPay = int(input("Enter Down Payment amount:  "))
        except:
            print()
            print("ENTER AN AMOUNT FOR THE DOWN PAYMENT")
            print()
            downPay = ""
            while loopstooper == False:
                if downPay == "":
                    try:
                        downPay = int(input("Enter Down Payment amount:  "))
                    except:
                        print()
                        print("ENTER AN AMOUNT FOR THE DOWN PAYMENT")
                        print()
                    else:
                        loopstooper = True
        else:
            loopstooper = True
    else:
        print()
        print("ENTER PAYMENT TYPE")
        print()
        paymentType = input("Enter Payment Type (Full, Monthly, or Down Pay):  ").title()


#validation for if the customer has any previous claims
print()
custClaimsdate = ""
custClaimscost = int(0)
custClaimsYN = input("Does customer have any previous claims? (Y/N):  ").upper()
while True:
    if custClaimsYN == listYesNo[0] or custClaimsYN == listYesNo[1]:

        #input for the customers previous claims
        while True:
            print()
            print("Enter date of customers previous claim")
            custClaimsdate = input('in the format of DD-MM-YY (Type "DONE" to finish):  ')
            if custClaimsdate.upper() == "DONE":
                custClaimsYN = listYesNo[2]
                break
            else: 
                print()
                custClaimscost = float(input("Enter cost of customers previous claim: "))
                listClaimsdate.append(custClaimsdate)
                listClaimscost.append(custClaimscost)

    elif custClaimsYN == listYesNo[2] or custClaimsYN == listYesNo[3]:
        break
    else:
        print()
        print("INPUT Y OR N (yes or no)")
        print()
        custClaimsYN = input("Does customer have any previous claims? (Y/N):  ").upper()



#OH BOY MATH!!!!!!

#Insurance premium calculations
if insuredCars > 1:
    additionalPremium = Discount( BASIC_PREMIUM, ADDTIONAL_CAR_DIS)
    insuredTotal = (additionalPremium * insuredCars) + BASIC_PREMIUM
else: 
    insuredTotal =  BASIC_PREMIUM

#Changes extra costs to reflect how many cars are being insured
extraLiability = extraLiability * insuredCars
glassCoverage = glassCoverage * insuredCars
loanerCar = loanerCar * insuredCars

#total insurance premium
totalInsurancepremium = insuredTotal + extraLiability + glassCoverage + loanerCar

#tax
tax = Discount(totalInsurancepremium, HST)

#total
total = totalInsurancepremium + tax

#monthly payments
monthlyPay = ((total - downPay) + PROCESSING_MONTHLY_FEE) / 8



#TEMP OUTPUT

# print(custName)
# print(custAddress)
# print(custCity)
# print(custProvince)
# print(custPostal)
# print(custPhonenum)
# print(insuredCars)
# print(extraLiability)
# print(glassCoverage)
# print(loanerCar)
# print(paymentType)
# print(downPay)
# print(custClaimsYN)
# print(custClaimsdate)
# print(custClaimscost)
# print(listClaimsdate)
# print(listClaimscost)
# print(additionalPremium)
# print(insuredTotal)
# print(totalInsurancepremium)
# print(tax)
# print(total)
# print(monthlyPay)

#grabs the date from the system
date = dt.datetime.now()
dateplus30 = date + dt.timedelta(days = 30)
dateday1 = dateplus30.replace(day = 1)

#FINAL OUTPUT
print()
print()
print(f"         1       2       3       4")
print(f"12345678901234567890123456789012345678901234")
print(f"         ONE STOP INSURANCE COMPANY")
print(f"  ________________________________________")
print()
print(f"Customer Information:")
print()
print(f"{custName}")
print(f"{custAddress} {custCity},")
print(f"{custProvince} {custPostal}")
print()
print(f"Customer Phone: {custPhonenum}")
print()
print()
print(f"  ________________________________________")
print(f"                  Costs")
extraLiabilityDsp = "${:,.2f}".format(extraLiability)
glassCoverageDsp = "${:,.2f}".format(glassCoverage)
loanerCarDsp = "${:,.2f}".format(loanerCar)
print(f"Extra Liability:                {extraLiabilityDsp:>3s}")
print(f"Glass Coverage:                 {glassCoverageDsp:>3s}")
print(f"Loaner Car Cost:                {loanerCarDsp:>3s}")
print()
print(f"                              ---------")
insuredTotalDsp = "${:,.2f}".format(insuredTotal)
print(f"Insured Cars:                       {insuredCars:>3d}")
print(f"Insured Cars Cost:            {insuredTotalDsp:>3s}")
print()
print(f"                              ---------")
totalInsurancepremiumDsp = "${:,.2f}".format(totalInsurancepremium)
taxDsp = "${:,.2f}".format(tax)
downPayDsp = "${:,.2f}".format(downPay)
totalDsp = "${:,.2f}".format(total)
monthlyPayDsp = "${:,.2f}".format(monthlyPay)
if paymentType == "Monthly":
    print(f"Payment type:                   {paymentType:>3s}")
elif paymentType == "Full":
    print(f"Payment type:                      {paymentType:>3s}")
else:
    print(f"Payment type:        {paymentType:>3s}")
print()
print(f"Total Insurance Premium:      {totalInsurancepremiumDsp:>9s}")
print(f"HST:                          {taxDsp:>9s}")
print(f"Down Payment:                 {downPayDsp:>9s}")
print(f"TOTAL:                        {totalDsp:>9s}")
print(f"                              ---------")
if paymentType != "Full":
    print(f"Monthly payment:              {monthlyPayDsp:>9s}")
else:
    print(f"Full payment:                 {monthlyPayDsp:>9s}")
print(f"First payment date:          {dateday1.strftime('%d-%m-%Y')}")
print(f"  ________________________________________")
print(f" Invoice date:               {date.strftime('%d-%m-%Y')}")
print()
if custClaimscost != "":
    print(f"  ________________________________________")
    print(f"    Claim #     Claim Date      Amount")
    print()

    #prints all of the inputted claims
    claimsNum = 0
    lengthClaimsdate = len(listClaimsdate)
    while claimsNum < lengthClaimsdate - 1:
        claimsNum = claimsNum + 1
        listClaimscostDsp = "${:,.2f}".format(listClaimscost[claimsNum])

        print(f"      {claimsNum}.         {listClaimsdate[claimsNum]}     {listClaimscostDsp:>3s}")
print()


