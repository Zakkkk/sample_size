from numpy import std

def find_mean(vals_array):
    return sum(vals_array)/len(vals_array)

def expected_results(func, start=0, end=100):
    vals_array = []
    for i in range(start,end):
        vals_array.append(func(i))
    return find_mean(vals_array), std(vals_array)

def sort_into_categories(array, min=0, max=150):
    frequencies = [0 for i in range(min, max+1)]

    for number in array:
        # print(f'{round(number)} is being tested...')
        frequencies[round(number) - round(min)] += 1
        # print('worked!')
    return frequencies

def percentage_error(arr, func, samples_size):
    avg_diff = 0
    for index, number in enumerate(arr):
        avg_diff += abs(number - func(index))
    return avg_diff / samples_size

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()
