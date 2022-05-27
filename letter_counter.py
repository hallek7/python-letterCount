def main():
    print("This prog counts number of vowels in inpute phrase")
    lettetoCount = input("Enter letters to count : ").lower()
    
    inputeword = input("Enter a word : ").lower()


    totalwordtocount = 0
    for character in inputeword:
        if character in lettetoCount:
            totalwordtocount = totalwordtocount + 1

    print("Total vowels in your phrase {}".format(totalwordtocount)); 

if __name__ == "__main__":
   main()