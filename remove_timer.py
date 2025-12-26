
import os

input_path = r'd:\Downloads\saveweb2zip-com-gabrielnavarro-com-br\page.html'
output_path = r'd:\Downloads\saveweb2zip-com-gabrielnavarro-com-br\page_sem_timer.html'

try:
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the 'esconder' class to make everything visible immediately
    new_content = content.replace('esconder', '')
    
    # Also attempt to set the JS delay to 0 just in case there are other checks
    # Logic: '6942d5fb33e6f31e497e4912': { delay: 845 } -> delay: 0
    # A simple regex replace might be safer but string replace covers the class name which is the main CSS blocker.
    # The JS will still run but if the class is gone, CSS won't hide it.
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully created {output_path}")

except Exception as e:
    print(f"Error: {e}")
