from taskoneclassuserinput import UserInputValidator

instances_one = UserInputValidator()
instances_two = UserInputValidator()


num_one = ["2","3","-1","a"]
num_two = ["fhj","89","-10","1"]


check_one = instances_one.display_message(num_one)
check_one = instances_one.display_message(num_two)