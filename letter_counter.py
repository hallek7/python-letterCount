def Inputword():
    return input("Enter a word : ").lower()

def getVowelCount(words):
    vowelCount = 0
    for character in words:
        if character in ['a', 'e', 'i', 'o','u']:
            vowelCount = vowelCount + 1
    return vowelCount

def main():
    print("This prog counts number of vowels in inpute phrase")
    inputeword = Inputword()
    
    totalVowls = getVowelCount(inputeword)
    print("Total vowels in your phrase {}".format(totalVowls)); 

if __name__ == "__main__":
   main()