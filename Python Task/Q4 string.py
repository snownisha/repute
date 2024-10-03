def calc(word):
    vowels= 0
    consonants =0
    digits=0
    whiteSpace = 0


    for i in word:
        if i.isalpha():
            if i.lower() in "aeiou":
                vowels+=1
            else:
                consonants+=1
        if i.isdigit():
            digits+=1
        if i == " ":
            whiteSpace+=1
    print(f"There are {consonants} consonants, {digits} digits, {vowels} vowels and {whiteSpace} whitespaces in {word}")


string = input("Enter anything : ")
calc(string)
