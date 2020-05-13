class Customer:
    def __init__(self):
        self.customer_name = None
        self.customer_bill = None
    
    def purchases(self):
        discounted_amount=self.bill_amount-self.bill_amount*0.05
        self.pays_bill(discounted_amount)
    
    def pays_bill(self,amount):
        print(self.customer_name," pays bill amount of Rs",amount)

c1 = Customer()
c1.purchases()


class Customer:
    
    def __init__(self):
        self.customer_name="Omkar"
        self.bill_amount=0
        
    def pays_bill(self, amount):
        print(self.customer_name+" pays bill amount of Rs. "+ str(amount))
        
    def purchases(self):
        self.bill_amount=200
        pay_bill=self.bill_amount*0.95
        self.pays_bill(pay_bill)
         
c1 = Customer()
c1.purchases()