#####
# L11 - Loops and Iterations
#####

n=5
while n>0 :
    print(n)
    n-=1
print("Dead")
print(n)


while True:
    rstr=input("Finish me: ")    
    if rstr=="finish":
        print("Finished")
        break # break ends the loop
    print("rstr")


while True:
    rstr=input("So? ")    
    if rstr=="finish":
        print("Finished")
        break 
    elif rstr=="again":
        print("I love it")
        continue # continue jumps to the top of the loop


#####
# L12 - Iterations: Definite Loops
#####

for i in [1,2,3,4,5]:
    print(i)


friends=["Gio", "Sis", "Lil"]
for friend in friends :
    print("Hi ", friend)


#####
# L13 - Iterations: Loop Idioms
#####

largest=-1

for n in [0,4,78,2,34,9,98,11] :
    if n>largest:
        largest=n

print(largest) # max


#####
# L14 - Iterations: More Patterns
#####

# Counting
count=0
print(count)
for i in [3,4,6,34,67,43,2,1]:
    count+=1
    print(count)


# Summing
sum=0
print(sum)
for i in [3,4,6,34,67,43,2,1]:
    sum+=i
    print(sum)


# Average
count=0
sum=0
for i in [3,4,6,34,67,43,2,1]:
    count+=1
    sum+=i
    print(sum/count)


# Searching
found=False
for i in [1,8,52,45,96,3,25,7]:
    if i==25:
        found=True
        print(found, i)
        break
    print(found, i)


# Smallest
smallest=None
for i in [1,8,52,45,96,3,25,7]:
    if smallest is None:
        smallest=i
    elif i < smallest:
        smallest=i

print("Smallest ", smallest)