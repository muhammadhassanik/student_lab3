import numpy as np

def standardise_loop(data):
    rows = len(data)
    cols = len(data[0])
    result = [[0.0] * cols for _ in range(rows)]
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += data[i][j]
        mean = col_sum / rows
        
        var_sum = 0
        for i in range(rows):
            var_sum += (data[i][j] - mean) ** 2
        std = (var_sum / rows) ** 0.5
        
        for i in range(rows):
            result[i][j] = (data[i][j] - mean) / std
    return result

def standardise_np(data):
    return (data - data.mean(axis=0)) / data.std(axis=0)