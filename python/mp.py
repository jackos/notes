import concurrent.futures
import time

def get_sqaure(val):
    return(val**25)

def main():
    start = time.time()
    mylist = range(1, 10000)
    counter = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number in executor.map(get_sqaure, mylist):
            print(number)
            counter += 1
            
    duration = time.time() - start
    print(f'It took {duration} seconds to calculate {counter + 1} numbers')

if __name__ == '__main__':
    main()