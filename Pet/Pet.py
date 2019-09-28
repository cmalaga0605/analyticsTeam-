constestant_1 = list(input().split())
constestant_2 = list(input().split ())
constestant_3 = list(input().split())
constestant_4  = list(input().split ())
constestant_5 = list(input().split())

sum_contestant_1 = int(constestant_1[0]) + int(constestant_1[1]) + int(constestant_1[2]) + int(constestant_1[3]) 
sum_contestant_2 = int(constestant_2[0]) + int(constestant_2[1]) + int(constestant_2[2]) + int(constestant_2[3]) 
sum_contestant_3 = int(constestant_3[0]) + int(constestant_3[1]) + int(constestant_3[2]) + int(constestant_3[3])
sum_contestant_4 = int(constestant_4[0]) + int(constestant_4[1]) + int(constestant_4[2]) + int(constestant_4[3])
sum_contestant_5 = int(constestant_5[0]) + int(constestant_5[1]) + int(constestant_5[2]) + int(constestant_5[3])

list = [sum_contestant_1 , sum_contestant_2 , sum_contestant_3 , sum_contestant_4 ,sum_contestant_5 ]

if (sum_contestant_1 > sum_contestant_2  and  sum_contestant_1 > sum_contestant_3  and sum_contestant_1 > sum_contestant_4 and sum_contestant_1 > sum_contestant_5 ):
    print(1 , sum_contestant_1)
elif (sum_contestant_2 > sum_contestant_1  and  sum_contestant_2 > sum_contestant_3  and sum_contestant_2 > sum_contestant_4 and sum_contestant_2 > sum_contestant_5 ):
    print (2 , sum_contestant_2)
elif (sum_contestant_3 > sum_contestant_1  and  sum_contestant_3 > sum_contestant_2  and sum_contestant_3 > sum_contestant_4 and sum_contestant_3 > sum_contestant_5 ):
    print (3 , sum_contestant_3)
elif (sum_contestant_4 > sum_contestant_1  and  sum_contestant_4 > sum_contestant_2 and sum_contestant_4 > sum_contestant_3 and sum_contestant_4 > sum_contestant_5 ):
    print (4 , sum_contestant_4)
elif(sum_contestant_5 > sum_contestant_1  and  sum_contestant_5 > sum_contestant_2  and sum_contestant_5 > sum_contestant_3 and sum_contestant_5 > sum_contestant_4 ):
    print(5 , sum_contestant_5)