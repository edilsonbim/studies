from time import sleep
for c in range(10, -1, -1):
    print('\033[1:30:46m-=\033[m' * 6)
    print(' \033[1:30:46m' * 5 , '{} '.format(c) ,'  \033[m' * 5)
    print('\033[1:30:46m-=\033[m' * 6)
    sleep(1)
print('\033[1:30:46m-=\033[m' * 12)
print(' \033[1:30:46mFELIZ ANO NOVO!!!\033[m')
print('\033[1:30:46m-=\033[m' * 12)
