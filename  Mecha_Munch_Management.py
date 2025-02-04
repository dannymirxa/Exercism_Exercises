from collections import Counter

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    

    return dict(Counter(current_cart) + Counter(items_to_add))

# print(add_item({'Broccoli': 1, 'Banana': 1}, ('Broccoli', 'Kiwi', 'Kiwi', 'Kiwi', 'Melon', 'Apple', 'Banana', 'Banana')))

ideas = {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
        'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}
recipe_updates = (
                    ('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),
                
                    )

             
ideas = {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
         'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
         'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}}

recipe_updates = (('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
                ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
                ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3}))

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    """

    ideas.update(dict(recipe_updates))

    return ideas

# print(update_recipes(ideas, recipe_updates))

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    # for k_cart, v_cart in cart.items():
    #     for k_aisle, v_aisle in aisle_mapping.items():
    #         if k_cart == k_aisle:
    #             aisle_mapping[k_aisle].insert(0, v_cart)
    # return dict(sorted(aisle_mapping.items(), reverse=True))

    for k_cart, v_cart in cart.items():
        for k_aisle, v_aisle in aisle_mapping.items():
            if k_cart == k_aisle:
                v_aisle.insert(0, v_cart)
                cart[k_cart] = v_aisle

    return dict(sorted(cart.items(), reverse=True))   

# print(send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
#                     {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))

# print(send_to_store({'Orange': 1}, 
#                     {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 
#                     'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))

# print(send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1},
#                     {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False],
#                      'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    # for k_inventory, v_inventory in store_inventory.items():
    #     for k_cart, v_cart in fulfillment_cart.items():
    #         if k_inventory == k_cart:
    #             # print(f"k_inventory: {k_inventory}")
    #             # print(f"v_inventory: {v_inventory}")
    #             # print(f"k_cart: {k_cart}")
    #             # print(f"v_cart: {v_cart}")
    #             # print(f"result: {v_inventory[0]- v_cart[0]}")
    #             if v_inventory[0] - v_cart[0] <= 0:
    #                 v_cart[0] = "Out of Stock"
    #             else:
    #                 v_cart[0] = v_inventory[0] - v_cart[0]
    # for k, v in store_inventory.items():
    #     print(k,v)
    # return fulfillment_cart

    for k in fulfillment_cart.keys():
        # if fulfillment_cart[k][0] != "Out of Stock":
        store_inventory[k][0] -= fulfillment_cart[k][0]
        if store_inventory[k][0] <= 0:
            store_inventory[k][0] = "Out of Stock"

    return store_inventory

print(

update_store_inventory(   {'Kiwi': [1, 'Aisle 6', False], 'Melon': [4, 'Aisle 6', False], 'Apple': [2, 'Aisle 1', False],
                            'Raspberry': [2, 'Aisle 6', False], 'Blueberries': [5, 'Aisle 6', False],
                            'Broccoli': [1, 'Aisle 3', False]},
                            {'Apple': [2, 'Aisle 1', False], 'Raspberry': [5, 'Aisle 6', False],
                            'Blueberries': [10, 'Aisle 6', False], 'Broccoli': [4, 'Aisle 3', False],
                            'Kiwi': [1, 'Aisle 6', False], 'Melon': [8, 'Aisle 6', False]})
                                )


"""{'Kiwi': ['Out of Stock', 'Aisle 6', False], 'Melon': [4, 'Aisle 6', False],
    'Apple': ['Out of Stock', 'Aisle 1', False], 'Raspberry': [3, 'Aisle 6', False],
    'Blueberries': [5, 'Aisle 6', False], 'Broccoli': [3, 'Aisle 3', False]}"""

update_store_inventory({'Kiwi': [3, 'Aisle 6', False]},\

                        {'Kiwi': [3, 'Aisle 6', False], 'Juice': [5, 'Aisle 5', False],
                        'Yoghurt': [2, 'Aisle 2', True], 'Milk': [5, 'Aisle 2', True]})

"""{'Juice': [5, 'Aisle 5', False], 'Yoghurt': [2, 'Aisle 2', True],
    'Milk': [5, 'Aisle 2', True], 'Kiwi': ["Out of Stock", 'Aisle 6', False]}"""

