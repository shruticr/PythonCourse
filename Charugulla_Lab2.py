# This program calculates the amount of ingredients needed
# when the number of cookies is defined.

# Create named constants for the ingredients
RECIPE_SUGAR = 1.5
RECIPE_BUTTER = 1
RECIPE_FLOUR = 2.75

# Create a variable for number of cookies made from the recipe
recipeCookieNumber = 48

# Get the user's total number of cookies
userCookieNumber = float(input("Enter Number of Cookies:"))

# Calculate the expected cups of sugar
expectedCupsOfSugar = (userCookieNumber/recipeCookieNumber) * RECIPE_SUGAR

# Calculate the expected cups of butter
expectedCupsOfButter = (userCookieNumber/recipeCookieNumber) * RECIPE_BUTTER

# Calculate the expected cups of flour
expectedCupsOfFlour = (userCookieNumber/recipeCookieNumber) * RECIPE_FLOUR

# Display the amount of ingredients with cups rounded to 2 decimal places
print ("For " + str(userCookieNumber) + " cookies, you will need " + \
       format(expectedCupsOfSugar, ".2f")+" cups of sugar, " + \
       format(expectedCupsOfButter, ".2f") + " cups of butter, " + \
       format(expectedCupsOfFlour, ".2f") + " cups of flour.")
