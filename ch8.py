def Display_message():
    """Display a message"""
    print("hello, I'm learning about how to call a function")

Display_message()



birds = ["Crows","Ravens",'Hawks','Owls','Vultures','Shoebills']


def print_list(objects):
    """prints an object from a list"""
    for object in objects:
        print("\t" + object)

print_list(birds)

def make_shirt(size, message):
    print('Thank you for your money, size ' + size + " with '" + message + "' \nas your chose message will be made shortly (or never)")
print("\nPlease enter shirt message")
mess=input()
print("\nPlease enter shir size")
shirsize=input()
make_shirt(shirsize, mess)