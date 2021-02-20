### Java vs. Python ###

# while loops

# Java
# int x = 0;
# while (x < 5) {
#   System.out.print(x + " ");
#   x++;
# }

# Python
# x = 0
# while x<5:
#     print(x, end = " ")
#     x+=1

# for loops

# Java
# for (int i = 0; i < 5; i++) {
#   System.out.print(i + " ");
# }

# Python
# range goes from 0 to whatever is in range, exclusive
# can also put a starting value ex. range (2,10)
# increment range(2, 10, 3)
# for x in range(5):
#     print(x, end = " ")

# for-each loops, break and continue statements

# Java
# int[] array = {1,2,3,4};
# for(i in array) {
#   System.out.print(i + " ");
# }

# Python
# list = [1,2,3,4]
# for x in list:
#     if x == 3:
# can replace break with continue
#         break
#     print(x, end=" ")

# Python ONLY: else off of for loop
# else body is execute if the loop is iterated fully
# in this ex., if x == 3, then else will never be executed
# for x in range(5):
#     if x == 6:
#         break
# else:
#     print('else entered')

