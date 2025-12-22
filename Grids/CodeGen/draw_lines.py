# For tab_devn.svg, generate 5 sets of 6 lines of tab.
# x1 and x2 are always static, being the start and end of lines
# After generation, paste into tab_dev03.svg.
rows = 7 # 6 lines plus 1 spacer row
sets = 5
x = 20
width = 60
height = 40
y_start = 10
y_step = 5 # increment between rows

print(f'<!-- codegen inject start -->')
for i in range(sets * rows):
    y1 = y_start + i * y_step
    # text_y = y + height // 2 + 2  # center vertically; tweak offset if needed
    if i%rows == 0 and i != 0:
        # print(f"{i}")
        print("")
        continue
    print(f' <line class="std-line" x1="10" y1="{y1}" x2="370" y2="{y1}"/>')
print(f'<!-- codegen inject end -->')    

