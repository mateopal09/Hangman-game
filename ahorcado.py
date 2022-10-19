import random
import os


def playing(normalized):

    list1 = []

    attempts = 6 

    

    for separate in normalized:
         list1.append(separate)

    hidels = ['_' for i in range(0,len(list1))]

    os.system('cls')
    print("Bienvenido al ahorcado")
    print("Made by Mateo")
    while hidels != list1:
        
        print("\nYour attempts are " , attempts)
        print(" ".join(hidels).lower())
        word = input("\nType the letter ")
        contador = 0
        for i in range(0,len(list1)):    
            if  list1[i] == word:
                hidels.pop(i)
                hidels.insert(i,word)
                contador = contador + 1
                                       
        if contador == 0:
            attempts=attempts-1 
            print("                       __                              ")
            print("                     .'  '.                            ")
            print("                 _.-'/  |  \                          ")
            print("    ,        _.-'  ,|  /  0 `-.                        ")
            print("    |\    .-'       `--""-.__.'=====================-, ")
            print("    \ '-'`        .___.--._)=========================| ")
            print("     \            .'      |                          | ")
            print("      |     /,_.-'        |        UUU esa no es,    | ")
            print("    _/   _.'(             |         vidas  {}         | ".format(attempts)) 
            print("   /  ,-' \  \            |      siguelo intentando  | ")
            print("   \  \    `-'            |                          | ")
            print("    `-'                   '--------------------------' ")
        if attempts==0:
            print("Sorry, you do not have more lives, the word was:", normalized.upper() ,"see you soon!!")
            break           
    if hidels == list1:
        print(normalized)


def normalize(random_word):
    
    normalized = random_word.translate(random_word.maketrans(('áéíóú'), ('aeiou')))
    return normalized

 
def chooserandomword(enumerated_dict):

    valor = enumerated_dict
    for i in valor.keys():
        random_word = random.randint(i,len(valor))
        random_words = valor.get(random_word)  
        return random_words


def enumerate_data(data_list):

    enumerated_dict = dict(enumerate(data_list))
    return enumerated_dict


def read_field():

    data_list = []
    with open("./archivos/datos.txt", "r", encoding="utf-8") as read:
        for reading in read:
            reading = reading.replace('\n','')
            data_list.append(reading)
    return data_list


def run():

    organizated_data = enumerate_data(read_field())
    theword = chooserandomword(organizated_data)
    fixword = normalize(theword) 
    playing(fixword)
    
     
if __name__ == '__main__':
    run()