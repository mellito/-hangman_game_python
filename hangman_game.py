import random
import os


# esta funcion retorna una lista con los nombre dentro de el archivo data.txt
def read():
    list_words=[]
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        for line in f:
            line=line.strip("\n")
            list_words.append(line)
                          
    return list_words    

#decidi separar el imput del usuario en un metodo la verdad no se si es muy adecuado
def word_ask():
    user_word=input("""

    adivina la palabra
    solo puedes digitar 1 letra a la vez
    """)
    return user_word


#en este metodo hacemos la validacion de todo el programa
#escojemos una palabra random con el metodo random que importe
#tambien hacemos que se establesca una lista vacia con el tamano de la letra escogida aleatoriamente
# hacemos un while que compare la 
def word_validation():

    random_word=lambda list: random.choice(list)
    palabra=random_word(read()).upper()

    empty_word=['_' for i in range(len(palabra))]
    os.system("clear")

    while set(empty_word) != set(palabra):
        
        print("    "+''.join(empty_word)) 
             
        letter=word_ask().upper()               
        os.system("clear")

        for  i in range(len(palabra)):
                
            if palabra[i]==letter:
                
                empty_word[i] = letter

                
    print(f'ganaste la palabra era {palabra}')
                                         
                

def main():
    
    word_validation()
 



if __name__=='__main__':
    main()
