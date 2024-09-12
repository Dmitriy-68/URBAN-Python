from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline() != '':
            all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный метод
# start = datetime.now()
# for f in filenames:
#     read_info(f)
# end = datetime.now()
# print(end - start)

# многопроцессорный метод
if __name__ == '__main__':
    start = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = datetime.now()
    print(end - start)
