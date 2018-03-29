# https://www.adidas.com/us/ultraboost-shoes/BB6165.html
# http://www.adidas.com/us/ultraboost-shoes/BB6166_590.html?forceSelSize=BB6166_590
# http://www.adidas.com/us/ultraboost-shoes/BB6166_610.html?forceSelSize=BB6166_610
# https://www.adidas.com/us/ultraboost-shoes/BB6167.html


def create_url(model, size):
    # Set the lowest shoe size to look at to be a Men's size 6.5
    start_size = 580

    # Take whatever size the user inputs and subtract 6.5 to help generate size code
    shoe_size_code = size - 6.5

    # Multiply the size code by 20 because Adidas increases the value for each whole size by 20
    shoe_size_code = size * 20

    # Add this size code to the start size to create a code for any sized shoe
    temp = start_size + shoe_size_code

    # Convert this value into an integer
    shoe_size_code = int(temp)

    # Create the URL
    url = 'http://www.adidas.com/us/' + str(model) + '_' + str(shoe_size_code) + '.html?forceSelSize=' + str(model) + \
          '_' + str(shoe_size_code)

    return url
