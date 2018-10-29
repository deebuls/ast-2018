
def say_hello():
    """Print Hello world"""
    print("Hello World!")

def loop(ex):
    """ """
    result = ex
    while ( result > 1 ):
        result = result/2
        print (result)

def tic_tac():
    word = ""
    loop_count = 5
    for i in range(1,loop_count):
        if ( i%2 == 0 ):
            print ("---------")
        elif (i%2 > 0 ):
            print ("  |  |  ")

def tic_tac_2():
    columns=26
    rows=18
    string = ""
    for r in range(rows):
        for c in range(columns):
            if ( r%3 == 0):
                if (c%2 == 0):
                    string == string + '='
                    print ("Something")
            elif(r%5 == 0):
                if (c%2 == 0):
                    string == string + '+'
            else:
                if (c%2 == 0):
                    string == string + '-'
                x=0
        print (string)
        string = ""

def fizz():
    result = 0
    for i in range(1,1002):
        if (i%5 == 0) or (i%3 == 0):
            result += i
    print (result)

def collatz(ex):
    print ("The amount of values is ")
    something = ex
    counter = 0.
    while (ex>1):
        if (ex%2 ==0):
            ex = ex/2
        else:
            ex = ex*3+1
        print (ex)
        counter += 1
    print ("The amount of values is " + str(counter))

def deg():
     fahrenheit = float(input())
     celsiuss= ((fahrenheit - 32) * 5/9 )
     print ("It is {0} degrees Celsius".format(celsiuss))

def python_interactive():
    s = [0] *3
    print (s)
    s[0] *= 1
    print (s)

    s = [''] *3
    print (s)
    s[0] += 'a'
    print (s)

    s = [[]] *3
    print (s)
    s[0] += [1]
    print (s)

    s[0].append(1)
    print (s)
    id(s)

def tuples_gcd(a,b):
    while b != 0:
        (a, b) = (b, a % b)
    print a

def flip_dict(dictionary_value):
    print dictionary_value
    from collections import defaultdict

    diccion = dictionary_value
    rev_diccion = defaultdict(list)

    for key,value in diccion.iteritems():
        rev_diccion[value].append(key)
    print (rev_diccion)

def comprehension():
    '''[x for x in [1, 2, 3, 4]]
        Here the list comprehension will not do anything
        [n - 2 for n in range(10)]
        To every number from 0 to 9 will substract a value of 2
        [k % 10 for k in range(41) if k % 3 == 0]
        here the new value will be the residue of the division by 10 of every number divisible by 3
        [s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]]
        in this example the returned value will be the string on lowercase
        when the first letter has a value lesser than the last lettter in the word
        because the Uppercases (ASCII) are first than the lowercases the only match is
        PythOn which will be returned in lowercases

        # Something is fishy here. Can you spot it?
        arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
        The comma after 'do'

        print([el.append(el[0] * 4) for el in arr])  # What is printed?
        for every item in the array it will be multpilied by 4 his value or his content
        value in case of int, repetition by 4 in case strings and 4 times the tuple
        print(arr)  # What is the content of `arr` at this point?


        [letter for letter in "pYthON" if letter.isupper()]
        {len(w) for w in ["its", "the", "remix", "to", "ignition"]}'''

    print ([(x**2)+1 for x in [0, 1, 2, 3]]) # -> [1, 3, 5, 7]  # Double and add one
    print ([s[0].upper() for s in ['apple', 'orange', 'pear']]) #-> ['A', 'O', 'P']  # Capitalize first letter
    print ([s for s in ['apple', 'orange', 'pear'] if s.find('p')>=0 ])  # -> ['apple', 'pear']]  # Contains a 'p'

    print ([s.replace("TA_","") for s in ["TA_sam", "student_poohbear", "TA_guido", "student_htiek"] if s.find("TA_")>=0])
    # -> ["sam", "guido"]
    print ([(s,len(s)) for s in ['apple', 'orange', 'pear']])
    # [('apple', 5), ('orange', 6), ('pear', 4)]
    print ([{s:len(s)} for s in ['apple', 'orange', 'pear']])
    # [('apple', 5), ('orange', 6), ('pear', 4)]

def pascals_triangle(n):
    one = [v for v in n ]
    two = [v for v in n ]

    one.insert(0,0)
    two.insert(len(two),0)
    result = [o + t for o, t in zip(one, two)]
    print(result)
    return result



if __name__ == '__main__':
    """Runs each of the lab solution functions and prints the attached docstring and source"""
    #say_hello()
    #print (say_hello.__name__)
    #loop(1024)
    #print (say_hello.__doc__)
    #deg()
    # collatz(1000000)
    # python_interactive()
    # tuples_gcd(10, 25) # => 5
    # tuples_gcd(14, 15) # => 1
    # tuples_gcd(3, 9) # => 3
    # tuples_gcd(1, 1) # => 1
    # flip_dict({"CA": "US", "NY": "US", "ON": "CA"})
    # comprehension()
    #print (comprehension.__doc__)
    # docstring(comprehension)
    # pascals_triangle(pascals_triangle(pascals_triangle(pascals_triangle([1]))))
