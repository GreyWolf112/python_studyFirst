# name = input("请输入您的名字～")
# id =input("请输入您的学号~")
#
# print(f"我的名字是{name},我的学号是{id}")
cardID = "123456"
pass_world = "123456"

cardID1 = input("请输入卡号")
pass_world1 = input("请输入密码～")

if cardID == cardID1 and pass_world == pass_world1:
    print("帐号密码正确～，请取钱")
    output_money = input("需取多少～");
    total = 10000
    over_money = total - int(output_money)
    if int(output_money) > total:
        print("余额不足～")
    elif int(output_money) > 0:
        print(f"取了{output_money}元,还剩{over_money}元")
    else:
        print("请重新输入金额")
else:
    print("帐号密码不正确，请重新输入～")
