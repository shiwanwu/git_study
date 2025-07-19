# BMI = wight / (height ** 2)

weight = int(input("请输入您的体重(kg): "))
height = float(input("请输入您的身高(m): "))
bmi = weight / (height ** 2)
print("您的BMI指数为:" + str(round(bmi, 2)))

