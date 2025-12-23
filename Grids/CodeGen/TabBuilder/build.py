from generate_tab import generate_tab_lines

template_path ='Grids/CodeGen/TabBuilder/template.svg'
output_path = "tab_output.svg"

start_tag = "<!-- codegen inject start v2 -->"
end_tag = "<!-- codegen inject end v2 -->"

# Read template
template = open(template_path).read()

# Generate new block
generated = generate_tab_lines()

# Split template around the injection markers
before = template.split(start_tag)[0]
after = template.split(end_tag)[1]

# Reassemble final SVG
output = (
    before
    + start_tag + "\n"
    + generated + "\n"
    + end_tag
    + after
)

# Write output file
with open(output_path, "w") as f:
    f.write(output)

print("Generated:", output_path)