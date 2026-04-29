from catalog import catalog

cart = [] # global variable empty list 

#header / helper function


def print_header(text):
    print("-------------------------------")
    print(text)
    print("-------------------------------")

def menu():
    print("====   Menu:   ====")
    print("1. - View catalog")
    print("2. - Serch Product")
    print("3. - View Cart")
    print("4. - Clear Cart")
    print("Q. - Quit")


#catalog and cart funtions
def print_catalog():
    print_header("-- our catalog --")
    for prod in catalog:
        print(f"| {prod['id']} - {prod['title'].ljust(15)} - ${prod['price']:.2f} |")
    
    answer = input("type ID to add (N to close): ")
    if answer.lower() == "n":
        return                      
    else:
        add_product_to_cart(answer)  
        print("---------------------------------")


def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id): 
            found = True
            cart.append(prod) # add products to the end of the cart
            print(f" {prod["title"]} added to your cart.")
            break # stop after finding the product

    if not found:
        print(f"**Error: invalid ID")
        print("---------------------------------")

def search_product():
    text = input("search product title:  ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f"| {prod['id']} - {prod['title'].ljust(15)} - ${prod['price']:.2f} |")
            choice = input(" do you want to add this item to your cart? (Y/N) ")
            if choice.lower() == "y":
                add_product_to_cart(str(prod["id"]))
            break # stop after finding the product
    
    if not found:
        print(f"sorry this item it dosent exist")
        print("---------------------------------")

#create a funtion called view_cart()
#print a header call it "your cart"
#use if and else to print out all items in your cart

def view_cart():
    print_header("your cart")
    if len(cart) == 0:
        print("your cart is empty")
    else:
        for prod in cart:
            print(f"| {prod['id']} - {prod['title'].ljust(15)} - ${prod['price']:.2f} |")
        cart_total()
    print("---------------------------------")


#funtion cart_total
#variable total = 
# for loop to add the price of the product
# print total 

def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
    print(f"total: ${total:.2f}")

#clear code
# funtion clear_cart()
# give the user the option (menu)
# add to main program loop
# print ("cart cleared")

def clear_cart():
    cart.clear() 
    print("cart cleared!!")


# main program loop
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to the Store")
    menu()

    option = input("choose an option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        cart.clear() # clear the cart list
        print("cart cleared")
    elif option == "q" or option == "Q":
        print("good bye")
    else:
        print("**Error: invalid option")
        print("---------------------------------")





