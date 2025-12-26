
import re

css_path = "d:/Downloads/saveweb2zip-com-gabrielnavarro-com-br/post-6953.css"

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find all background-image declarations
matches = re.findall(r'background-image:\s*url\(([^)]+)\)', css_content)

print("Found background images in CSS:")
for match in matches:
    print(match)

# Look for media queries that might contain background definitions
media_queries = re.findall(r'@media\s*\([^\)]+\)\s*\{([^}]+)\}', css_content)
print("\nScanning media queries for backgrounds...")
for mq in media_queries:
    if "background-image" in mq:
        print(f"Found background in media query: {mq[:100]}...")
