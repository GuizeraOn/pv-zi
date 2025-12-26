
import os
import re

file_path = "d:/Downloads/saveweb2zip-com-gabrielnavarro-com-br/page_sem_timer.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Translate FAQ Questions
replacements = {
    "1. Quanto tempo eu tenho acesso ao curso?": "1. ¿Por cuánto tiempo tendré acceso al curso?",
    "2. Por onde eu recebo o acesso?": "2. ¿Por dónde recibo el acceso?",
    "3. Vou aprender a investir do zero?": "3. ¿Aprenderé a invertir desde cero?",
    "4. Quais as formas de pagamento?": "4. ¿Cuáles son las formas de pago?",
    "5. Posso confiar no curso?": "5. ¿Puedo confiar en el curso?"
}

for pt, es in replacements.items():
    if pt in content:
        content = content.replace(pt, es)
        print(f"Replaced: {pt} -> {es}")
    else:
        print(f"WARNING: Could not find '{pt}'")

# 2. Update Prices
# Anchor Price: $797,00 -> $297.90
if "$797,00" in content:
    content = content.replace("$797,00", "$297.90")
    print("Updated anchor price to $297.90")
else:
    print("WARNING: Could not find anchor price $797,00")

# 3. Update Current Price and Remove Installments
# We need to find the specific block structure and replace it.
# Structure to find and replace:
# <h2 class="elementor-heading-title elementor-size-default">12x de</h2>
# ...
# <h2 class="elementor-heading-title elementor-size-default">$19,90</h2>
# ...
# <h2 class="elementor-heading-title elementor-size-default">O <span class='text545'>$197,00 </span>al contado</h2>

# Use regex to replace the specific block more reliably regarding whitespace
# Regex to match the block:
# Note: The structure in view_file showed them in separate containers/widgets.
# It seems safer to replace specific text fragments if they are unique enough or use regex spanning lines.

# Let's try to locate the "12x de" and replace/remove the surrounding elements.
# The user wants "Preço atual: $12.90" and "Nao tem mais possibilidade de dividir".

# Strategy:
# Replace "12x de" with "Por apenas" (or empty if purely replacing values)
# Replace "$19,90" with "$12.90"
# Remove "O $197,00 al contado" block entirely or hide it.

# Let's try replacements:
if "12x de" in content:
    content = content.replace("12x de", "Por apenas")
    print("Replaced '12x de' with 'Por apenas'")

if "$19,90" in content:
    content = content.replace("$19,90", "$12.90")
    print("Updated current price to $12.90")

# Remove the "O ... al contado" line entirely or change it.
# Regex for: <h2 ...>O <span...>...</span>al contado</h2>
pattern_contado = r'<h2 class="elementor-heading-title elementor-size-default">\s*O\s*<span class=\'text545\'>\$197,00\s*</span>al contado\s*</h2>'
replacement_contado = "" # Remove it
content = re.sub(pattern_contado, replacement_contado, content)
print("Removed 'al contado' option")

# 4. Update FAQ Answer about payments (remove installments mention)
payment_faq_old = "¡Puedes inscribirte pagando hasta en 12 cuotas con tarjeta o al contado!"
payment_faq_new = "¡Puedes realizar el pago tarjeta de crédito, débito o PayPal!"

if payment_faq_old in content:
    content = content.replace(payment_faq_old, payment_faq_new)
    print("Updated Payment FAQ answer")
else:
    print("WARNING: Could not find payment FAQ answer")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished updating page_sem_timer.html")
