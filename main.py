from functions import *
from findError import find_collection_error
import matplotlib.pyplot as plt
from utils import human_format

while True:
    option_input = ''
    print("Choose a function type:")
    options = [
        ['linear', linear],
        ['exponential', exponential], 
        ['sinusoidal', sinusoidal], 
        ['absolute', absolute], 
        ['ellipse', ellipse], 
        ['upside down normal', upside_normal],
        ['quadratic', quadratic]
    ]
    for i, option in enumerate(options):
        print(f'{i}: {option[0]}')
    option_input = input()
    try:
        function_name = options[int(option_input)][0]
        chosen_function = options[int(option_input)][1]
        break
    except:
        print('try again.')

number_of_samples = int(input('Number of samples to be generated: '))

single_or_multiple = int(input('Single trial or series? (S: 0, M: 1): '))
if single_or_multiple == 0: # single trial
    sample_size = int(input('Sample size: '))
    find_collection_error(
        chosen_function,
        sample_size, 
        number_of_samples,
        plot_graph=True)
    
else: # mutliple trials
    upper_limit = int(input('Upper limit n: '))+1
    list_of_err = []

    for i in range(1, upper_limit):
        list_of_err.append(
            find_collection_error(
                chosen_function,
                i, 
                number_of_samples)
        )
        
        print(f'{i}/{upper_limit-1} completed...')

    for i, err in enumerate(list_of_err):
        print(f'n={i+1}: P={round(err * 100, 2)}%')
    
    x = [i for i in range(1,upper_limit)]
    y = [100 * j for j in list_of_err]

    plt.figure(figsize=(8, 5)) 
    plt.plot(x, y)
    plt.xlabel('n')
    plt.ylabel('% error')
    plt.title(f'% error based on n ({function_name}), {human_format(number_of_samples)} samples')
    plt.grid(True)
    plt.show()
