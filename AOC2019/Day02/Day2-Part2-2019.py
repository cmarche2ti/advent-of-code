PROGRAM = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]

# input_list = [int(val) for val in input.split(",")]
# # print(input)
# # print(input_list)
# # print(len(input_list))
# target = 19690720

# def output(a, b, l):
#     print(l)
#     l[1]= a
#     l[2]= b
    
#     for num in range(0,len(l)+1, 4):
#         optcode = l[num]
#         # try:
#         #     if optcode == 99:
#         #         break
#         #     elif optcode == 1:
#         #         print(optcode)
#         #         l[l[num+3]] = l[l[num+1]]+l[l[num+2]]
#         #     elif optcode == 2:    
#         #         print(optcode)
#         #         l[l[num+3]] = l[l[num+1]]*l[l[num+2]] 
#         #     else:
#         #         print(optcode)
#         #         print("something went wrong")
#         # except:
#         #     print('something went wrong')
#     return l[0]

# # for i in range(30):
# #     for j in range(30):
# #         test = output(i, j, input_list)
# #         if  test == target:
# #             print(i,j, "You got it")
# #             break
# #         else:
# #             print(i, j, "Try again")


# print(output(3,4,input_list))

# Grus solution to part 1
from typing import List
Program = List[int]

def run(program: Program) -> None:
    pos = 0
    while program[pos] != 99: # halt
        opcode, loc1, loc2, loc3 = program[pos], program[pos+1], program[pos+2], program[pos+3]
        if opcode ==1:
            program[loc3]= program[loc1] + program[loc2]
        elif opcode == 2:
            program[loc3]= program[loc1] * program[loc2]
        else:
            raise RuntimeError(f'invalid opcode: {opcode}')
        pos += 4

prog1 = [1,0,0,0,99]; run(prog1); assert prog1 == [2,0,0,0,99]
prog2 = [2,3,0,3,99];  run(prog2); assert prog2 == [2,3,0,6,99]
prog3 = [2,4,4,5,99,0]; run(prog3); assert prog3 == [2,4,4,5,99,9801]
prog4 = [1,1,1,4,99,5,6,0,99]; run(prog4); assert prog4 == [30,1,1,4,2,5,6,0,99]

def alarm(program: Program, noun: int = 12, verb: int = 2) -> int:
    program = program[:]
    program[1] = noun
    program[2] = verb
    run(program)
    return program[0]

# print(alarm(PROGRAM))

target = 19690720

for noun in range(100):
    for verb in range(100):
        output = alarm(PROGRAM, noun, verb)
        if output == target:
            print(noun, verb, 100*noun+verb)
            break


