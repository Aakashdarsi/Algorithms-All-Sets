def ceaserCiphorEncryptor(letters,key):
    new_letters = []
    new_key = key%26 
    for i in letters:
        new_character_unicode = ord(i) + new_key
        if new_character_unicode <= 122 :
            new_letters.append(chr(new_character_unicode))
        else:
            new_letters.append(chr(96 + new_character_unicode % 122))
    print(new_letters)
l = input()
key = int(input())
ceaserCiphorEncryptor(l,key)