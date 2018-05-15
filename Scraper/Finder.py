# https://www.adidas.com/us/ultraboost-shoes/BB6165.html
# http://www.adidas.com/us/ultraboost-shoes/BB6166_590.html?forceSelSize=BB6166_590
# http://www.adidas.com/us/ultraboost-shoes/BB6166_610.html?forceSelSize=BB6166_610
# https://www.adidas.com/us/ultraboost-shoes/BB6167.html

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}

import bs4

import requests

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
