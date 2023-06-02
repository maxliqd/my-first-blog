if 3 > 2:
	print('It works')

if 5 > 3:
	print('five is bigger than three')
else: 
	print('five is not bigger than three')

name = 'Max'
if name == 'Ola':
	print('Hey Ola')
elif name == 'Max':
	print('Hey Max')
else: 
	print('Hey anonymous!')
volume = 53
if volume < 20:
	print("It's kinda quiet.")
elif 20 <= volume < 40:
	print("It's nice for background music")
elif 40<= volume <60:
	print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
	print("Nice for parties")
elif 80 <= volume < 100:
	print ("A bit loud")
else: 
	print ("My ears are hurting! :(")
# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
	volume = 50
	print("That's better!")
def hi():
	print('Hi there!')
	print('How are you?')

hi()
def hi(name):
	if name == 'Max':
		print('Hi Max')
	elif name == 'Sonja':
		print('Hello Sonja!')
	else:
		print('Hi anonymous')
	print('Bye anonymous!')

hi('Mickey Mouse')

# def hi(name):
	# print('Hi ' + name +'!')

hi("Rahel")

# def hi(name):
	# print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Sonja', 'Max']
for name in girls:
	hi(name)
	print('Next girl')

for i in range(1, 6):
	print(i)
	hi(str(i))





