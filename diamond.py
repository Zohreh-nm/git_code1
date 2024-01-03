def print_star_line(number_of_stars, total_stars):
    number_of_spaces = (total_stars - number_of_stars) // 2
    print(f"{' '* number_of_spaces}{'*' * number_of_stars}{' ' * number_of_spaces}")
    
def draw_diamond(num):
    for i in range(num):
        if i < num / 2:
            print_star_line((i * 2 + 1), num)
        else:
            print_star_line(((num - i) * 2 - 1), num)
            
draw_diamond(7)
            