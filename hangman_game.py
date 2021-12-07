import random



# esta funcion retorna una lista con los nombre dentro de el archivo data.txt
def read():
    list_words=[]
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        for line in f:
            line=line.strip("\n")
            list_words.append(line)
                          
        return list_words    

            

def main():
    random_word=lambda list: random.choice(list)
    palabra=random_word(read())
    print(palabra)
    print(len(palabra))


    



if __name__=='__main__':
    main()
