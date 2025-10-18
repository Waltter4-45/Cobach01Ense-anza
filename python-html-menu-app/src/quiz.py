import random

def get_quiz_questions():
    quiz_questions = [
        {
            "pregunta": "¿Qué componente electrónico emite luz cuando circula corriente en un solo sentido?",
            "opciones": ["Resistor", "Condensador", "Fusible", "LED"],
            "respuesta": "LED"
        },
        {
            "pregunta": "¿Qué dispositivo se utiliza para mostrar números con siete segmentos en forma de barras LED?",
            "opciones": ["Pantalla OLED", "Display de 7 segmentos", "potenciometro", "buzzer"],
            "respuesta": "Display de 7 segmentos"
        },
        {
            "pregunta": "¿Qué pantalla utiliza cristales líquidos y retroiluminación para mostrar información?",
            "opciones": ["Pantalla LCD", "Relé", "LDR", "LED"],
            "respuesta": "Pantalla LCD"
        },
        {
            "pregunta": "¿Qué tipo de pantalla tiene cada píxel que emite su propia luz, logrando alto contraste?",
            "opciones": ["OLED", "LCD", "Motor", "Resistor"],
            "respuesta": "OLED"
        },
        {
            "pregunta": "¿Qué dispositivo pequeño produce sonidos simples como pitidos o alarmas?",
            "opciones": ["Buzzer", "LED", "Condensador", "Relé"],
            "respuesta": "Buzzer"
        },
        {
            "pregunta": "¿Qué componente convierte energía eléctrica en movimiento giratorio en su eje?",
            "opciones": ["Motor DC", "LDR", "Fusible", "Resistor"],
            "respuesta": "Motor DC"
        },
        {
            "pregunta": "¿Qué dispositivo permite controlar el paso de corriente ajustando manualmente la resistencia?",
            "opciones": ["Potenciómetro", "Condensador", "LED", "Relé"],
            "respuesta": "Potenciómetro"
        },
        {
            "pregunta": "¿Qué componente mide la temperatura y es muy usado en Arduino (ej. LM35, DHT11)?",
            "opciones": ["Sensor de temperatura", "LDR", "Fusible", "Buzzer"],
            "respuesta": "Sensor de temperatura"
        },
        {
            "pregunta": "¿Qué sensor detecta obstáculos y mide distancias usando ultrasonido?",
            "opciones": ["Sensor ultrasónico", "Motor", "Resistor", "LED"],
            "respuesta": "Sensor ultrasónico"
        },
        {
            "pregunta": "¿Qué sensor reacciona a la luz cambiando su resistencia según la intensidad luminosa?",
            "opciones": ["LDR", "Condensador", "Fusible", "Relé"],
            "respuesta": "LDR"
        },
        {
            "pregunta": "¿Qué componente almacena carga eléctrica temporalmente y se usa para suavizar señales?",
            "opciones": ["Condensador", "Resistor", "LED", "Buzzer"],
            "respuesta": "Condensador"
        },
        {
            "pregunta": "¿Qué módulo inalámbrico permite comunicación con Arduino usando Bluetooth?",
            "opciones": ["Módulo Bluetooth", "Pantalla LCD", "Motor DC", "Fusible"],
            "respuesta": "Módulo Bluetooth"
        },
        {
            "pregunta": "¿Qué módulo se usa para conexión WiFi en proyectos con Arduino, como el ESP8266?",
            "opciones": ["Módulo WiFi", "Relé", "LDR", "LED"],
            "respuesta": "Módulo WiFi"
        },
        {
            "pregunta": "¿Qué dispositivo abre o cierra un circuito de forma manual para controlar el paso de electricidad?",
            "opciones": ["Interruptor", "Sensor de gas", "Buzzer", "Condensador"],
            "respuesta": "Interruptor"   
        },
        {
            "pregunta": "¿Qué sensor detecta movimiento de personas por radiación infrarroja?",
            "opciones": ["Sensor PIR", "Potenciómetro", "Fusible", "Motor DC"],
            "respuesta": "Sensor PIR"
        },
        {
            "pregunta": "¿Qué componente electrónico básico limita la cantidad de corriente en un circuito?",
            "opciones": ["Resistor", "LED", "Relé", "Pantalla OLED"],
            "respuesta": "Resistor"
        },
        {
            "pregunta": "¿Qué módulo se usa para leer tarjetas y llaveros de identificación por radiofrecuencia?",
            "opciones": ["Módulo RFID", "Sensor ultrasónico", "Buzzer", "LDR"],
            "respuesta": "Módulo RFID"
        },
        {
            "pregunta": "¿Qué sensor detecta gases como humo o monóxido de carbono (ej. MQ-2, MQ-7)?",
            "opciones": ["Sensor de gas", "Motor DC", "Condensador", "LED"],
            "respuesta": "Sensor de gas"
        },
        {
            "pregunta": "¿Qué dispositivo se utiliza para emitir o recibir señales infrarrojas en un control remoto?",
            "opciones": ["Emisor/Receptor IR", "Fusible", "Resistor", "Pantalla LCD"],
            "respuesta": "Emisor/Receptor IR"
        },
        {
            "pregunta": "Qué componente electrónico protege un circuito cortando el paso de corriente cuando hay sobrecarga?",
            "opciones": ["Fusible", "Relé", "Buzzer", "Sensor PIR"],
            "respuesta": "Fusible"
        }
    ]
    
    random.shuffle(quiz_questions)
    for q in quiz_questions:
        random.shuffle(q["opciones"])
    return quiz_questions

def get_quiz_results(user_answers, questions):
    correct = 0
    total = len(questions)
    for i, q in enumerate(questions):
        user_answer = user_answers.get(f"question_{i}")
        if user_answer and user_answer.strip().lower() == q["respuesta"].strip().lower():
            correct += 1
    score = round((correct / total) * 100, 2)
    return {
        "correct_answers": correct,
        "total_questions": total,
        "score": score
    }