
import os

file_path = r'd:\Downloads\saveweb2zip-com-gabrielnavarro-com-br\page_sem_timer.html'

replacements = [
    ("ESSE VÍDEO SAI DO AR HOJE, 22/12/2025", "¡ESTE VIDEO DEJARÁ DE ESTAR DISPONIBLE HOY, 22/12/2025!"),
    ("CONDIÇÃO ESPECIAL DE BLACK FRIDAY!", "¡CONDICIÓN ESPECIAL DE BLACK FRIDAY!"),
    ("Nos próximos 7 dias você começará a construir a sua", "¡En los próximos 7 días comenzarás a construir tu"),
    ("renda vitalícia", "patrimonio para toda la vida"),
    ("Para você não entende nada sobre investimentos, mas quer fazer o dinheiro render com segurança e praticidade.", "Ideal para ti que no entiendes nada sobre inversiones, pero quieres hacer que tu dinero rinda con seguridad y practicidad."),
    ("GARANTIR MINHA VAGA", "ASEGURAR MI CUPO"),
    ("Nas próximas semanas você vai:", "En las próximas semanas vas a:"),
    ("CONTEÚDO", "CONTENIDO"),
    ("Saber onde investir para tirar da poupança e da conta corrente", "Saber dónde invertir para sacar tu dinero del banco y de la cuenta de ahorros tradicional"),
    ("Vencer a inflação e ver o seu dinheiro rendendo de verdade", "Vencer a la inflación y ver cómo tu dinero crece de verdad"),
    ("Começar a investir de forma simples, segura e rentável", "Empezar a invertir de forma simple, segura y rentable"),
    ("Fazer seu dinheiro trabalhar por você", "Hacer que tu dinero trabaje para ti"),
    ("Receber rendimentos passivos na sua conta todos os meses", "Recibir ingresos pasivos en tu cuenta todos los meses"),
    ("Ter quase o dobro de rentabilidade da poupança. com extrema segurança", "Tener casi el doble de rentabilidad que una cuenta de ahorros, con extrema seguridad"),
    ("Esse é o preço da ignorância", "Este es el precio de la ignorancia"),
    ("para você e sua família", "para ti y tu familia"),
    ("Estar no ciclo da pobreza hoje não é culpa sua. Mas continuar a partir de hoje, é. Seguir o mesmo caminho de 99% das pessoas será uma decisão sua, se não começar a investir hoje.", "Estar en el ciclo de la pobreza hoy no es tu culpa. Pero continuar ahí a partir de hoy, sí lo es. Seguir el mismo camino del 99% de las personas será tu decisión si no empiezas a invertir hoy."),
    ("FONTE: IBGE", "FUENTE: Estadísticas Oficiales"),
    ("Previdência social no Brasil", "El sistema de pensiones"),
    ("SITUAÇÃO DOS NOSSOS APOSENTADOS", "SITUACIÓN DE NUESTROS JUBILADOS"),
    ("Dependem de parentes", "Dependen de parientes"),
    ("Dependem de caridade", "Dependen de la caridad"),
    ("São obrigados a trabalhar", "Están obligados a seguir trabajando"),
    ("São independentes", "Son independientes"),
    ("Porque agora a venda caiu dos seus olhos e você sabe a diferença entre só economizar, colocar na poupança e investir da maneira correta.", "Porque ahora se te cayó la venda de los ojos y conoces la diferencia entre solo guardar dinero, dejarlo en el banco e invertir de la manera correcta."),
    ("Projeção", "Proyección"),
    ("R$200 por mês em 30 anos", "$200 por mes en 30 años"),
    ("Economizando", "Guardando efectivo"),
    ("Poupança", "Cuenta de Ahorros"),
    ("Investindo", "Invirtiendo"),
    ("R$500 por mês em 30 anos", "$500 por mes en 30 años"),
    ("Isso considerando uma rentabilidade de 12% ao ano. Extremamente conservadora.", "Esto considerando una rentabilidad del 12% anual. Extremadamente conservadora."),
    ("3 bônus exclusivos para você que entrar hoje", "3 bonos exclusivos para ti que entres hoy"),
    ("para você que entrar hoje", "para ti que entres hoy"),
    ("Minhas planilhas", "Mis plantillas"),
    ("Todas as minhas planilhas de organização financeira, planejamento e investimentos também serão suas, de bônus.", "Todas mis plantillas de organización financiera, planificación e inversiones también serán tuyas, como bono."),
    ("Imersão EUA", "Inmersión EE.UU."),
    ("Um guia prático e uma imersão exclusiva sobre investimentos nos EUA. Você saberá como proteger e multiplicar o seu patrimônio investindo nas maiores empresas do mundo (e em dólar).", "Una guía práctica y una inmersión exclusiva sobre inversiones en EE.UU. Sabrás cómo proteger y multiplicar tu patrimonio invirtiendo en las empresas más grandes del mundo (y en dólares)."),
    ("Acesso vitalício", "Acceso vitalicio"),
    ("O do Zero a Investidor já está ridículo de barato por 1 ano. Mas eu vou tornar a sua decisão ainda mais fácil. Porque você, que entrar hoje por essa página, vai ter acesso vitalício ao treinamento.", "El programa \"De Cero a Inversionista\" ya está ridículamente barato por 1 año. Pero voy a hacer tu decisión aún más fácil. Porque tú, que entres hoy a través de esta página, tendrás acceso de por vida al entrenamiento."),
    ("Entrando hoje, na condição dessa página você leva:", "Entrando hoy con la condición de esta página te llevas:"),
    ("DO ZERO A INVESTIDOR", "DE CERO A INVERSIONISTA"),
    ("Mude sua realidade através dos investimentos.", "Cambia tu realidad a través de las inversiones."),
    ("7 dias de garantia", "7 días de garantía"),
    ("Se dentro do prazo de 7 dias ver que o treinamento não é para você, basta enviar um e-mail para nosso suporte.", "Si dentro del plazo de 7 días ves que el entrenamiento no es para ti, basta con enviar un e-mail a nuestro soporte."),
    ("De R$797,00", "De $797,00"),
    ("12x de", "12x de"),
    ("R$19,90", "$19,90"),
    ("Ou R$197,00 à vista", "O $197,00 al contado"),
    ("Mais de 30 aulas", "Más de 30 clases"),
    ("Três bônus especiais", "Tres bonos especiales"),
    ("Garantia 7 Dias", "Garantía de 7 días"),
    ("ENTRAR NO “DO ZERO A INVESTIDOR”", "ENTRAR AL \"DE CERO A INVERSIONISTA\""),
    ("Perguntas Frequentes", "Preguntas Frecuentes"),
    ("O acesso normal do ZI é de 1 ano. Mas você que entrar através dessa página, terá acesso VITALÍCIO.", "El acceso normal del curso es de 1 año. Pero tú, que entras a través de esta página, tendrás acceso VITALICIO (de por vida)."),
    ("Assim que você finalizar sua inscrição, você recebe um email com o seu acesso da Hotmart!", "¡Tan pronto finalices tu inscripción, recibirás un email de Hotmart con tu acceso!"),
    ("Sim, esse é o meu curso para iniciantes que estão começando agora, do zero e querem começar a investir nos próximos 7 dias.", "Sí, este es mi curso para principiantes que están empezando ahora, desde cero, y quieren comenzar a invertir en los próximos 7 días."),
    ("Você pode se inscrever pagando em até 12x no cartão ou à vista no PIX!", "¡Puedes inscribirte pagando hasta en 12 cuotas con tarjeta o al contado!"),
    ("Eu não colocaria minha reputação em risco. São milhões de seguidores, livro escrito, palestras etc. Além disso, você tem 7 dias de garantia dentro do ZI!", "Yo no pondría mi reputación en riesgo. Son millones de seguidores, libros escritos, conferencias, etc. Además, ¡tienes 7 días de garantía dentro del curso!"),
    ("DO ZERO AO INVESTIDOR", "DE CERO A INVERSIONISTA"),
    ("TODOS OS DIREITOS RESERVADOS", "TODOS LOS DERECHOS RESERVADOS"),
    ("TERMOS DE USO", "TÉRMINOS DE USO"),
    ("POLÍTICA DE PRIVACIDADE", "POLÍTICA DE PRIVACIDAD")
]

# Currency value replacements (simplified to avoid messing up other things)
# Performing these at the end
currency_replacements = [
    ("R$77.000,00", "$77.000,00"),
    ("R$231.015,88", "$231.015,88"),
    ("R$878.741,03", "$878.741,03"),
    ("R$185.000,00", "$185.000,00"),
    ("R$532.370,40", "$532.370,40"),
    ("R$1.927.230,27", "$1.927.230,27"),
    ("R$797,00", "$797,00"),
    ("R$197,00", "$197,00")
]

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply text replacements
    for old, new in replacements:
        if old not in content:
            print(f"Warning: Phrase not found: '{old}'")
        content = content.replace(old, new)
        
    # Apply currency replacements
    for old, new in currency_replacements:
        content = content.replace(old, new)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Translation completed successfully.")

except Exception as e:
    print(f"Error: {e}")
