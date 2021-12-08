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
# hacemos un while que compare la con el metodo set la palabra random y la lista vacia
def word_validation():

    random_word=lambda list: random.choice(list)
    palabra=random_word(read()).upper()

    empty_word=['_' for i in range(len(palabra))]
    os.system("clear")

    try_counter=10

    while set(empty_word) != set(palabra):
        
        
        print(f'    tienes {try_counter} intentos')  

        print("    "+''.join(empty_word)) 
        
         
        letter=word_ask().upper()               
        os.system("clear")  
        
        try:
            if len(letter)>1:
                raise ValueError("    solo puedes ingresar una letra") 
            if letter=="":
                raise ValueError("    tienes que ingresar un dato") 
            if letter[0].isdigit()==True:
                raise ValueError("    no puedes ingresar numeros") 
            
            check=bool
            
            for  i in range(len(palabra)):
                
                if palabra[i]==letter:
                
                    empty_word[i] = letter 
                    check=True
            

        except ValueError as ve:
            print(ve)  

        if check!=True:
            try_counter=try_counter-1

        check=False    

        if try_counter == 0:
            print("se te acabaron los intentos perdiste")
            break
    
        
    if set(empty_word) == set(palabra):
        print(f'ganaste la palabra era {palabra}')
        
           
    
                
    
                                         
                

def main():
    
    word_validation()
 



if __name__=='__main__':
    main()
