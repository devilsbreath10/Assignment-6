# Function creation
def ds(roll_no, name):
 # List creation
    ls=[]
    ls.append(roll_no)
    ls.append(name)
    print("List: ",ls)

 # Tuple creation
    tup_ex = ()
    tup_ex = tup_ex + (roll_no,) + (name,) #If no comma is given it will show TypeError!!
    print("Tuple: ",tup_ex)

# Set creation
    set_ex = set()
    set_ex.add(roll_no)
    set_ex.add(name)
    print("Set: ",set_ex)

# Dictionary creation
    dic_ex = {}
    dic_ex["Roll No"] = roll_no
    dic_ex["Name"] = name
    print("Dictionary: ",dic_ex)

# Adding values to each data structure!!
    #List
    ls[0] = "16"
    ls[1] = "Yousuf"
    print("List after changing values: ",ls)
    #Tuple
    tup_ex = ("52","Nandish")
    print("Tuple after changing values: ",tup_ex)
    #Set
    set_ex = set(["55","Owais"])
    print("Set after changing values: ", set_ex)
    #Dictionary
    dic_ex["Roll No"] = "38"
    dic_ex["Name"] = "Devarsh"
    print("Dictionary after changing values: ",dic_ex)

    # Delete the data structures
    del ls
    #print(ls)          It will display error
    del tup_ex
    #print(tup_ex)      It will display error
    del set_ex
    #print(set_ex)      It will display error
    del dic_ex
    #print(dic_ex)      It will display error

ds("20","Harry")