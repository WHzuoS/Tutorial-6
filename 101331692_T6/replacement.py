def appendList():
    """
    Function Description:
        Add user-defined elements within a specified range to a list.

    Parameters:
        None
        
    Return:
        List: all user defined elements
    """
    # Initialize list
    num_list = []

    # Initialize variables
    list_elements = 0
    
    while True:
        
        # Prompt user for a number between 1-10
        # Check if the number is negative
        list_elements = input("Please enter a number between 1-10 [Type -1 to exit] >> ")
        if (int(list_elements) <= 0):
            break
        
        # Append user number to list
        num_list.append(int(list_elements))
    
    # Output list
    print("List: ", num_list, "\n")
    
    # Return list with string elements
    return num_list
        
def replace(num_list):
    """
    Function Description:
        This function replaces all specified elements with a user-defined string. 
        It then outputs the modified result and counts the number of changes made.
    
    Parameters:
        num_list (string): List with user-defined elements.
        
    Return:
        None
    """
    # Initialize variables
    num = 0
    data = ""

    while True:
        
        # Create and initialize a local variable
        position = -1
        counter = 0
        
        # Prompt user for a number in the list
        # Check if user inputs 'q'
        num = input("Enter a number to change ['q' to quit] >> ")
        if (num.lower() == 'q'):
            break
        
        # Prompt user for a string
        data = input("With string >> ")
        
        # Iterate through list elements
        # Check for specified element to change
        # Using a counter, determine the position of element to change
        # then count all instances where the element was changed
        for i in num_list:
            position += 1
            if (i == int(num)):
                num_list[position] = data
                counter += 1
                
        # Output list
        # Output counter
        print("List: ", num_list)
        print(f"The number {num} was replaced {counter} times. \n")

# Call function appendList    
# Call function replace()       
replace(appendList())