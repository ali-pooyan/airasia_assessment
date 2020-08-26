def counting (target , input ):
    sum = 0
    for i in input :
        if i == target :
            sum=sum+1
    print('number count of '+target )
    print(sum)

target = 'zero'
input = ['zero','help','zero','real','none','hello']
counting(target,input)
