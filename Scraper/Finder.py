from selenium import webdriver

import time


def create_url(model, size):
    # Set the lowest shoe size to look at to be a Men's size 6.5
    start_size = 580

    # Take whatever size the user inputs and subtract 6.5 to help generate size code
    shoe_size_code = size - 6.5

    # Multiply the size code by 20 because Adidas increases the value for each whole size by 20
    shoe_size_code = shoe_size_code * 20

    # Add this size code to the start size to create a code for any sized shoe
    temp = start_size + shoe_size_code

    # Convert this value into an integer
    shoe_size_code = int(temp)

    # Create the URL
    url = 'http://www.adidas.com/us/' + str(model) + '_' + str(shoe_size_code) + '.html?forceSelSize=' + str(model) + \
          '_' + str(shoe_size_code)

    return url

# Testing the create_url method
# model = input("Model # ")
#
# size = input("Size ")
#
# new_url = create_url(model, float(size))
#
# print(new_url)

# Base url: black ultraboosts in a size 6.5


path = "C:\Python27\selenium\geckodriver"
driver = webdriver.Firefox(path)

url = 'http://www.adidas.com/us/ultraboost-shoes/BB6166_580.html?forceSelSize=BB6166_580'
driver.get(url)

# Opens the size dropdown box and opens the list of all sizes
sizeBox = driver.find_element_by_class_name('col-s-9')
sizeBox.click()

# Finds all of the ordered list items on the page which includes all of the shoe sizes
sizeList = sizeBox.find_elements_by_tag_name('li')

# Boolean associated with shoe size availability
isAvailable = False

# Prints all of the shoe sizes
for i in sizeList:
    # ignores unneeded white space
    if i.text != '':
        print(i.text)

    # This code will be used to click on the user's desired shoe size
    # 7 is just a placeholder size
    if i.text == '7':
        isAvailable = True
        i.click()

        # Once the size is selected don't need to continue to search
        break

if not isAvailable:
    print('The size you have selected is unavailable.')
    exit(0)


# Add the shoe to the user's cart
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div/div[5]/form/div[4]/button').click()

# Need this delay to give the page enough time to load the checkout overlay
time.sleep(1)

checkoutPopup = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/main')

if checkoutPopup.is_displayed():
    print('displayed')
else:
    print('invisible')

# Finds all of the links on the checkout overlay
# Options: View Bag and Checkout
checkoutLinks = checkoutPopup.find_elements_by_tag_name('a')

# Searches all of the links in the overlay for the checkout option
# for link in checkoutLinks:
#     if link.text == 'CHECKOUT':
#         link.click()
#     print(link.text)

# Checkout is the second link, but if the page changes in the future will need to use the above for loop to find the
# button
checkoutLinks.__getitem__(1).click()

# Wait for the checkout page to load
time.sleep(1)

# To use this method, I have to have the user's password which means I need to find a way to safely use and remove the
# the password after it's used so it can't be stolen

# Begin logging the user in for a faster checkout
email = driver.find_element_by_xpath('//*[@id="dwfrm_login_username"]')

email.send_keys('email@email.com')

password = driver.find_element_by_xpath('//*[@id="dwfrm_login_password"]')

# This is dangerous because I need a way to keep a user's password hidden
password.send_keys('password')

# Clicks the login button
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[3]/div[2]/div[1]/div/form/fieldset/div[4]/button').click()

# # The user provided invalid login credentials so the login warning banner was displayed
# if driver.find_element_by_xpath('//*[@id="login-warning-alert"]').is_displayed():
#     print('Invalid login')
#     exit(0)

# If user doesn't give login info.  Fill out the shipping information

firstName = driver.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_firstName"]')

firstName.send_keys('first')

lastName = driver.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_lastName"]')

lastName.send_keys('last')

address = driver.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_address1"]')

address.send_keys('1234 fake address st')

city = driver.find_element_by_xpath('//*[@id="dwfrm_shipping_shiptoaddress_shippingAddress_city"]')

city.send_keys('city')

driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[2]/ng-form/div[2]/div/div[6]/div[1]').click()

stateList = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[2]/ng-form/div[2]/div/div[6]/div[1]/div[2]')


for state in stateList:
    if state.text == 'Montana':
         driver.execute_script("arguments[0].className = 'materialize-select-option selected'", state)
        break
    else:
        print(state.text)