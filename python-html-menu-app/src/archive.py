from flask import Blueprint, render_template

archive_bp = Blueprint('archive', __name__)

# Diccionario con información sobre dispositivos eléctricos
archive_data = {
    "baterias": {
        "titulo": "Baterías",
        "descripcion": "Dispositivos que almacenan y suministran energía eléctrica de manera portátil.",
        "categoria": "Alimentación y protección"
    },
    "portapilas": {
        "titulo": "Portapilas",
        "descripcion": "Soportes para alojar y conectar baterías o pilas en un circuito.",
        "categoria": "Alimentación y protección"
    },
    "fusibles": {
        "titulo": "Fusibles",
        "descripcion": "Dispositivos de protección que se funden para interrumpir el paso de corriente en caso de sobrecarga.",
        "categoria": "Alimentación y protección"
    },
    "reguladores_7805": {
        "titulo": "Reguladores de voltaje (ej. 7805)",
        "descripcion": "Componentes que mantienen un voltaje constante en el circuito.",
        "categoria": "Alimentación y protección"
    },
    "diodos_proteccion": {
        "titulo": "Diodos de protección",
        "descripcion": "Diodos usados para evitar daños por polaridad inversa o picos de voltaje.",
        "categoria": "Alimentación y protección"
    },
    "leds": {
        "titulo" : "LEDs",
        "descripcion": "Un LED (Light Emitting Diode o diodo emisor de luz) es un componente electrónico que, al ser atravesado por corriente eléctrica en el sentido correcto, emite luz. A diferencia de una bombilla tradicional, no funciona por calentamiento de un filamento, sino por un proceso llamado electroluminiscencia en el material semiconductor.",
        "categoria": "Componentes de salida"
    },
    "Pantallas LCD u OLED": {
        "titulo": "Pantallas LCD u OLED",
        "descripcion": "Una pantalla LCD (Liquid Crystal Display) y una pantalla OLED (Organic Light Emitting Diode) son dispositivos electrónicos de salida que permiten mostrar texto, números, gráficos e incluso imágenes en proyectos de electrónica.",
        "categoria": "Componentes de salida",
    },
    "buzzer": {
        "titulo": "Buzzer",
        "descripcion": "Un buzzer es un dispositivo electrónico de salida de audio que convierte la energía eléctrica en sonido. Se usa mucho en proyectos con Arduino para emitir pitidos, alarmas o tonos musicales simples.",
        "categoria": "Componentes de salida",
    },
    "motores_dc": {
        "titulo": "Motores DC",
        "descripcion": "Un motor DC pequeño es un dispositivo electromecánico que convierte la energía eléctrica de corriente directa (DC) en movimiento mecánico giratorio.",
        "categoria": "Componentes de salida",
    },
    "Servomotores": {
        "titulo": "Servomotores",
        "descripcion": "Un servomotor es un dispositivo electromecánico que convierte la energía eléctrica en movimiento mecánico controlado con alta precisión.",
        "categoria": "Componentes de salida",
    },
    "motores_paso_a_paso": {
        "titulo": "Motores paso a paso",
        "descripcion": "Un motor paso a paso es un dispositivo electromecánico que convierte la energía eléctrica en movimiento mecánico giratorio en pasos discretos y controlados.",
        "categoria": "Componentes de salida",
    },
    "relevadores": {
        "titulo": "Relevadores",
        "descripcion": "Un relevador es un interruptor electromecánico que permite controlar un circuito eléctrico mediante una señal de baja potencia.",
        "categoria": "Componentes de salida",
    },
    "Resistores": {
        "titulo": "Resistores",
        "descripcion": "Un resistor es un componente electrónico pasivo que se utiliza para limitar o regular el flujo de corriente eléctrica en un circuito.",  
        "categoria": "componentes de control/pasivo",
    },
    "potenciometros": {
        "titulo": "Potenciómetros",
        "descripcion": "Un potenciómetro es un tipo de resistor variable que permite ajustar manualmente la resistencia en un circuito eléctrico.",
        "categoria": "componentes de control/pasivo",
    },
    "condensadores": {
        "titulo": "Condensadores",
        "descripcion": "Un condensador es un componente electrónico pasivo que almacena energía en forma de campo eléctrico entre dos placas conductoras separadas por un material dieléctrico.",
        "categoria": "componentes de control/pasivo",
    },
    "interruptores y pulsadores": {
        "titulo": "Interruptores y pulsadores",
        "descripcion": "Un interruptor es un dispositivo que permite abrir o cerrar un circuito eléctrico, controlando el flujo de corriente. Un pulsador es un tipo de interruptor momentáneo que solo mantiene el circuito cerrado mientras se presiona.",
        "categoria": "componentes de control/pasivo",
    },
    "LDR": {
        "titulo": "LDR (Light Dependent Resistor)",
        "descripcion": "Una LDR es un tipo de resistor cuya resistencia varía en función de la cantidad de luz que incide sobre su superficie. A mayor luz, menor resistencia, y viceversa.",
        "categoria": "componentes de control/pasivo",
    },
    "Sensor de temperatura (LM35, DHT11, DHT22)": {
        "titulo": "Sensor de temperatura (LM35, DHT11, DHT22)",
        "descripcion": "Un sensor de temperatura es un dispositivo que mide la temperatura del entorno y convierte esa información en una señal eléctrica que puede ser leída por un microcontrolador como Arduino.",
        "categoria": "Sensores",
    },
    "sensor de humedad": {
        "titulo": "Sensor de humedad",
        "descripcion": "Un sensor de humedad es un dispositivo que mide la cantidad de vapor de agua en el aire o en un material específico y convierte esa información en una señal eléctrica que puede ser leída por un microcontrolador como Arduino.",
        "categoria": "Sensores",
    },
    "Sensor ultrasónico (HC-SR04)": {
        "titulo": "Sensor ultrasónico (HC-SR04)",
        "descripcion": "Un sensor ultrasónico es un dispositivo que utiliza ondas sonoras de alta frecuencia para medir la distancia entre el sensor y un objeto u obstáculo.",
        "categoria": "Sensores",
    },
    "Sensor de movimiento PIR": {
        "titulo": "Sensor de movimiento PIR",
        "descripcion": "Un sensor de movimiento PIR (Passive Infrared Sensor) es un dispositivo que detecta cambios en la radiación infrarroja emitida por objetos en su campo de visión, permitiendo identificar la presencia o movimiento de personas u animales.",
        "categoria": "Sensores",
    },
    "Sensor de gas (MQ-2, MQ-7, etc.)": {
        "titulo": "Sensor de gas (MQ-2, MQ-7, etc.)",
        "descripcion": "Un sensor de gas es un dispositivo que detecta la presencia y concentración de gases específicos en el aire, como humo, monóxido de carbono, metano, entre otros.",
        "categoria": "Sensores",
    },
    "Sensor infrarrojo": {
        "titulo": "Sensor infrarrojo",
        "descripcion": "Un sensor infrarrojo es un dispositivo que detecta la radiación infrarroja emitida por objetos en su campo de visión, permitiendo identificar la presencia o movimiento de personas u objetos.",
        "categoria": "Sensores",    
    },
    "Sensor de sonido (micrófonos electret o digitales)": {
        "titulo": "Sensor de sonido (micrófonos electret o digitales)",
        "descripcion": "Un sensor de sonido es un dispositivo que detecta ondas sonoras en el ambiente y convierte esas ondas en señales eléctricas que pueden ser procesadas por un microcontrolador como Arduino.",
        "categoria": "Sensores",
    },
    "Módulos Bluetooth (HC-05, HC-06)": {
        "titulo": "Módulos Bluetooth (HC-05, HC-06)",
        "descripcion": "Un módulo Bluetooth es un dispositivo que permite la comunicación inalámbrica entre dispositivos a corta distancia utilizando la tecnología Bluetooth.",
        "categoria": "Comunicación",
    },
    "Módulos WiFi (ESP8266, ESP32)": {
        "titulo": "Módulos WiFi (ESP8266, ESP32)",
        "descripcion": "Un módulo WiFi es un dispositivo que permite la conexión de un microcontrolador como Arduino a una red WiFi para enviar y recibir datos a través de Internet.",
        "categoria": "Comunicación",
    },
    "Módulos RF 433 MHz": {
        "titulo": "Módulos RF 433 MHz",
        "descripcion": "Un módulo RF 433 MHz es un dispositivo que permite la comunicación inalámbrica entre dispositivos utilizando ondas de radio en la frecuencia de 433 MHz.",
        "categoria": "Comunicación",    
    },
    "Módulos RFID": {
        "titulo": "Módulos RFID",
        "descripcion": "Un módulo RFID es un dispositivo que permite la lectura y escritura de etiquetas RFID (Radio Frequency Identification) para identificar y rastrear objetos de forma inalámbrica.",
        "categoria": "Comunicación",
    }
}
# ...otros dispositivos...
def get_archive_item(item_id):
    # Devuelve la información de un ítem específico
    return archive_data.get(item_id, {
        "titulo": "No encontrado",
        "descripcion": "El dispositivo no existe.",
        "categoria": ""
    })

def get_archive_list():
    # Devuelve una lista de todos los ítems del archivero
    return [{"id": k, **v} for k, v in archive_data.items()]