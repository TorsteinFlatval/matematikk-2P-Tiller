import xml.etree.ElementTree as ET

# Register namespaces to preserve them
namespaces = {
    '': 'http://www.w3.org/2000/svg',
    'xlink': 'http://www.w3.org/1999/xlink',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'cc': 'http://creativecommons.org/ns#'
}

for prefix, uri in namespaces.items():
    ET.register_namespace(prefix, uri)

# Parse both SVG files
tree1 = ET.parse('figur1.svg')
tree2 = ET.parse('figur2.svg')

root1 = tree1.getroot()
root2 = tree2.getroot()

# Get dimensions
ns = {'svg': 'http://www.w3.org/2000/svg'}
width1 = float(root1.get('width').replace('pt', ''))
height1 = float(root1.get('height').replace('pt', ''))
width2 = float(root2.get('width').replace('pt', ''))
height2 = float(root2.get('height').replace('pt', ''))

# Total dimensions
total_width = width1 + width2
total_height = max(height1, height2)

# Create new root
merged_root = ET.Element('{http://www.w3.org/2000/svg}svg')
merged_root.set('{http://www.w3.org/1999/xlink}xlink', 'http://www.w3.org/1999/xlink')
merged_root.set('width', f'{total_width}pt')
merged_root.set('height', f'{total_height}pt')
merged_root.set('viewBox', f'0 0 {total_width} {total_height}')
merged_root.set('xmlns', 'http://www.w3.org/2000/svg')
merged_root.set('version', '1.1')

# Copy metadata from first file
for child in root1:
    if child.tag.endswith('metadata'):
        merged_root.append(child)
        break

# Copy defs from first file
for child in root1:
    if child.tag.endswith('defs'):
        merged_root.append(child)
        break

# Add white background
bg = ET.SubElement(merged_root, '{http://www.w3.org/2000/svg}rect')
bg.set('width', f'{total_width}pt')
bg.set('height', f'{total_height}pt')
bg.set('style', 'fill: #ffffff')

# Add first figure
g1 = ET.SubElement(merged_root, '{http://www.w3.org/2000/svg}g')
g1.set('transform', 'translate(0, 0)')
for child in root1:
    if child.tag.endswith('figure') or child.tag.endswith('axes'):
        g1.append(child)

# Add second figure translated
g2 = ET.SubElement(merged_root, '{http://www.w3.org/2000/svg}g')
g2.set('transform', f'translate({width1}, 0)')
for child in root2:
    if child.tag.endswith('figure') or child.tag.endswith('axes'):
        g2.append(child)

# Write output
tree = ET.ElementTree(merged_root)
tree.write('merged_figure.svg', encoding='utf-8', xml_declaration=True)

print("Merged figure created successfully: merged_figure.svg")
