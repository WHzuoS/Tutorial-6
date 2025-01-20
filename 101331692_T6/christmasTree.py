def generateTree(tree_height):
    """
    Function Description
        The function will take user input as a parameter and display a tree.
    Parameters:
        tree_height (integer): Height of christmas tree
    Return: None
    """
    # Each iteration outputs one line of the christmas tree
    for i in range(tree_height + 1):
        
        # Check if the row equals tree_height 
        # Output tree stump and terminate loop
        if i == tree_height:
            print(" " * (tree_height - 1) + "|")
            break

        print(" " * (tree_height - i - 1) + "*" * ((2 * i) + 1))

    # Output new line when row ends
    print("\n")

def checkError(tree_height):
    """
    Function Description
        The function will take user input as a parameter and return the error
        message if applied.
    Parameters:
        tree_height (integer): Height of christmas tree
    Return: None
    """
    # Check if tree_height is less than expected
    if tree_height < 2:
        print("Looks like we've got a baby tree here - not quite ready for Christmas cheer.")
    
    # Check if tree_height is more than expected
    elif tree_height > 10:
        print("Whoa, that tree is too big for my cozy living room. Let's find one that fits just right.")
    
    # Draw tree
    else:
        # Call generateTree()
        generateTree(tree_height)
        
def main():
    # Call checkError()
    checkError(int(tree_height))

while True:

    # Global variable
    # Prompt user to input the height of the christmas tree
    tree_height = input("Enter the height of the Christmas tree: ")
    
    # Check if user wishes to terminate program
    if (tree_height == "quit"):
        break
    
    # Call main()
    main()
    
