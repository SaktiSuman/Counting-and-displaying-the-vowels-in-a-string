def countVowels(my_string):
    count = 0
    vowels_list = []
    vowels = set("aeiouAEIOU")
    for alphabet in my_string:
        if alphabet in vowels:
            count = count + 1
            vowels_list.append(alphabet)
    vowels_string = str(vowels_list)
    print(vowels_string)
    return count
my_string = str("Sakti Suman")
print(countVowels(my_string))