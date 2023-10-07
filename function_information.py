def find_true(function):
    sum = 0
    for i in range(100):
        sum += function(i+1)

    mean = sum/100

    avg_dif = 0
    for i in range(100):
        avg_dif += abs(function(i+1) - mean)

    std_dev = avg_dif/100
    return mean, std_dev

def find_sample(dataset):
    sum = 0
    for value in dataset:
        sum += value

    mean = sum/len(dataset)

    avg_dif = 0
    for value in dataset:
        avg_dif += abs(mean - value)

    std_dev = avg_dif/len(dataset) 

    return mean, std_dev
