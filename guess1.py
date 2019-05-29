import random
r = random.randint(1, 100)
count = 0 #计数
while True:
	count = count + 1#+=也行
	num = input('请输入你所猜的数字： ')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('这是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这是你猜的第', count, '次')