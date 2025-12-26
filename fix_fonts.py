
import os
import requests
import re

# Configuration
base_dir = r'd:\Downloads\saveweb2zip-com-gabrielnavarro-com-br'
fonts_dir = os.path.join(base_dir, 'fonts')
css_file_path = os.path.join(base_dir, 'post-6953.css')
html_file_path = os.path.join(base_dir, 'page_sem_timer.html')

# Font URLs to download (extracted from CSS inspection)
font_urls = [
    "https://gabrielnavarro.com.br/wp-content/uploads/2024/09/HelveticaNowDisplay-Regular.woff2",
    "https://gabrielnavarro.com.br/wp-content/uploads/2024/09/HelveticaNowDisplay-Medium.woff2",
    "https://gabrielnavarro.com.br/wp-content/uploads/2024/09/HelveticaNowDisplay-Bold.woff2",
    "https://gabrielnavarro.com.br/wp-content/uploads/2024/09/ArchimotoV01-Regular.woff2",
    "https://gabrielnavarro.com.br/wp-content/uploads/2024/09/ArchimotoV01-Medium.woff2",
    "https://gabrielnavarro.com.br/wp-content/uploads/2024/09/ArchimotoV01-Black.woff2"
]

# Create fonts directory
if not os.path.exists(fonts_dir):
    os.makedirs(fonts_dir)
    print(f"Created directory: {fonts_dir}")

# Download fonts
for url in font_urls:
    filename = url.split('/')[-1]
    save_path = os.path.join(fonts_dir, filename)
    
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Saved to {save_path}")
        else:
            print(f"Failed to download {url}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Modify CSS file to point to local fonts
try:
    with open(css_file_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Regex to replace URL with local path
    # We replace the full URL with just 'fonts/FILENAME'
    # Pattern: url\('https://gabrielnavarro.com.br/wp-content/uploads/2024/09/([^']+)'\)
    # We only care about .woff2 mostly but formatting covers all if we are smart.
    # Actually, let's just replace the specific known base URL prefix.
    
    base_url_pattern = "https://gabrielnavarro.com.br/wp-content/uploads/2024/09/"
    new_css_content = css_content.replace(base_url_pattern, "fonts/")
    
    with open(css_file_path, 'w', encoding='utf-8') as f:
        f.write(new_css_content)
    print("Updated post-6953.css to use local fonts.")

except Exception as e:
    print(f"Error updating CSS file: {e}")

# Modify HTML to use local CSS file
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Replace the remote link to post-6953.css with local file
    # Remote: https://gabrielnavarro.com.br/wp-content/uploads/elementor/css/post-6953.css?ver=...
    # We need a regex because of the version parameter
    
    html_content = re.sub(
        r'href=[\'"]https://gabrielnavarro\.com\.br/wp-content/uploads/elementor/css/post-6953\.css[^"\']*[\'"]', 
        'href="post-6953.css"', 
        html_content
    )
    
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Updated page_sem_timer.html to link to local post-6953.css")

except Exception as e:
    print(f"Error updating HTML file: {e}")
