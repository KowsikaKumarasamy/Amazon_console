import streamlit as st
import time  
import base64


def get_base64_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    return encoded_img

# CSS to set the background image
def set_background_image(image_file):
    encoded_img = get_base64_image(image_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background_image('background.jpg')

st.title("Amazon Console website")


# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Login"

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "cart" not in st.session_state:
    st.session_state.cart = []

def login():
    st.title("Login to Amazon")
    email_or_phone = st.text_input("Email or Phone Number")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Check for predefined user credentials
        if (email_or_phone == "user@example.com" and password == "examplePassword"):
            st.success("Login Successful!")
            st.session_state.is_logged_in = True
            st.session_state.page = "Products"
            st.experimental_rerun()
        # Check against registered user credentials
        elif (email_or_phone == st.session_state.registered_email and 
              password == st.session_state.registered_password):
            st.success("Login Successful with registered account!")
            st.session_state.is_logged_in = True
            st.session_state.page = "Products"
            st.experimental_rerun()
        else:
            st.error("Invalid email or password")

    if st.button("Forgot Password?"):
        st.write("Instructions to reset your password will be sent to your registered email.")


# Registration Function
def register():
    st.title("Register for Amazon")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Register"):
        if password == confirm_password:
            st.success("Registration successful!")
            st.session_state.registered_email = email  # Store registered email
            st.session_state.registered_password = password  # Store registered password
            st.session_state.page = "Login"  # Navigate to login after registration
        else:
            st.error("Passwords do not match")

def product_selection():
    st.title("Select a Product")

    # New Product Categories
    category = ['Washing Machine', 'Fridge', 'Mobile Phone']
    user_selection = st.selectbox('Select the category you want to buy:', category)

    # Washing Machine 
    if user_selection == 'Washing Machine':
        st.subheader('Available Washing Machine Brands:')
        washing_machine_brands = ['LG', 'Samsung', 'Haier']
        brand = st.selectbox('Select the brand:', washing_machine_brands)

        if brand == 'LG':
            load_type = st.radio('Select load type:', ('Front load', 'Top load'))
            automatic_type = st.radio('Select type:', ('Automatic', 'Semi-automatic'))

            price_dict = {
                ('red', '6kg'): 12000,
                ('silver', '6kg'): 12700,
                ('black', '6kg'): 12900,
                ('red', '7kg'): 14000,
                ('silver', '7kg'): 17500,
                ('black', '7kg'): 19500
            }
            color = st.selectbox('Select color:', ['red', 'silver', 'black'])
            capacity = st.selectbox('Select capacity:', ['6kg', '7kg'])
        
        elif brand == 'Samsung':
            load_type = st.radio('Select load type:', ('Front load', 'Top load'))
            automatic_type = st.radio('Select type:', ('Automatic', 'Semi-automatic'))

            price_dict = {
                ('black', '6kg'): 13000, ('white', '6kg'): 13700, ('grey', '6kg'): 14900,
                          ('black', '7kg'): 15000, ('white', '7kg'): 17500, ('grey', '7kg'): 18500,
                          ('black', '8kg'): 20000, ('white', '8kg'): 25800, ('grey', '8kg'): 26900

            }
            color = st.selectbox('Select color:', ['white', 'grey', 'black'])
            capacity = st.selectbox('Select capacity:', ['6kg', '7kg','8kg'])

        elif brand == 'Haier':
            load_type = st.radio('Select load type:', ('Front load', 'Top load'))
            automatic_type = st.radio('Select type:', ('Automatic', 'Semi-automatic'))

            price_dict = {
                ('black', '6kg'): 13000, ('purple', '6kg'): 13700, ('peach', '6kg'): 14900,
                          ('black', '7kg'): 15000, ('purple', '7kg'): 17500, ('peach', '7kg'): 18500,
                          ('black', '8kg'): 20000, ('purple', '8kg'): 25800, ('peach', '8kg'): 26900
            }
            color = st.selectbox('Select color:', ['purple', 'peach', 'black'])
            capacity = st.selectbox('Select capacity:', ['6kg', '7kg','8kg'])


        if st.button('Add to Cart'):
            item = f'{brand} Washing Machine ({color}, {capacity})'
            price = price_dict.get((color, capacity))  # Directly get the price
            if price is not None:
                st.session_state.cart.append({"item": item, "price": int(price)})
                st.success(f'Added {item} to the cart for ₹{price}.')
            else:
                st.error("Price not found for selected options.")
        
        # Display price when options are selected
        if 'color' in locals() and 'capacity' in locals():
            st.write(f"**Price:** ₹{price_dict.get((color, capacity), 'N/A')}")

    # Fridge 
    elif user_selection == 'Fridge':
        st.subheader('Available Fridge Brands:')
        fridge_brands = ['LG', 'Whirlpool', 'Samsung']
        brand = st.selectbox('Select the brand:', fridge_brands)

        if brand == 'LG':
            door_type = st.radio('Select door type:', ('Single Door', 'Double Door'))

            if door_type == 'Single Door':
                color = st.selectbox('Select color:', ['silver', 'black', 'purple'])
                capacity = st.selectbox('Select capacity:', ['185ltr', '240ltr'])

                price_dict = {
                    ('silver', '185ltr'): 8000,
                    ('black', '185ltr'): 9000,
                    ('purple', '185ltr'): 7000,
                    ('silver', '240ltr'): 10000,
                    ('black', '240ltr'): 12000,
                    ('purple', '240ltr'): 11900
                }

            elif door_type == 'Double Door':
                color = st.selectbox('Select color:', ['black', 'blue', 'green', 'indigo'])
                capacity = st.selectbox('Select capacity:', ['240ltr', '289ltr'])

                price_dict = {
                    ('black', '240ltr'): 14000,
                    ('blue', '240ltr'): 12000,
                    ('green', '240ltr'): 11900,
                    ('indigo', '240ltr'): 13000,
                    ('black', '289ltr'): 22000,
                    ('blue', '289ltr'): 20000,
                    ('green', '289ltr'): 18900,
                    ('indigo', '289ltr'): 21000
                }

        if brand == 'Whirlpool':
            door_type = st.radio('Select door type:', ('Single Door', 'Double Door'))

            if door_type == 'Single Door':
                color = st.selectbox('Select color:', ['silver', 'black', 'purple'])
                capacity = st.selectbox('Select capacity:', ['185ltr', '240ltr'])

                price_dict = {
                    ('silver', '185ltr'): 8000,
                    ('black', '185ltr'): 9000,
                    ('purple', '185ltr'): 7000,
                    ('silver', '240ltr'): 10000,
                    ('black', '240ltr'): 12000,
                    ('purple', '240ltr'): 11900
                }

            elif door_type == 'Double Door':
                color = st.selectbox('Select color:', ['black', 'blue', 'green', 'indigo'])
                capacity = st.selectbox('Select capacity:', ['240ltr', '289ltr'])

                price_dict = {
                    ('black', '240ltr'): 14000,
                    ('blue', '240ltr'): 12000,
                    ('green', '240ltr'): 11900,
                    ('indigo', '240ltr'): 13000,
                    ('black', '289ltr'): 22000,
                    ('blue', '289ltr'): 20000,
                    ('green', '289ltr'): 18900,
                    ('indigo', '289ltr'): 21000
                }

        if brand == 'Samsung':
            door_type = st.radio('Select door type:', ('Single Door', 'Double Door'))

            if door_type == 'Single Door':
                color = st.selectbox('Select color:', ['violet', 'black', 'green'])
                capacity = st.selectbox('Select capacity:', ['185ltr', '240ltr'])

                price_dict = {
                    ('black', '185ltr'): 11000, ('violet', '185ltr'): 9000, ('green', '185ltr'): 9500,
                    ('black', '240ltr'): 15000, ('violet', '240ltr'): 13000, ('green', '240ltr'): 13900
                }

            elif door_type == 'Double Door':
                color = st.selectbox('Select color:', ['black', 'red', 'pastal greenn', 'silver'])
                capacity = st.selectbox('Select capacity:', ['240ltr', '289ltr'])

                price_dict = {
                    ('black', '240ltr'): 16000, ('pastal green', '240ltr'): 14000,
                    ('silver', '240ltr'): 11900, ('red', '240ltr'): 13000,
                    ('black', '289ltr'): 24000, ('pastal green', '289ltr'): 22600,
                    ('silver', '289ltr'): 20900, ('red', '289ltr'): 21000
                }

        if st.button('Add to Cart'):
            item = f'{brand} Fridge ({color}, {capacity})'
            price = price_dict.get((color, capacity))  #get the price
            if price is not None:
                st.session_state.cart.append({"item": item, "price": int(price)})
                st.success(f'Added {item} to the cart for ₹{price}.')
            else:
                st.error("Price not found for selected options.")
        
        # Display price when options are selected
        if 'color' in locals() and 'capacity' in locals():
            st.write(f"**Price:** ₹{price_dict.get((color, capacity), 'N/A')}")

    # Mobile Phone 
    elif user_selection == 'Mobile Phone':
        st.subheader('Available Mobile Phone Brands:')
        mobile_phone_brands = ['Redmi', 'Oppo', 'Vivo']
        brand = st.selectbox('Select the brand:', mobile_phone_brands)

        if brand == 'Redmi':
            model = st.selectbox('Select the model:', ['Redmi 13C 5G', 'Redmi 12 5G', 'Redmi Note 13 Pro'])
            color = st.selectbox('Select color:', ['red', 'black', 'mint'])
            variant = st.selectbox('Select variant:', ['4 GB RAM, 128GB STORAGE', '6 GB RAM, 128GB STORAGE', '8 GB RAM, 128GB STORAGE'])

            price_dict = {
                ('red', '4 GB RAM, 128GB STORAGE'): 15000,
                ('black', '4 GB RAM, 128GB STORAGE'): 17800,
                ('mint', '4 GB RAM, 128GB STORAGE'): 15900,
                ('red', '6 GB RAM, 128GB STORAGE'): 18000,
                ('black', '6 GB RAM, 128GB STORAGE'): 20600,
                ('mint', '6 GB RAM, 128GB STORAGE'): 16900,
                ('red', '8 GB RAM, 128GB STORAGE'): 20000,
                ('black', '8 GB RAM, 128GB STORAGE'): 25700,
                ('mint', '8 GB RAM, 128GB STORAGE'): 18600
            }

        elif brand == 'Oppo':
            model = st.selectbox('Select the model:', ['OPPO A3 PRO 5G', 'OPPO F25 PRO 5G', 'OPPO F27 PRO+ 5G'])
            color = st.selectbox('Select color:', ['coral purple', 'starry black', 'Navy'])
            variant = st.selectbox('Select variant:', ['8 GB RAM, 128GB STORAGE', '6 GB RAM, 128GB STORAGE', '8 GB RAM, 256GB STORAGE'])

            price_dict = {
                ('coral purple', '8 GB RAM, 128GB STORAGE'): 23999,
                ('starry black', '8 GB RAM, 128GB STORAGE'): 17999,
                ('navy', '8 GB RAM, 128GB STORAGE'): 27999,
                ('coral purple', '6 GB RAM, 128GB STORAGE'): 20999,
                ('starry black', '6 GB RAM, 128GB STORAGE'): 15999,
                ('navy', '6 GB RAM, 128GB STORAGE'): 19999,
                ('coral purple', '8 GB RAM, 256GB STORAGE'): 24999,
                ('starry black', '8 GB RAM, 256GB STORAGE'): 19999,
                ('navy', '8 GB RAM, 256GB STORAGE'): 29999
            }

        elif brand == 'Vivo':
            model = st.selectbox('Select the model:', ['VIVO Y28 5G', 'VIVO Y200 5G', 'VIVO Y58 5G'])
            color = st.selectbox('Select color:', ['aqua', 'jade black', 'gem green'])
            variant = st.selectbox('Select variant:', ['8 GB RAM, 128GB STORAGE', '6 GB RAM, 128GB STORAGE', '8 GB RAM, 256GB STORAGE'])

            price_dict = {
                ('aqua', '8 GB RAM, 128GB STORAGE'): 23000,
                ('jade black', '8 GB RAM, 128GB STORAGE'): 20800,
                ('gem green', '8 GB RAM, 128GB STORAGE'): 19900,
                ('aqua', '6 GB RAM, 128GB STORAGE'): 18000,
                ('jade black', '6 GB RAM, 128GB STORAGE'): 20600,
                ('gem green', '6 GB RAM, 128GB STORAGE'): 16900,
                ('aqua', '8 GB RAM, 256GB STORAGE'): 27000,
                ('jade black', '8 GB RAM, 256GB STORAGE'): 25700,
                ('gem green', '8 GB RAM, 256GB STORAGE'): 21900
            }
        

        if 'color' in locals() and 'variant' in locals():
            price = price_dict.get((color, variant))

            if st.button('Add to Cart'):
                item = f'{brand} {model} ({color}, {variant})'
                if price is not None:
                    st.session_state.cart.append({"item": item, "price": int(price)})
                    st.success(f'Added {item} to the cart for ₹{price}.')
                else:
                    st.error("Price not found for selected options.")

            # Display price when model is selected
            if price is not None:
                st.write(f"**Price:** ₹{price}")

# View Cart Function
def view_cart():
    st.title("Your Cart")
    if st.session_state.cart:
        total_price = 0
        for i, item in enumerate(st.session_state.cart):
            st.write(item["item"])  
            total_price += int(item["price"])  # Convert to int to avoid Error
            
        remove_item = st.selectbox("Remove Item", [item["item"] for item in st.session_state.cart] + ["None"])
        if st.button("Remove"):
            if remove_item != "None":
                st.session_state.cart = [item for item in st.session_state.cart if item["item"] != remove_item]
                st.experimental_rerun()

        st.write(f"**Total: ₹{total_price}**")
        
        if st.button("Proceed to Payment"):
            st.session_state.page = "Payment"
            st.experimental_rerun()
    else:
        st.warning("Your cart is empty. Add some products to the cart!")



# Payment Function
def payment():
    st.title("Payment")

    total_price = sum(item["price"] for item in st.session_state.cart)
    st.write(f"**Total amount: ₹{total_price}**")
    
    payment_method = st.selectbox("Select Payment Method", ["Debit Card", "Credit Card"])
    card_number = st.text_input("Card Number")
    cvv = st.text_input("CVV", type="password")
    otp = st.text_input("Enter OTP", type="password")

    if st.button("Confirm Payment"):
        if card_number and cvv and otp:
            st.success("Payment Successful!")
           

            # Delay before moving to the invoice page
            time.sleep(2)  
            st.session_state.page = "Invoice"  # Navigate to the invoice page
            st.experimental_rerun()
        else:
            st.error("Please complete all payment fields!")

# Generate Invoice Function
def generate_invoice():
    st.title("Invoice")
    
    total_price = 0
    st.write("**Purchased Items:**")
    
    # Display purchased items and calculate total price
    for item in st.session_state.cart:
        st.write(f"- {item['item']} - ₹{item['price']}")
        total_price += item["price"]
    
    st.write(f"**Total Amount Paid: ₹{total_price}**")
    
    # Display invoice details 
    st.write("---")  
    st.subheader("Invoice Details:")
    
    for item in st.session_state.cart:
        st.write(f"- {item['item']} - ₹{item['price']}")
    
    st.write(f"**Total Amount: ₹{total_price}**")

# Sidebar for navigation
with st.sidebar:
    if not st.session_state.is_logged_in:
        selected = st.selectbox("Main Menu", ["Login", "Register"])
    else:
        selected = st.selectbox("Main Menu", ["Products", "View Cart", "Payment", "Invoice", "Logout"])
    st.session_state.page = selected

# Page rendering
if st.session_state.page == "Login":
    login()

elif st.session_state.page == "Register":  
    register() 

elif st.session_state.page == "Products":
    if st.session_state.is_logged_in:
        product_selection()
    else:
        st.warning("Please login to access the Products page.")

elif st.session_state.page == "View Cart":
    if st.session_state.is_logged_in:
        view_cart()
    else:
        st.warning("Please login to access the Cart.")

elif st.session_state.page == "Payment":
    if st.session_state.is_logged_in and st.session_state.cart:
        payment()
    elif not st.session_state.cart:
        st.warning("Your cart is empty. Add some products before proceeding to payment.")
    else:
        st.warning("Please login to proceed with the payment.")

elif st.session_state.page == "Invoice":
    generate_invoice()

elif st.session_state.page == "Logout":
    st.session_state.is_logged_in = False
    st.success("You have been logged out.")
    st.session_state.page = "Login"
    st.experimental_rerun()
