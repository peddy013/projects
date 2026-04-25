RESTUARANT_NAME = "Eyo Hut"
menu = {
"sku1":{
    "name" : "Hamburger",
    "Price":200},
    "sku2":{
    "name" : "Chesseburger",
    "Price": 210},
    "sku3":{
    "name" : "Milkshack",
    "Price": 200},
    "sku4":{
    "name" : "Fries",
    "Price": 20},
    "sku5":{
    "name" : "Sub",
    "Price": 160},
    "sku6":{
    "name" : "Ice Cream",
    "Price": 40},
    "sku7":{
    "name" : "Fountain drink",
    "Price": 211},
    "sku8":{
    "name" : "cookie",
    "Price": 20},
    "sku9":{
    "name" : "Brownie",
    "Price": 20},
    "sku10":{
    "name" : "Sauce",
    "Price": 100,
}
}
app_actions = {
    "1" : "Add a new menu item to cart",
    "2" : "Remove an item fro the cart",
    "3" : "Modify a cart item's quantity",
    "4" : "View cart",
    "5" : "Checkout",
    "6" : "Exit"
}
SALES_TAX_RATE = 0.75 #nigeria tax rate
cart = {} #declearing an empty cart

def display_menu():
    print("\n*****MENU*****\n")
    for sku in menu:
        parse_sku = sku[3:]
        sku_name = menu[sku]["name"] #this loop each sku and return value for name key
        sku_cost = menu[sku]["Price"]#this loop each sku and return value for price key
        print("("+ parse_sku + ")" , " ", sku_name , "-----","#",str(sku_cost) ,sep="")

#print(display_menu())
def add_item_to_cart(sku,quantity=1):
    if sku in menu:#checks if sku typed is correct
        if sku in cart:
            cart[sku] += quantity # add 
        else:
            cart[sku] = quantity #else return default 1
            #print("added", quantity,"of",menu[sku]["name"], "to the cart", sep =" ")
    else:
        print("This item is not avialable")

#print(add_item_to_cart("sku1",4))

def remove_item_from_cart(sku):
    if sku in cart:
        remove_val = cart.pop(sku)#pop remove the item and assign it to remove_val
        print(f"Removed {remove_val} from the cart")
    else:
        print(f"the item with SKU{sku} is not in the cart")
#print(remove_item_from_cart("sku1"))
#print(cart)

def modify_cart():
    print("this is a placeholder:")

def view_cart():
    print("\n*****This are your Items*****\n")
    subtotal = 0
    count = 0
    for sku,count in cart:
        if sku in cart:
            qty = cart[sku]
            count =+ 1
            subtotal += menu[sku]["Price"] * qty
        print(f"item {count} in the cart: {qty} of {menu[sku]["name"]} @ {menu[sku]["Price"]} naira = {subtotal}")
    tax = subtotal * SALES_TAX_RATE
    grand_total = subtotal + tax 
    print("Grand total:", grand_total,"naira",sep =" ")

def check_out():
    print("\n****\n")
    view_cart()
    print("thanks for the Order! Goodbye")
    print("\n")

def get_sku_and_qty(sku_prompt, qty_prompt=None):
    item_sku = input(sku_prompt)#provide the input when passing value to function
    item_sku = "sku" + item_sku #input store original value as string

    if qty_prompt: # if its not none
        qty = input(qty_prompt)#input store original value as string
        if not qty.isdigit():
            qty = 1
        qty = int(qty)

        return item_sku,qty
    else:
        return item_sku

def ordering():
    print("Welcome to "+ RESTUARANT_NAME +"!")
    order = True
    while order:
        print("\n******Ordering action******\n")
        for number in app_actions:  
            description = app_actions[number]
            print("("+ number+")", description, sep =" ")
        response = input("please enter the number of actions you want to perform: ")
        if response == "1":
            display_menu() 
            sku_prompt = "Please enter the sku from the menu you want to order: "
            qty_prompt = "Please enter the quantity from the menu you want to order: "
            ordered_sku,quantity = get_sku_and_qty(sku_prompt,qty_prompt)#tuple from return variable
            add_item_to_cart(ordered_sku,quantity)
        elif response == "2":
            display_menu() 
            sku_prompt = "Please enter the sku from the menu you want to order"
            item_sku = get_sku_and_qty(sku_prompt)
            remove_item_from_cart(item_sku)
        elif response == "3":
            modify_cart()   
        elif response == "4":  
            view_cart()     
        elif response == "5":                             
            check_out()
            order = False
        elif response == "6":
            print("Goodbye")
            order = False
        else:
            print("You have entered an invalid action number, pls try again")

ordering()



     