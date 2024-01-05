print ("Welcome to Tip calcilator")
Total_bill = float(input("What is the total bill?"))
Tip_percentage = int("Percentage tip?")
Total_tip = Total_bill * (Tip_percentage/100)
Sales_tax = int("Sales tax percentage?")
Total_sales_tax = Total_bill * (Sales_tax/100)
Grand_Total = Total_bill + Total_tip + Total_sales_tax

Print("Your total Bill is:", Grand_Total)