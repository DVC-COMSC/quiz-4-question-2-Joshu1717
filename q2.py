
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###


while True:
    words = (input("Enter some words or the word stop or STOP to quit: "))
    wordlist = words.split()

    if words == "STOP" or words == "stop":
        break

    print("The words in the list are: ", words)

    smallest = largest = wordlist[0];  
   
    for i in range(0, len(wordlist)):
        if(len(smallest) > len(wordlist[i])):
            smallest = wordlist[i]
        if(len(largest) < len(wordlist[i])):
            largest = wordlist[i]
    
    print("Smallest word: " + smallest);  
    print("Largest word: " + largest); 