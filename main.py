def min_n_variables(elements):
    min_v = elements[1] 
    for x in elements:
        if x < min_v:
            min_v = x
    return min_v

# elements = [6**6, 7**5, 5**7]
elements = [5,1,9,0,7]

assert mim_n_variables (elements) == 1