
class ColorSortI:
    # int RED = 0
    # int WHITE = 1
    # int BLUE = 2
    def __init__(self, colors):
        self.colors_size = len(colors)
        self.ordered_colors = colors
        
    def color_array_sort(self):
        i = 0
        red_end = 0 
        blue_start = self.colors_size - 1
        while i <= blue_start:
            if self.ordered_colors[i] == 0:
                # if red
                self.swap_color(i, red_end)
                i += 1
                red_end += 1
            elif self.ordered_colors[i] == 2:
                #  if blue
                self.swap_color(i, blue_start)
                blue_start -= 1 
            else:
                i += 1
                
        return self.ordered_colors
    
    def swap_color(self, i, j):
        temp = self.ordered_colors[i]
        self.ordered_colors[i] = self.ordered_colors[j]
        self.ordered_colors[j] = temp
         
# test_array = [1, 0, 2, 1, 2, 2]
test_array = [0, 2, 0, 1, 2, 1]
# test_array = [2, 0, 2, 1, 1, 0]
result = ColorSortI(test_array).color_array_sort()
print(result)