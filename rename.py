import os
import re
import sys

if len(sys.argv) == 1:
    source_dir = 'files'
    pattern = 'photo_\d+_'  
elif len(sys.argv) == 3:
    source_dir = str(sys.argv[1])
    pattern = str(sys.argv[2])
else:
    sys.exit("Erro na quantidade de argumentos passados")

if os.path.exists(str(sys.argv[1])) == False:
    sys.exit("Erro: diretório não existe.")

for i, f_name in enumerate(os.listdir(source_dir)):
    source_f = source_dir + "/" + f_name
    num = ''
    if 0<=i<9:
        num = '000'+str(i)
    elif 9<i<100:
        num = '00'+str(i)
    else:
        num = '0'+str(i)

    destination_f = source_dir + "/" + re.sub(pattern, num + '_' , f_name)
    os.rename(source_f, destination_f)
    print(source_f + "--->"+destination_f)

