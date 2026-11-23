# day=input("请输入需要查询的工作日程")
#
# match day:
#     case "1":
#         print("开会")
#     case "2":
#         print("第二天带回")
#     case "3":
#         print("第三天带回")
#     case "4":
#         print("第四天带回")
#     case"5":
#         print("第五天带回")
#     case"6"|"7":
#         print("放假")
#     case _:
#         print(" 输入错误")

first_num = int(input("请输入第一个数字"))
second_num = int(input("请输入第二个数字"))

num = input("请输入该如何计算")

match num:
    case "+":
        print(f"两个数两个的结果为{first_num+second_num}")
    case "-":
        print(f"两个数相减的结果为{first_num-second_num}")
    case "*" :
        print(f"相乘的结果为{first_num*second_num}")
    case "/"  if second_num > 0:
        print(f"相除的结果为{first_num/second_num}")
    case _ :
        print("chongxinshuru ")