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

# This function calculates and prints all the shipping costs
def main():
    admin_fee = 5.99

    UK_shipping = carrier_cost_UK(admin_fee)
    EUR_shipping_less = carrier_cost_EUR_less(admin_fee)
    EUR_shipping_more = carrier_cost_EUR_more(admin_fee)
    ROW_shipping_less = carrier_cost_ROW_less(admin_fee)
    ROW_shipping_more = carrier_cost_ROW_more(admin_fee)

    print(f"The admin fee is {admin_fee}, below is the transit cost included")
    print(f"- UK {UK_shipping}")
    print(f"- European shipment, weighing less than 18kg {EUR_shipping_less}")
    print(f"- European shipment, weighing more than 18kg {EUR_shipping_more}")
    print(f"- ROW shipment, weighing less than 18kg {ROW_shipping_less}")
    print(f"- ROW shipment, weighing more than 18kg {ROW_shipping_more}")

# Ensure this is the main entry point of the program
if __name__ == "__main__":
    main()
