import multiprocessing
import os

def execute(proceso):
    os.system('Python procesos/{0}'.format(proceso))

def main():
    cola_de_ejecucion = (
        'proceso_2.py',
        'proceso_3.py',
        'proceso_4.py',
    )
    print('mensaje desde main.py')
    pool_size = multiprocessing.cpu_count() * 2
    print('pool size', pool_size)
    pool = multiprocessing.Pool(processes=pool_size)

    execute('proceso_1.py')
    
    pool.map(execute, cola_de_ejecucion)
    pool.close()
    pool.join()

    execute('proceso_5.py')

if __name__ == '__main__':
    main()

    # conclusion

    # la ejecucion de los procesos previos y posteriores,
    # a la cola de ejecucion siguen siendo lineales y de esta forma.

    # se pueden ejecutar tareas previas y posteriores