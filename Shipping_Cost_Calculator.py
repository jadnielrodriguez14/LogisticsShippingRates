# Shipping Cost Calculator

## Input package Weight and Shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilograms: "))

## Calculate Shippin Cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
