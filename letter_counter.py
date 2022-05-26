def main():
    print("This prog counts number of vowels in inpute phrase")
    inputeword = input("Enter a word : ").lower()

    totalwords = 0
    for character in inputeword:
        if character in ['a', 'e', 'i', 'o','u']:
            totalwords = totalwords + 1

    print("Total vowels in your phrase {}".format(totalwords)); 

if __name__ == "__main__":
   main()