# https://github.com/asalnorouzzade/Practice-32-Price-Calculator.git
def price(cost, rate=0.1):
    return cost * (1 + rate)

def main():
    cost_input = input()
    cost = float(cost_input)
    raw = input()
    
    if raw == "":
        final_cost = price(cost)
      
    else:
        rate = float(raw)
        final_cost = price(cost, rate)
    print(final_cost)

main()
