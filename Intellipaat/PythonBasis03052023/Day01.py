#Introduced by guido van russom in 1991
#High Level Programming Language
#its widely used in DS,AI,ML,WebApp etc.
#Its Interpreted Language
#its based on Oops concept
#To execute python : Python -c[command | -m module-name |script|-] [args]
#All arguments will end up in sys.argv , sys.argv[0] always give source program's name
##Variables(int,string,float,boolean)
#rules of Variables(Keywords&Inbuilt Function name cannot be used as variable name)
#(input()--getting input from user--always it receives input as string)
#if we want to convert to int for the input() we need to do typecast int(input()),float(input()) etc)
#Datatypes(1.Basic/universal,2.Collective)
#basic/universal datatypes--Single value provided to variable(int,float,boolean,str)
#collective datatypes--(store multiple values in single variable(Mutable/Immutable))
#Mutable datatype(value of the variable will get overrided--tuple,string)
#ImMutable datatype(value of the variable wont get overrided-list,set,dict)

#dict
a={"key":"value","key2":"value2s"}
print(type(a))
b=print(a.items())
b=print(a.keys())
b=print(a.values())

#list
l=[1,2,'mani',3]
print(l)

#sets --collection of unique items which will remove duplicate data and its unordered and unindexed
s={1,5,3,3,'mani'}
print(s)
s={True,False,1,0}
print(str(s))

#conditional statement
#if
#if else
#if elif else
#nested if else

if 5>10:
    print('yes')
else:
    print('no')

if 5>13:
    print('yes')
elif 6>2:
    print('ee')
else:
    print('else')

if 20>10:
    if 6>20:
        print('the value is yes')
    elif 6>13:
        print('the value is no')
    else:
        print("get out")    
else:
    print("come out")
#looping statement
#for
#while
