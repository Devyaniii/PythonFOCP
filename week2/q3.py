stud=int(input("how many students?"))
group_size=int(input("required group size?"))
groups= stud//group_size
left= stud% group_size
print("There will be",groups,"groups with",left,"student left over.")