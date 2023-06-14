#Tu day hoi nang cao =)))

#Generator
#tao ra nhung k luu lai -> giam bo nho
def square_nums(list_nums):
    for x in list_nums:
        yield x*x

list_nums = [1,2,3,4]
generated = square_nums(list_nums)
print(next(generated))
print(next(generated))
print(next(generated))
print(next(generated))
