import sys

def get_hour_glass_text_Int(file_path):
    """
    open a file, read as list and split to remove new line
    loop through the list, and assign it to a new list whilst splitting
    loop through the second list and cast to ints
    store the new list in the outler list
    :param file_path:
    :return: outler list
    """

    with open(file_path, 'r') as f:
        file_contents = f.read().split('\n')
        output_list = list()

        for values in file_contents:
            store_new_values = values.split()
            inner_list = []
            for num in store_new_values:
                inner_list.append(int(num))
            output_list.append(inner_list)
    return output_list

def _hourglass(arr):
    max_value = -sys.maxsize

    print(len(arr))

    for row in range(len(arr)-2):
        for col in range(len(arr) -2):
            current_val = arr[row][col] + arr[row][col+1] + arr[row][col+2] + \
                          arr[row+1][col+1] + \
                          arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if current_val > max_value:
                max_value = current_val
    print("The maximum hour glass is : ({}) ".format(max_value))
    return max_value

if __name__ =="__main__":
    text_file = get_hour_glass_text_Int('hourglass.txt')
    _hourglass(text_file)
