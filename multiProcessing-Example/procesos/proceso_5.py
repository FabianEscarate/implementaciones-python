import time

const_n_proceso = 5

def main():
    print('comienza proceso {0}'.format(const_n_proceso))
    time.sleep(3)
    print('termina proceso {0}'.format(const_n_proceso))

if __name__ == '__main__':
    main()