
import os

file_path = r'd:\Downloads\saveweb2zip-com-gabrielnavarro-com-br\page_sem_timer.html'

# These are specific fixes for things that failed in the first pass due to HTML structure or previous partial replacements
fixes = [
    ("3 bônus exclusivos", "3 bonos exclusivos"),
    ("Ou <span class='text545'>$197,00 </span>à vista", "O <span class='text545'>$197,00 </span>al contado"),
    ("ENTRAR NO “DE CERO A INVERSIONISTA”", "ENTRAR AL \"DE CERO A INVERSIONISTA\""),
    ("Eu não colocaria minha reputação em risco. São milhões de seguidores, livro escrito, palestras etc. Além disso, você tem 7 días de garantía dentro do ZI!", 
     "Yo no pondría mi reputación en riesgo. Son millones de seguidores, libros escritos, conferencias, etc. Además, ¡tienes 7 días de garantía dentro del curso!")
]

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for old, new in fixes:
        if old not in content:
            print(f"Warning: Fix phrase not found: '{old}'")
        else:
            print(f"Applying fix for: '{old[:20]}...'")
        content = content.replace(old, new)
        
    # Additional cleanup if needed (e.g. any lingering "bônus" or "R$" that wasn't monetary)
    # Checking for specific 'bônus' lower case just in case
    content = content.replace("bônus", "bonos") # Safe if not inside other words? "bônus" is Portuguese. "Bonus" or "bonos" is Spanish/English.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Final translation fixes applied.")

except Exception as e:
    print(f"Error: {e}")
