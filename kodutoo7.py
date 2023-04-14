# Model input
model1 = "Toyota"
model2 = "BMW"
model3 = "Audi"
model4 = "Rolls Royce"
model5 = "Tesla"

# Model 1 Toyota prices
model1_dayprice = 12
toyota_insurance = 3
toyota_disount = 0.1

# Model 2 BMW prices
model2_dayprice = 17
bmw_insurance = 5
bmw_disount = 0.12

# Model 3 Audi prices
model3_dayprice = 19
audi_insurance = 5
audi_disount = 0.15

# Model 4 Rolls Royce prices
model4_dayprice = 70
rolls_royce_insurance = 30
rolls_royce_disount = 0.03

# Model 5Tesla prices
model5_dayprice = 35
tesla_insurance = 15
tesla_disount = 0.2


# PROGRAMME START #
# Welcome message
print("Welcome to our car rental service!")
print("You can choose among several models, as: Toyota, BMW, Audi, Rolls Royce and Tesla")

model = input("What model do You want to rent? ")
days = int(input("For how many days? "))

if days >= 3:
    if model == model1:
        modelrent_price_day = model1_dayprice
        modelrent_price = model1_dayprice * days
        insurance = toyota_insurance
        insurance_price = toyota_insurance * days
        discount = toyota_disount
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", modelrent_price_day, "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", insurance, "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
    elif model == model2:
        modelrent_price_day = model2_dayprice
        modelrent_price = model2_dayprice * days
        insurance = bmw_insurance
        insurance_price = bmw_insurance * days
        discount = bmw_disount
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", modelrent_price_day, "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", insurance, "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
    elif model == model3:
        modelrent_price_day = model3_dayprice
        modelrent_price = model3_dayprice * days
        insurance = audi_insurance
        insurance_price = audi_insurance * days
        discount = audi_disount
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", modelrent_price_day, "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", insurance, "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
    elif model == model4:
        modelrent_price_day = model4_dayprice
        modelrent_price = model4_dayprice * days
        insurance = rolls_royce_insurance
        insurance_price = rolls_royce_insurance * days
        discount = rolls_royce_disount
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", modelrent_price_day, "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", insurance, "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
    elif model == model5:
        modelrent_price_day = model5_dayprice
        modelrent_price = model5_dayprice * days
        insurance = tesla_insurance
        insurance_price = tesla_insurance * days
        discount = tesla_disount
        total_price = modelrent_price + insurance_price
        rental_price_discount = (modelrent_price - (modelrent_price * discount))
        discount_price_for_rental = rental_price_discount + insurance_price
        print("Renting a", model, "for", days, "days will cost", discount_price_for_rental, "euros")
        print(discount_price_for_rental, "€ is the price, because",
              model, "costs", modelrent_price_day, "€ per day (", modelrent_price,
              "€ total ), but since its over 3 days we need to apply discount (",
              modelrent_price, "*", discount, "). \nSo its", rental_price_discount, "euros",
              "Now we need to add insurance (", insurance, "euros * ", days, "=", insurance_price,
              "). So in total", modelrent_price, "+", insurance_price, "=", discount_price_for_rental), "euros."
if days < 3:
    if model == model1:
        modelrent_price_day = model1_dayprice
        modelrent_price = model1_dayprice * days
        insurance = toyota_insurance
        insurance_price = toyota_insurance * days
        total_price = modelrent_price + insurance_price
        print("Your rental price is", total_price, "euros")
        print(total_price, "€ is the price, because", model, "costs", modelrent_price_day, "€ per day (",
              modelrent_price,
              "€ for", days, "days ) and insurance is ", insurance, "€ per day (", insurance_price,
              "€ for", days, "days ) so in total", modelrent_price, "+", insurance_price, "=", total_price)
    elif model == model2:
        modelrent_price_day = model2_dayprice
        modelrent_price = model2_dayprice * days
        insurance = bmw_insurance
        insurance_price = bmw_insurance * days
        total_price = modelrent_price + insurance_price
        print("Your rental price is", total_price, "euros")
        print(total_price, "€ is the price, because", model, "costs", modelrent_price_day, "€ per day (",
              modelrent_price,
              "€ for", days, "days ) and insurance is ", insurance, "€ per day (", insurance_price,
              "€ for", days, "days ) so in total", modelrent_price, "+", insurance_price, "=", total_price)
    elif model == model3:
        modelrent_price_day = model3_dayprice
        modelrent_price = model3_dayprice * days
        insurance = audi_insurance
        insurance_price = audi_insurance * days
        total_price = modelrent_price + insurance_price
        print("Your rental price is", total_price, "euros")
        print(total_price, "€ is the price, because", model, "costs", modelrent_price_day, "€ per day (",
              modelrent_price,
              "€ for", days, "days ) and insurance is ", insurance, "€ per day (", insurance_price,
              "€ for", days, "days ) so in total", modelrent_price, "+", insurance_price, "=", total_price)
    elif model == model4:
        modelrent_price_day = model4_dayprice
        modelrent_price = model4_dayprice * days
        insurance = rolls_royce_insurance
        insurance_price = rolls_royce_insurance * days
        total_price = modelrent_price + insurance_price
        print("Your rental price is", total_price, "euros")
        print(total_price, "€ is the price, because", model, "costs", modelrent_price_day, "€ per day (",
              modelrent_price,
              "€ for", days, "days ) and insurance is ", insurance, "€ per day (", insurance_price,
              "€ for", days, "days ) so in total", modelrent_price, "+", insurance_price, "=", total_price)
    elif model == model5:
        modelrent_price_day = model5_dayprice
        modelrent_price = model5_dayprice * days
        insurance = tesla_insurance
        insurance_price = tesla_insurance * days
        total_price = modelrent_price + insurance_price
        print("Your rental price is", total_price, "euros")
        print(total_price, "€ is the price, because", model, "costs", modelrent_price_day, "€ per day (", modelrent_price,
          "€ for", days, "days ) and insurance is ", insurance, "€ per day (", insurance_price,
          "€ for", days, "days ) so in total", modelrent_price, "+", insurance_price, "=", total_price)