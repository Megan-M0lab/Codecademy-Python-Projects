weight = 41.5

# Ground Shipping Cost
ground_cost = 0
if weight <= 2:
  ground_cost = (weight * 1.5) + 20
elif weight <= 6:
  ground_cost = (weight * 3) + 20
elif weight <= 10:
  ground_cost = (weight * 4) + 20
else:
  ground_cost = (weight * 4.75) + 20
print("Ground shipping cost: " + str(ground_cost))

premium_shipping_cost = 125
print("Premium ground shipping cost: " + str(premium_shipping_cost))
#Drone Shipping Cost

drone_cost = 0
if weight <= 2:
  drone_cost = (weight * 4.5)
elif weight <= 6:
  drone_cost = (weight * 9) 
elif weight <= 10:
  drone_cost = (weight * 12)
else:
  drone_cost = (weight * 14.25) 
print("Drone shipping cost: " + str(drone_cost))