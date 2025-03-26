from time import sleep
co = 10
for c in range(10, 0, -1):
    print('\033[1:30:46m-=\033[m' * 6)
    print(' \033[1:30:46m' * 5 , '{} '.format(co) ,'  \033[m' * 5)
    co = co - 1
    print('\033[1:30:46m-=\033[m' * 6)
    sleep(1)
print('\033[1:30:46m-=\033[m' * 12)
print(' \033[1:30:46mFELIZ ANO NOVO!!!\033[m')
print('\033[1:30:46m-=\033[m' * 12)
