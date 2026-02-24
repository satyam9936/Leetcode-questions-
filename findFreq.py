freq={}
input_string="aabbcc"
for char in input_string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)