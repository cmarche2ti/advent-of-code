input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0"

input_list = [int(val) for val in input.split(",")]

input_list[1]=12
input_list[2]=2


for i in range(0,len(input_list)+1, 4):
    optcode = input_list[i]
    print(i)
    # print(optcode, input_list[i+1], input_list[i+2], input_list[i+3])
    if optcode == 1:
        print(optcode)
        input_list[input_list[i+3]] = input_list[input_list[i+1]]+input_list[input_list[i+2]]
        
    elif optcode == 2:
        print(optcode)
        input_list[input_list[i+3]] = input_list[input_list[i+1]]*input_list[input_list[i+2]]
        
    elif optcode == 99:
        print(optcode)
        break
    else:
        print("something went wrong")
    print(input_list)

print(input_list)