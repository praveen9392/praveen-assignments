# Day3 quesion-1

input = [1,2,3, [1,2,3,[3,4],2]]
output=[]
def flatten(input):
    for i in input:
        flatten(i) if type(i) == list else output.append(i)
    return output
print(flatten(input))

### output = [1,2,3,1,2,3,3,4,2]
        
# Day3 question-2

nested_list = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']], [['(1,2,3)', '(4,5,6)'], ['(7,8,9)', '(0,1,2)']]]
def convert_list(lst):
    for i in lst: 
        if type(i) == list:  
            convert_list(i)  
        else:
            lst[lst.index(i)] = [int(x) for x in i.strip("'()'").split(",") ] 
    return nested_list
print(convert_list(nested_list))

### output= [[[[0, 1, 2], [3, 4, 5]], [[5, 6, 7], [9, 4, 2]]], [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]]]


### Hi Sir Please let me know the inputs for my code. I am ready to take suggestions and improve further.