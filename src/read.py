# function to read from degree files
def read_vec_2(path, seperator):
    list1 = []
    list2 = []
    fr = open(path,'r')
    for line in fr:
        arr = line.strip().split(seperator)
        x1 = int(arr[0])
        x2 = int(arr[1])
        list1.append(x1)
        list2.append(x2)
    fr.close()
    return (list1, list2)
