def read_input(myfile):
    with open(myfile, 'r') as fobject:
        contents = fobject.read()
    first_split = contents.split('\n\n')
    second_split = [[int(calories) for calories in content.split('\n')] for content in first_split[:-1]]
    return second_split

def result1(myfile):
    second_split = read_input(myfile)
    return max(sum(calories) for calories in second_split)

def result2(myfile):
    second_split = read_input(myfile)
    totals = [sum(calories) for calories in second_split]
    return sum(sorted(totals)[-3:])
