def dict_comp(stop, step):
  pass

def dict_comp(stop, step):
    value= stop//step
    range_value= step *value
    number_list=[]
    num_list=[]
    answer_list=[]
    answer={}
    for number in range(1,range_value+1):
        number_list.append(number)

    for num in range(1,value+1):
        num_list.append(f'item-{num}')
   
    for i in range(0, len(number_list), 4):
        answer_list.append(number_list[i:i+step])
    i=0
    while i< len(answer_list):
        answer[num_list[i]]=answer_list[i]
        i+=1
    print(answer)
   
           
dict_comp(10, 2)
