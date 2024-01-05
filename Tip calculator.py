print ("Welcome to Tip calculator")
Total_bill = float(input("What is the total bill?"))
Tip_percentage = int(input("Percentage tip?"))
Total_tip = Total_bill * (Tip_percentage/100)
Sales_tax = int(input("Sales tax percentage?"))
Total_sales_tax = Total_bill * (Sales_tax/100)
Grand_Total = Total_bill + Total_tip + Total_sales_tax

Print("Your total Bill is:", Grand_Total)
