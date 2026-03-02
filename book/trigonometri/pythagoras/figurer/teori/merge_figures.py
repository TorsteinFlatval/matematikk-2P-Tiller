import xml.etree.ElementTree as ET

# Register namespaces
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')

# Parse SVG files
tree1 = ET.parse('figur1.svg')
tree2 = ET.parse('figur2.svg')

root1 = tree1.getroot()
root2 = tree2.getroot()

# Get width and height
width1 = float(root1.get('width').replace('pt', ''))
height1 = float(root1.get('height').replace('pt', ''))
width2 = float(root2.get('width').replace('pt', ''))

# Create new merged SVG root
total_width = width1 + width2
merged_root = ET.Element('svg', {
    'xmlns': 'http://www.w3.org/2000/svg',
    'xmlns:xlink': 'http://www.w3.org/1999/xlink',
    'version': '1.1',
    'width': f'{total_width}pt',
    'height': f'{height1}pt',
    'viewBox': f'0 0 {total_width} {height1}'
})

# Create group for first figure
g1 = ET.SubElement(merged_root, 'g', {'transform': 'translate(0, 0)'})
# Copy all children from first SVG
for child in root1:
    g1.append(child)

# Create group for second figure, translated to the right
g2 = ET.SubElement(merged_root, 'g', {'transform': f'translate({width1}, 0)'})
# Copy all children from second SVG
for child in root2:
    g2.append(child)

# Write merged SVG
tree = ET.ElementTree(merged_root)
tree.write('merged_figure.svg', encoding='utf-8', xml_declaration=True)

print("Merged figure saved: merged_figure.svg")
