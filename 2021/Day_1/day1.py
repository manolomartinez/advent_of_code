import numpy as np

def read_input(input_file):
    with open(input_file, 'r') as ifile:
        lines = ifile.readlines()
    return np.array([int(line) for line in lines])


def increases(my_list):
    one = my_list[:-1]
    two = my_list[1:]
    incr = [two_ > one_ for one_, two_ in zip(one, two)]
    return sum(incr)


def aggregate_3(my_list):
    one = my_list[:-2]
    two = my_list[1:-1]
    three = my_list[2:]
    return one + two + three


def main():
    data = read_input('input.txt')
    # First puzzle
    result = increases(data)
    print("First puzzle: {}".format(result))
    # Second puzzle
    data_3 = aggregate_3(data)
    result = increases(data_3)
    print("Second puzzle: {}".format(result))

if __name__=="__main__":
        main()

