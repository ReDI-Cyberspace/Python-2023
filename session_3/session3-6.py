my_list = [
    1,
    "hello",
    True,
    'bye'
]

for element in my_list:
    if type(element) == str:
        # is_string(eleemtn, str)
        print('I have found my string! - '+str(element))
