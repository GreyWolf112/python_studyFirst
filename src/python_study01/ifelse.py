# user_id ="1333";
# password= "123456"
#
# user_id1 =input("请输入帐号～")
# password1 = input("请输入密码～")
#
# if user_id ==user_id1 and password==password1:
#     print("登录成功～")
# else:
#     print("用户名或帐号密码错误，请重新输入～")



# year = int(input("请输入年份"))
#
# if year % 100 !=0 or year % 400 ==0:
#     print(f"{year}闰年")
# else:
#     print(f"{year}平年")

# num = int(input("请输入数字"))
#
# if num == 0:
#     print("等于零")
# elif num <0:
#     print("负数")
# else:
#     print("正数")

first_length=int(input("diyi"))
second_length=int(input("dier"))
third_length=int(input("disan"))

xingzhuang =False
if (first_length+second_length)>third_length and (third_length+first_length)>second_length and (second_length+third_length)>first_length:
    xingzhuang = True
    if xingzhuang:
        if first_length ==second_length ==third_length:
            print("等边三角形")
        elif first_length == second_length or second_length == third_length or third_length == first_length:
            print("等腰三角形")
        else:
            print("普通三角形")

else:
     print("不是三角形")

