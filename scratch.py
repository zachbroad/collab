VAR = (1, 2, "hey")

def func(age, day, greeting):
    print(age, day, greeting)


func(VAR[0], VAR[1], VAR[2])
func(*VAR)
