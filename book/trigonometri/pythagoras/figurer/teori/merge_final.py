with open('figur1.svg', 'r') as f:
    fig1_content = f.read()

with open('figur2.svg', 'r') as f:
    fig2_content = f.read()

# Extract the content between <g id="figure_1"> and </g>
import re

fig1_match = re.search(r'<g id="figure_1">(.*?)</g>\s*<defs>', fig1_content, re.DOTALL)
fig1_inner = fig1_match.group(1) if fig1_match else ""

fig2_match = re.search(r'<g id="figure_1">(.*?)</g>\s*<defs>', fig2_content, re.DOTALL)
fig2_inner = fig2_match.group(1) if fig2_match else ""

# Extract defs from both
fig1_defs_match = re.search(r'<defs>(.*?)</defs>', fig1_content, re.DOTALL)
fig1_defs = fig1_defs_match.group(1) if fig1_defs_match else ""

fig2_defs_match = re.search(r'<defs>(.*?)</defs>', fig2_content, re.DOTALL)
fig2_defs = fig2_defs_match.group(1) if fig2_defs_match else ""

# Extract clipPath from both
fig1_clip_match = re.search(r'<clipPath[^>]*>.*?</clipPath>', fig1_content, re.DOTALL)
fig1_clip = fig1_clip_match.group(0) if fig1_clip_match else ""

fig2_clip_match = re.search(r'<clipPath[^>]*>.*?</clipPath>', fig2_content, re.DOTALL)
fig2_clip = fig2_clip_match.group(0) if fig2_clip_match else ""

# Calculate dimensions
width1 = 226.068
width2 = 207.443571
total_width = width1 + width2
height = 262.238571

# Create merged SVG
merged_svg = f'''<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="{total_width}pt" height="{height}pt" viewBox="0 0 {total_width} {height}" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2026-03-02</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.9.1, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{{stroke-linejoin: round; stroke-linecap: butt}}</style>
  {fig1_defs}{fig2_defs}
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 {height}
L {total_width} {height}
L {total_width} 0
L 0 0
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1_left" transform="translate(0, 0)">
   {fig1_inner}
  </g>
  <g id="axes_1_right" transform="translate({width1}, 0)">
   {fig2_inner}
  </g>
 </g>
 <defs>
  {fig1_clip}
  {fig2_clip}
 </defs>
</svg>
'''

with open('merged_figure.svg', 'w') as f:
    f.write(merged_svg)

print("Merged figure created successfully: merged_figure.svg")
