import hashlib
import time
start_time = time.time()

senha = input("Digite sua senha:")
senhaMD5 = hashlib.md5(senha.encode('utf-8')).hexdigest()

dicionario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for a in range(0, len(dicionario)):
    for b in range(0,len(dicionario)):
        for c in range(0,len(dicionario)):
            for d in range(0,len(dicionario)):
                for e in range(0,len(dicionario)):
                    for f in range(0, len(dicionario)):
                        letra1 = dicionario[a]
                        letra2 = dicionario[b]
                        letra3 = dicionario[c]
                        letra4 = dicionario[d]
                        letra5 = dicionario[e]
                        letra6 = dicionario[f]
                        possivelSenha = letra1 + letra2 + letra3 + letra4 + letra5 + letra6
                        print(possivelSenha)
                        possivelSenhaMD5 = hashlib.md5(possivelSenha.encode('utf-8')).hexdigest()
                        if possivelSenhaMD5 == senhaMD5:
                            print('SENHA QUEBRADA!! Senha: '+possivelSenha+'  MD5: '+possivelSenhaMD5)
                            elapsed_time = time.time() - start_time
                            print(time.strftime("Tempo que demorou para quebrar a senha: %H:%M:%S", time.gmtime(elapsed_time)))
                            exit()