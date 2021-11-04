#! /usr/bin/env python
from platform import python_version

print("Versão utilizada:" + python_version() + "\n")

def validaTipoInserido(stringInserida):
    try: 
        test = int(stringInserida)
        return True;
    except ValueError:
        print("\nOps! Algo deu errado, certifique-se de inserir um identificador válido se atendando aos valores inseridos.")
        return False

def validaZeroNoInicio(stringInserida):
    if stringInserida[0]=="0":
        return False
    else:
        return True

def validaSequenciaCaracteres(stringInserida):
    if( len(cdvpy) == 6 ):

        doubleCaracteres = []
        
        [ doubleCaracteres.append(stringInserida[i]+stringInserida[i+1]) for i in range(0,len(stringInserida)-1) ]
        
        countRepetidos = len( set( [ i for i in doubleCaracteres if doubleCaracteres.count( i ) > 1] ) )
        
        if (countRepetidos > 0):
            return False
        else:
            return True

    else:
        print("\nOps! Algo deu errado, certifique-se de inserir um identificador válido se atentando ao tamanho inserido.")
        return False
    
def valida_cdvpy(cdvpy):
    ans = False

    if validaTipoInserido(cdvpy) and validaZeroNoInicio(cdvpy):
        ans = validaSequenciaCaracteres(cdvpy)
    
    return ans

if __name__ == '__main__':
    cdvpy = input('Digite um CDvPy:')
    print(valida_cdvpy(cdvpy))