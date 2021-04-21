from functools import reduce


xs = [1,1,2,2]
ys = [2,2,3,3]
zs = [3,3,4,4]


def make_count(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc

#my own original logic
def combination_dict(right, left):
    result = {}
    for k in right.keys():
        for a in left.keys():
            if k == a:
                result[k] = right.get(k,0) + left.get(a,0)
                # print(result)
            else:
                if k not in result.keys(): 
                    result[k] = right.get(k)
                if a not in result.keys():
                    result[a] = left.get(a)
                # print(result)
            
    return result
    
#implimentation using Set
def combination_dict1(right, left):
    
    keys = set(right.keys()).union(set(left.keys()))
    result = {key : right.get(key, 0) + left.get(key, 0) for key in keys}
    return result
    


d_xs = reduce(make_count, xs, {})
d_ys = reduce(make_count, ys, {})
d_zs = reduce(make_count, zs, {})

print(d_xs)
print(d_ys)
print(d_zs)

result = combination_dict1(combination_dict(d_xs, d_ys), d_zs)
print(result)


