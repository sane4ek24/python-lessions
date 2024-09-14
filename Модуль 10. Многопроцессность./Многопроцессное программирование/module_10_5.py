import multiprocessing
from datetime import datetime
from multiprocessing import pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
# Линейный расчет
st1 = datetime.now()
for f in files:
    print(f)
    read_info(f)
end1 = datetime.now()
print(end1 - st1)

# Многопроцессорный расчет

if __name__ == '__main__':
    start2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    end2 = datetime.now()
    print(end2 - start2)
