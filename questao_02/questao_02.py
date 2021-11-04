#! /usr/bin/env python
import pandas as pd
from platform import python_version

print("Versão utilizada:" + python_version() + "\n")

data = pd.read_csv("questao_02.csv")


def writeOnFile( inteiro ):

    arq = open("saida_%s.json" % str(inteiro), 'w')   

    arq.write("{\n\t\"title\": \"Floor Access Event\",\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"person_id\": {\n\t\t\t\"type\": " + "\"string\"\n" )
    
    arq.write("\t\t},\n\t\t\"datetime\": {\n\t\t\t\"type\": " + "\"string\"" + ",\n\t\t\t\"format\": " + "\"" + "date-time" + "\"\n" )

    arq.write("\t\t},\n\t\t\"floor_level\": {\n\t\t\t\"type\": " + "\"integer\"\n")

    arq.write("\t\t},\n\t\t\"building\": {\n\t\t\t\"type\": " + "\"string\"\n")

    arq.write("\t\t}\n\t},\n\t\"required\": [ " + "\"" + str(data.loc[inteiro,"Person Id"]) + "\"" + ", " + "\"" + str(data.loc[inteiro,"Floor Access DateTime"]) + "\"" + ", " + str(data.loc[inteiro,"Floor Level"]) + ", " + "\"" + str(data.loc[inteiro,"Building"]) + "\"" + "]\n}" )

    arq.close()


if __name__ == '__main__':

    for i in range(0,len(data.index)):
        writeOnFile(i)
