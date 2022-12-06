test="""test=hi
test1=bye"""

test = test.split('\n')
for x in range(len(test)):
    print(test[x].split('='))