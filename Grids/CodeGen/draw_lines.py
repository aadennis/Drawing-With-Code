# Generate 5 staves, each with 6 horizontal lines and 5 bars.
# Each bar contains 3 internal guide lines.

rows = 7       # 6 strings + 1 spacer
sets = 5
y_start = 10
y_step = 5

x1 = 10
x2 = 370

bars = 5
bar_width = (x2 - x1) / bars
guides_per_bar = 3   # internal vertical lines

print('<!-- codegen inject start v2 -->')

for s in range(sets):

    # Compute the vertical span of this stave (top of string 1 to bottom of string 6)
    stave_top = y_start + (s * rows + 1) * y_step
    stave_bottom = y_start + (s * rows + 6) * y_step

    # Spacer row
    print("")

    # Horizontal lines (6 strings)
    for r in range(1, 7):
        y = y_start + (s * rows + r) * y_step
        print(f' <line class="std-line" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>')

    # Vertical barlines + internal guides
    for b in range(bars + 1):  # +1 to draw the final right barline
        bx = x1 + b * bar_width
        print(f' <line class="std-line" x1="{bx}" y1="{stave_top}" x2="{bx}" y2="{stave_bottom}"/>')

        if b < bars:  # internal guides only inside bars
            for g in range(1, guides_per_bar + 1):
                gx = bx + (g * bar_width / (guides_per_bar + 1))
                print(f' <line class="std-line" x1="{gx}" y1="{stave_top}" x2="{gx}" y2="{stave_bottom}" '
                      f'stroke-opacity="0.3"/>')

print('<!-- codegen inject end  v2 -->')