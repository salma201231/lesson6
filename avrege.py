print("enter the marks of 5 subjects out of 100")
markone=int(input())
marktwo=int(input())
marktree=int(input())
markfour=int(input())
markfive=int(input())
Total=markone+marktwo+marktree+markfour+markfive
avg=Total/5
if avg>=91 and avg<=100:
    print("your grade is A1")
elif avg>=81 and avg<=90:
    print("your grade is A2")
elif avg>=71 and avg<=80:
    print("your grade is B1")
elif avg>=61 and avg<=70:
    print("your grade is B2")
elif avg>=51 and avg<=60:
    print("your grade is C1")
else:
    print("invalid input")