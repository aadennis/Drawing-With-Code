# Generate 6 stacked <rect> and <text> elements for SVG
# After generation, paste into stacked_text_01.svg
rows = 6
x = 20
width = 80
height = 50
y_start = 20
y_step = 54  # increment between rows

labels = ["1/E", "2/B", "3/G", "4/D", "5/A", "6/E"]

for i in range(rows):
    y = y_start + i * y_step
    text_y = y + height // 2 + 2  # center vertically; tweak offset if needed
    print(f'  <rect class="box" x="{x}" y="{y}" width="{width}" height="{height}"/>')
    print(f'  <text class="label" x="{x + width//2}" y="{text_y}">{labels[i]}</text>')
