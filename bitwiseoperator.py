# And operation 
8 &11
print(8 &11)

#OR OPERTATION
8 &11

#right shift divide by 2
#left shift - multiply by 2

#interger inoto binary
binary_number=[1,1,1,0,0,0,1]

def binary_to_integer(nums):
    out=0
    power=0
    for i in range (len(nums)-1,-1,-1):
        if nums[i]==1:
            out +=2**power
        power+=1
    return out

binary_to_integer(binary_number)

#right shist to find binary to integer
def count_set_bits(num):
    count=0
    while num >0:
        count += num&1
        num >> 1
    return count

#setr bits
def find_different_bits(n1,n2):
    xor_res=n1^n2
    return count_set_bits(xor_res)




