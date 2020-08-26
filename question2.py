
def matching (str1,str2):

    print('pattern string is '+ str1)
    print('target string is '+ str2)
    print('index is :')
    for index,value in enumerate(str2) :
    #     print(str2[index:index+len(str1)])
        if str2[index:index+len(str1)] == str1 :
            print(index)
str1= 'aaa'
str2 = 'aaaaanaapaaa'
matching(str1,str2)
