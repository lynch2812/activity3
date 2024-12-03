# imports 
import test_exchange

def convert_usd_to_eur(amount):
    return amount * test_exchange.USD_TO_EUR

def convert_usd_to_gbp(amount):
    return amount * test_exchange.USD_TO_GBP

def convert_usd_to_jpy(amount):
    return amount * test_exchange.USD_TO_JPY

def main():
    usd_amount = 100
    
    eur_amount = convert_usd_to_eur(usd_amount)
    gbp_amount = convert_usd_to_gbp(usd_amount)
    jpy_amount = convert_usd_to_jpy(usd_amount)
    
    print(f"USD {usd_amount} is equal to:")
    print(f"- EUR {eur_amount}")
    print(f"- GBP {gbp_amount}")
    print(f"- JPY {jpy_amount}")

if __name__ == "__main__":
    main()

# importing courier cost of courier and adding the cost to the price per country it is being sent to creating the 
# amount that the cost would be added with the shipping 
import test_exchange

def carrier_cost_UK(cost):
    return cost + test_exchange.UK_to_UK

def carrier_cost_EUR_less(cost):
    return cost + test_exchange.UK_to_EUR_less_than

def carrier_cost_EUR_more(cost):
    return cost + test_exchange.UK_to_EUR_more_than

def carrier_cost_ROW_less(cost):
    return cost + test_exchange.UK_to_ROW_less_than

def carrier_cost_ROW_more(cost):
    return cost + test_exchange.UK_to_ROW_more_than
# below creates the admin fee charge as a variable and 
def main():
    admin_fee = 5.99


    UK_shipping = carrier_cost_UK(admin_fee)
    EUR_shipping_less = carrier_cost_EUR_less(admin_fee)
    EUR_shipping_more = carrier_cost_EUR_more(admin_fee)
    ROW_shipping_less = carrier_cost_ROW_less(admin_fee)
    ROW_shipping_more = carrier_cost_ROW_more(admin_fee)



    print(f"The admin fee is {admin_fee}, below is the transit cost included")
    print(f"- UK {UK_shipping}")
    print(f"- European shipment,  weighing less than 18kg {EUR_shipping_less}")
    print(f"- European shipment,  weighing more than 18kg {EUR_shipping_more}")
    print(f"- ROW shipment, weighing less then 18kg {ROW_shipping_less}")
    print(f"- ROW shipment, weighing more then 18kg {ROW_shipping_more}")
    

    if __name__ == "__main__":
      main()