def check(list1,list2):
    count = 0
    init = 0
    if len(list1) == 1 and len(list2) == 1 or len(list1) == len(list2):
        return
    if len(list1)>len(list2):
        temp1 = list1
        temp2 = list2
        for ind in range(len(temp1)):
            i = temp1[init]
            print('entered while i is', i)
            print(len(temp2),"is the temp2 len")
            if len(temp2)==1:
                print('length is one and i is :')
                print(i)
                if i in temp2:
                    print(temp2)
                    print('i is in temp2')
                    temp1.remove(i)
                    print(i,' i is removed')
                    print('temp is ',temp1)
                    if len(temp1) > 1:
                        print('More than 1 elements')
                        return
                    result = temp1[0]
                    print("Result is ",result)
                    return
                else:
                    print('i is not in temp2')
                    if temp2[0] == temp1[0] or temp2[0] != temp1[1]: 
                        result = temp1[1]
                    if temp2[0] != temp1[0] or temp2[0] == temp1[1]:
                        result = temp1[0]
                        print('result is ',result)
                        return
                    else:
                        print('error two extra element')
                        return
            try:
                if i in temp2:
                    temp1.remove(i)
                    temp2.remove(i)
                    print(i, 'removed')
                    print(temp1,temp2)
                else:
                    init+=1
            except:
                if count == 1:
                    print('second Error')
                    return 
                else:
                    print('First error')
                    init+=1
                    print(temp1,temp2)
                    count = 1
    if len(list2)>len(list1):
        temp1 = list2
        temp2 = list1
        for ind in range(len(temp1)):
            i = temp1[init]
            print('entered while i is', i)
            print(len(temp2),"is the temp2 len")
            if len(temp2)==1:
                print('length is one and i is :')
                print(i)
                if i in temp2:
                    print(temp2)
                    print('i is in temp2')
                    temp1.remove(i)
                    print(i,' i is removed')
                    print('temp is ',temp1)
                    if len(temp1) > 1:
                        print('More than 1 elements')
                        return
                    result = temp1[0]
                    print("Result is ",result)
                    return
                else:
                    print('i is not in temp2')
                    if temp2[0] == temp1[0] or temp2[0] != temp1[1]: 
                        result = temp1[1]
                    if temp2[0] != temp1[0] or temp2[0] == temp1[1]:
                        result = temp1[0]
                        print('result is ',result)
                        return
                    else:
                        print('error two extra element')
                        return
            try:
                if i in temp2:
                    temp1.remove(i)
                    temp2.remove(i)
                    print(i, 'removed')
                    print(temp1,temp2)
                else:
                    init+=1
            except:
                if count == 1:
                    print('second Error')
                    return 
                else:
                    print('First error')
                    init+=1
                    print(temp1,temp2)
                    count = 1