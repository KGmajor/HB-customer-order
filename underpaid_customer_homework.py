MELON_PRICE = 1.00

def melon_payments(payment_report):

    payment_report = open("customer-orders.txt")

    for line in payment_report:
        single_order = line.split('|')

        customer_name = single_order[1]
        melons_ordered = float(single_order[2])
        paid_price = float(single_order[3])

        true_melon_cost = melons_ordered * MELON_PRICE
        amount_owed = true_melon_cost - paid_price
        amount_due = paid_price - true_melon_cost

        if paid_price > true_melon_cost:
            print(("{} overpaid for their {} melons by ${:.2f}".format(customer_name, melons_ordered, amount_due)))

        elif paid_price < true_melon_cost:
            print("{} underpaid for their {} melons by ${:.2f}".format(customer_name, melons_ordered, amount_owed))

    payment_report.close()

melon_payments("customer-orders.txt")



