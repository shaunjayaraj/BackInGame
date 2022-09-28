hanging_on_wall = "{0} green bottles hanging on the wall,\n{1} green bottles hanging on the wall,\nAnd if {2} green bottle should accidentally fall,\nThere’ll be {3} green bottles hanging on the wall. \n"
number_to_name = {1:'One', 2:"Two", 3:"Three", 4:"Four", 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 0:'Zero', 10:'Ten'}
doodie = list(map(lambda num: print(hanging_on_wall.format((number_to_name[num]),(number_to_name[num]),(number_to_name[1]),(number_to_name[num-1]))),range(10,0, -1)))

