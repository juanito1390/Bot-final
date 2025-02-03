import discord
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
#############
diccionarioAgua = {
    1: "Cerrar la llave mientras te cepillas los dientes para evitar el desperdicio de agua, ya que una llave abierta puede desperdiciar hasta 10 litros por minuto.",
    2: "Reparar fugas y goteos en tuberías y grifos para reducir el consumo innecesario de agua, pues una pequeña fuga puede desperdiciar cientos de litros al mes.",
    3: "Recolectar agua de lluvia para regar plantas y jardines, lo que ayuda a reducir el uso de agua potable y aprovechar un recurso natural gratuito.",
    4: "Utilizar sistemas de riego por goteo en lugar de aspersores para minimizar la evaporación y optimizar el uso del agua en la jardinería.",
    5: "Lavar el coche con un balde en lugar de usar una manguera para ahorrar agua, ya que una manguera puede gastar hasta 500 litros en un solo lavado.",
    6: "Optar por electrodomésticos eficientes en el consumo de agua, como lavadoras y lavavajillas ecológicos, que utilizan menos agua sin comprometer su funcionamiento.",
    7: "Usar detergentes biodegradables para evitar contaminar el agua con sustancias químicas nocivas que afectan ríos, lagos y ecosistemas acuáticos.",
    8: "No verter aceites ni productos químicos en el desagüe para evitar la contaminación del agua, ya que un solo litro de aceite puede contaminar hasta 1,000 litros de agua.",
    9: "Reducir el uso de agua caliente, ya que su producción consume más energía y agua, lo que contribuye a la reducción del consumo eléctrico y las emisiones de carbono.",
    10: "Promover campañas de concienciación sobre el ahorro de agua en la comunidad, incentivando hábitos responsables y el uso eficiente de este recurso vital."
}

diccionarioTierra = {
    1: "Utilizar abonos orgánicos y evitar los fertilizantes químicos para mejorar la salud del suelo y prevenir la contaminación de los mantos acuíferos.",
    2: "Practicar la rotación de cultivos para mantener la fertilidad del suelo y evitar el agotamiento de los nutrientes esenciales para las plantas.",
    3: "Evitar la deforestación y promover la reforestación para conservar los ecosistemas, protegiendo la biodiversidad y reduciendo la erosión del suelo.",
    4: "Minimizar el uso de pesticidas para proteger la biodiversidad del suelo, ya que estos productos pueden dañar microorganismos esenciales para la fertilidad.",
    5: "Recolectar y aprovechar residuos orgánicos para producir compost, lo que ayuda a reducir los desechos y mejorar la calidad del suelo de manera natural.",
    6: "Usar técnicas de agricultura sostenible como la agroforestería, combinando cultivos con árboles para mejorar la productividad y reducir la degradación del suelo.",
    7: "Evitar la sobreexplotación de recursos naturales y fomentar el uso responsable del suelo para garantizar su conservación a largo plazo.",
    8: "Proteger humedales y cuerpos de agua para conservar la calidad del suelo, ya que estos ecosistemas regulan la humedad y previenen la desertificación.",
    9: "Evitar la erosión plantando coberturas vegetales en zonas vulnerables, lo que ayuda a fijar el suelo y mantener su estructura natural.",
    10: "Promover la educación sobre la importancia del suelo en la sostenibilidad ambiental, concienciando a las nuevas generaciones sobre su conservación."
}

diccionarioAire = {
    1: "Reducir el uso de vehículos particulares optando por transporte público, bicicleta o caminatas, disminuyendo la emisión de gases contaminantes y el tráfico.",
    2: "Usar combustibles limpios y preferir energías renovables para reducir emisiones contaminantes, disminuyendo así el impacto del cambio climático.",
    3: "Plantar árboles y mantener áreas verdes, ya que absorben dióxido de carbono y producen oxígeno, mejorando la calidad del aire y regulando la temperatura.",
    4: "Evitar la quema de basura, hojas secas o madera, ya que liberan gases tóxicos al aire que pueden causar enfermedades respiratorias y afectar la capa de ozono.",
    5: "Usar productos de limpieza y aerosoles ecológicos que no contengan compuestos químicos volátiles, evitando la contaminación del aire en espacios cerrados y abiertos.",
    6: "Revisar y dar mantenimiento regular a los vehículos para reducir la emisión de gases contaminantes, mejorando su eficiencia y reduciendo su impacto ambiental.",
    7: "Reducir el uso de calefacción y aire acondicionado para disminuir el consumo de energía y las emisiones de gases de efecto invernadero.",
    8: "Evitar el uso excesivo de plástico, ya que su producción y quema liberan sustancias dañinas al aire, contribuyendo a la contaminación ambiental.",
    9: "Apoyar regulaciones ambientales que busquen reducir la contaminación del aire, promoviendo leyes y normativas que incentiven el uso de tecnologías limpias.",
    10: "Concientizar a la comunidad sobre la importancia de mantener el aire limpio y promover buenas prácticas que ayuden a mejorar la calidad del ambiente."
}

hello = ["https://media.giphy.com/media/3oKIPsx2VAYAgEHC12/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g", 
         "https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g", 
         "https://media.giphy.com/media/dzaUX7CAG0Ihi/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g", 
         "https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif?cid=ecf05e47iufwqgmwcn9eluxk4cx8m1wrgovqxiwqotai1lpb&ep=v1_gifs_search&rid=giphy.gif&ct=g", 
         "https://media.giphy.com/media/XO8RMtRaK73isIt0i2/giphy.gif?cid=ecf05e47iufwqgmwcn9eluxk4cx8m1wrgovqxiwqotai1lpb&ep=v1_gifs_search&rid=giphy.gif&ct=g", 
         "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif?cid=790b7611dakcsz6m2255bq773ott40bay7pi1scj2kcnff8q&ep=v1_gifs_search&rid=giphy.gif&ct=g"
         ]
comandos = ["$hola  -  hola",
            "$cuidar_agua  -  Acciones para cuidar el agua",
            "$cuidar_tierra  -  Acciones para cuidar la tierra en el medio ambiente",
            "$cuidar_aire  -  Acciones para cudar el aire"
            ]
#mandar con enter
com = "\n".join(comandos)

# 0-agua    1- aire        2-   tierra
articulos = {
    "agua": "https://www.fundacionaquae.org/consejos-para-cuidar-del-agua/",
    "tierra": "https://elpais.com/planeta-futuro/2025-02-02/milpa-la-huerta-ancestral.html",
    "aire": "https://www.huffingtonpost.es/sociedad/los-cientificos-piden-dejes-freir.html"
}
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #comandos
    if message.content.startswith('$comandos'):
        await message.channel.send(com)
    #saludo con gif
    elif message.content.startswith("$hola"):
        await message.channel.send(random.choice(hello))
    #funcion aleatoria

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #funcion aleatorio
    def aleatorioselecc(diccionario, cant = 1):
        return random.sample(list(diccionario.values()), cant)
    #pregunta si o no
    async def preguntar_mas(message,tema):
        await message.channel.send("¿Quieres más información sobre esto?")
        def check(m):
            return m.author == message.author and m.channel == message.channel and m.content.lower() in ["sí", "no"]
        try:
            respuesta = await client.wait_for("message", check=check, timeout=30)
            if respuesta.content.lower() == "sí":
                await message.channel.send(articulos[tema])
            else:
                await message.channel.send("Oh, ok :(")
                await message.channel.send("https://media.giphy.com/media/ISOckXUybVfQ4/giphy.gif")
        except:
            await message.channel.send("No respondiste a tiempo. 😞")


    if message.content.startswith("$cuidar_agua"):
        agua = aleatorioselecc(diccionarioAgua)
        await message.channel.send("".join(agua))
        await preguntar_mas(message, "agua")
        
    elif message.content.startswith("$cuidar_tierra"):
        tierra = aleatorioselecc(diccionarioTierra)
        await message.channel.send("".join(tierra))
        await preguntar_mas(message, "tierra")
       
    elif message.content.startswith("$cuidar_aire"):
        aire = aleatorioselecc(diccionarioAire)
        await message.channel.send("".join(aire))
        await preguntar_mas(message, "aire")
        


client.run("MTMzNTYzNjMxMjg1Mzg0NDA4OQ.GBNpu1.sU44DyhzGG9xFZt_-_NMwA0TC9JvtXZfTBXvhI")