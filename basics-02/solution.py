

def say_hello():
    """ Prints hello world """
    print ("Helloo !!")

def conditionals():
    """ checks for a greater than b """

    pass

def loop():
    """ examples of looping  """ 


    variable = 1024
    while(variable > 0):
        print (variable)
        variable = round(variable / 2)

    variable = 1024
    for n in range(variable):
        print (variable)
        variable = round(variable/2)

    return


if __name__ == '__main__':
    """Runs each of the lab solution functions and prints the attached docstring and source"""

    say_hello()
    print (say_hello.__doc__)
    loop()
