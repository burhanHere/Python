# def devide(a,b):
#     try:
#         return float(a/b)
#     except Exception as e:
#         #by writting exception the interprator automatically detects and  store the type of error in e
#         print("Invalid Operation!!!\n",e)
#         return False
# a=devide(3, 'a')
# if a!=False:
#     print(a)

# b=[1,2,3,4]
# try:
#     print(b[7])
# except Exception as e:
#     #error is auto detected and saved in e which i then displayed in concole-window
#     print(e)


# even if you break the loop the finally block will still exicute , same is the sace with functions if we return before the finally block it will still be exicuted
# for i in range(10):
#     try:
#         print(i)
#         if i==1:
#             break
#     except:
#         print("Exception ma aa gya")
#     finally:
#         print("Finally")