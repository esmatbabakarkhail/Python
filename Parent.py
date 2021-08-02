#Following are examples related to Keyword Arguments


def my_function(child3, child2, child1):
 print("The youngest child is " + child3)
#Here we say that the order of arguments does not matter.
#For instance we can change that according to our requirements
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def std_class(classA, classB, classC):
    print("The student is of class "+classB)
    print("The student is of class "+classC)
    print("The student is of class "+classA)
    std_class(classB="GoldenBlue", classC="SilverBlue", classA="Blue")
