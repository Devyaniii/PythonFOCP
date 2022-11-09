def sweet_division():
    total_sweets = int(input("How many sweets? "))
    stds = int(input("Number of Student Present in Class? "))
    each_std_gets = int(total_sweets / stds)
    left_over = total_sweets % stds
    return(f"Each Student will get {each_std_gets} sweets. \nleft over sweets are {left_over}.")
    
print(sweet_division())
