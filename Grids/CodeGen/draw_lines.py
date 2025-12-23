# For tab_devn.svg, generate 5 sets of 6 lines of tab.
# x1 and x2 are always static, being the start and end of lines
# After generation, paste into tab_dev03.svg.
rows = 7      # 6 strings + 1 spacer
sets = 5
y_start = 10
y_step = 5

print('<!-- codegen inject start -->')

for s in range(sets):
    for r in range(rows):
        if r == 0:
            print("")   # spacer between staves
            continue

        y = y_start + (s * rows + r) * y_step
        print(f' <line class="std-line" x1="10" y1="{y}" x2="370" y2="{y}"/>')

print('<!-- codegen inject end -->')
