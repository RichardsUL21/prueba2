import streamlit as st
import pandas as pd
from datetime import datetime
import random
import time

# Configuración de la página
st.set_page_config(
    page_title="Software Libre vs Software Privativo - Presentación",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para un diseño profesional
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .slide-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        min-height: 500px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .slide-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .slide-subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        text-align: center;
        margin-bottom: 3rem;
        opacity: 0.9;
    }
    
    .slide-content {
        font-size: 1.2rem;
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .example-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: #333;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .example-card:hover {
        transform: translateY(-5px);
    }
    
    .libre-card {
        border-left: 5px solid #28a745;
    }
    
    .privativo-card {
        border-left: 5px solid #dc3545;
    }
    
    .software-name {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }
    
    .software-description {
        color: #666;
        margin-bottom: 1rem;
    }
    
    .comparison-table {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    .quiz-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .quiz-question {
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        color: #333;
    }
    
    .correct-answer {
        background-color: #d4edda !important;
        border-color: #c3e6cb !important;
        color: #155724 !important;
    }
    
    .incorrect-answer {
        background-color: #f8d7da !important;
        border-color: #f5c6cb !important;
        color: #721c24 !important;
    }
    
    .navigation-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .nav-button {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        border: 2px solid white;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .nav-button:hover {
        background: white;
        color: #764ba2;
    }
    
    .feature-list {
        list-style: none;
        padding: 0;
    }
    
    .feature-list li {
        padding: 0.5rem 0;
        display: flex;
        align-items: center;
    }
    
    .feature-list li:before {
        content: "✓";
        color: #28a745;
        font-weight: bold;
        margin-right: 1rem;
        font-size: 1.2rem;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        text-align: center;
    }
    
    .stat-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 10px;
        min-width: 150px;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# Datos de ejemplos de software
EJEMPLOS_SOFTWARE = {
    "libre": [
        {
            "nombre": "Linux",
            "descripcion": "Sistema operativo de código abierto",
            "categoria": "Sistema Operativo",
            "ventajas": ["Gratuito", "Personalizable", "Seguro", "Gran comunidad"],
            "ejemplos_distros": ["Ubuntu", "Debian", "Fedora", "Arch Linux"]
        },
        {
            "nombre": "LibreOffice",
            "descripcion": "Suite ofimática completa",
            "categoria": "Productividad",
            "ventajas": ["Compatible con MS Office", "Multiplataforma", "Sin licencias"],
            "componentes": ["Writer", "Calc", "Impress", "Draw"]
        },
        {
            "nombre": "Firefox",
            "descripcion": "Navegador web enfocado en privacidad",
            "categoria": "Navegador",
            "ventajas": ["Privacidad", "Extensiones", "Código abierto", "Multiplataforma"]
        },
        {
            "nombre": "GIMP",
            "descripcion": "Editor de imágenes profesional",
            "categoria": "Diseño Gráfico",
            "ventajas": ["Potente", "Plugins", "Gratuito", "Profesional"]
        },
        {
            "nombre": "VLC Media Player",
            "descripcion": "Reproductor multimedia universal",
            "categoria": "Multimedia",
            "ventajas": ["Reproduce todo", "Sin códecs adicionales", "Ligero"]
        }
    ],
    "privativo": [
        {
            "nombre": "Windows",
            "descripcion": "Sistema operativo de Microsoft",
            "categoria": "Sistema Operativo",
            "desventajas": ["Licencia costosa", "Código cerrado", "Vulnerabilidades"],
            "versiones": ["Windows 10", "Windows 11"]
        },
        {
            "nombre": "Microsoft Office",
            "descripcion": "Suite ofimática líder del mercado",
            "categoria": "Productividad",
            "desventajas": ["Suscripción mensual", "Dependencia del proveedor"],
            "componentes": ["Word", "Excel", "PowerPoint", "Outlook"]
        },
        {
            "nombre": "Adobe Photoshop",
            "descripcion": "Editor de imágenes profesional",
            "categoria": "Diseño Gráfico",
            "desventajas": ["Muy costoso", "Suscripción obligatoria", "Pesado"]
        },
        {
            "nombre": "Google Chrome",
            "descripcion": "Navegador web de Google",
            "categoria": "Navegador",
            "desventajas": ["Recopila datos", "Consume mucha RAM", "Privacidad limitada"]
        },
        {
            "nombre": "macOS",
            "descripcion": "Sistema operativo de Apple",
            "categoria": "Sistema Operativo",
            "desventajas": ["Solo en hardware Apple", "Costoso", "Ecosistema cerrado"]
        }
    ]
}

# Preguntas del quiz
QUIZ_QUESTIONS = [
    {
        "pregunta": "¿Cuál es la principal diferencia entre software libre y privativo?",
        "opciones": [
            "El precio",
            "La libertad de modificar y distribuir el código",
            "La calidad del software",
            "El soporte técnico"
        ],
        "respuesta_correcta": 1,
        "explicacion": "El software libre permite a los usuarios ejecutar, copiar, distribuir, estudiar, modificar y mejorar el software."
    },
    {
        "pregunta": "¿Cuál de estos es un ejemplo de software libre?",
        "opciones": [
            "Microsoft Windows",
            "Adobe Photoshop",
            "LibreOffice",
            "macOS"
        ],
        "respuesta_correcta": 2,
        "explicacion": "LibreOffice es una suite ofimática de código abierto y software libre."
    },
    {
        "pregunta": "¿Qué ventaja principal ofrece el software libre?",
        "opciones": [
            "Siempre es más rápido",
            "Libertad de uso y modificación",
            "Mejor interfaz gráfica",
            "Más publicidad"
        ],
        "respuesta_correcta": 1,
        "explicacion": "El software libre ofrece libertad completa para usar, estudiar, modificar y distribuir el software."
    },
    {
        "pregunta": "¿Cuál es una desventaja común del software privativo?",
        "opciones": [
            "Es gratuito",
            "Código abierto",
            "Dependencia del proveedor",
            "Demasiadas actualizaciones gratuitas"
        ],
        "respuesta_correcta": 2,
        "explicacion": "El software privativo crea dependencia del proveedor y no permite modificaciones del código."
    },
    {
        "pregunta": "¿Qué sistema operativo es software libre?",
        "opciones": [
            "Windows 11",
            "macOS Ventura",
            "Ubuntu Linux",
            "iOS"
        ],
        "respuesta_correcta": 2,
        "explicacion": "Ubuntu es una distribución de Linux, que es software libre y de código abierto."
    }
]

# Inicializar estado de la sesión
if 'slide_number' not in st.session_state:
    st.session_state.slide_number = 0
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_answered' not in st.session_state:
    st.session_state.quiz_answered = False
if 'show_quiz' not in st.session_state:
    st.session_state.show_quiz = False
if 'quiz_responses' not in st.session_state:
    st.session_state.quiz_responses = {}

# Función para cambiar de diapositiva
def change_slide(direction):
    if direction == "next" and st.session_state.slide_number < 4:
        st.session_state.slide_number += 1
    elif direction == "prev" and st.session_state.slide_number > 0:
        st.session_state.slide_number -= 1

# Función para mostrar el quiz
def show_quiz():
    st.session_state.show_quiz = True
    st.session_state.slide_number = 5

# Contenido de las diapositivas
def render_slide(slide_num):
    if slide_num == 0:
        # Diapositiva 1: Título
        st.markdown("""
        <div class="slide-container">
            <h1 class="slide-title">Software Libre vs Software Privativo</h1>
            <p class="slide-subtitle">Ejemplos y Comparación Profesional</p>
            <div class="stats-container">
                <div class="stat-item">
                    <div class="stat-number">5</div>
                    <div class="stat-label">Ejemplos Libres</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">5</div>
                    <div class="stat-label">Ejemplos Privativos</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">10</div>
                    <div class="stat-label">Minutos</div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 2rem;">
                <p style="font-size: 1.1rem; opacity: 0.8;">Estudiante 7 - 2da Ronda de Exposiciones</p>
                <p style="opacity: 0.7;">{}</p>
            </div>
        </div>
        """.format(datetime.now().strftime("%d de %B, %Y")), unsafe_allow_html=True)
    
    elif slide_num == 1:
        # Diapositiva 2: Definiciones
        st.markdown("""
        <div class="slide-container">
            <h2 class="slide-title">¿Qué es Software Libre y Privativo?</h2>
            <div class="slide-content">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 3rem;">
                    <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 15px;">
                        <h3 style="color: #4CAF50; margin-bottom: 1rem;">🔓 Software Libre</h3>
                        <p>Software que respeta la libertad de los usuarios y la comunidad. Los usuarios tienen la libertad de ejecutar, copiar, distribuir, estudiar, modificar y mejorar el software.</p>
                        <ul class="feature-list" style="margin-top: 1rem;">
                            <li>Código fuente accesible</li>
                            <li>Libertad de modificación</li>
                            <li>Distribución permitida</li>
                            <li>Sin restricciones de uso</li>
                        </ul>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 15px;">
                        <h3 style="color: #f44336; margin-bottom: 1rem;">🔒 Software Privativo</h3>
                        <p>Software que no es libre o de código abierto. El usuario tiene limitaciones en su uso, modificación y distribución según los términos de la licencia.</p>
                        <ul class="feature-list" style="margin-top: 1rem;">
                            <li style="color: #ffcccc;">❌ Código fuente oculto</li>
                            <li style="color: #ffcccc;">❌ Modificación prohibida</li>
                            <li style="color: #ffcccc;">❌ Distribución restringida</li>
                            <li style="color: #ffcccc;">❌ Licencias restrictivas</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif slide_num == 2:
        # Diapositiva 3: Ejemplos de Software Libre
        st.markdown("""
        <div class="slide-container" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);">
            <h2 class="slide-title">Ejemplos de Software Libre</h2>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, software in enumerate(EJEMPLOS_SOFTWARE["libre"]):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="example-card libre-card">
                    <h3 class="software-name">🔓 {software['nombre']}</h3>
                    <p class="software-description">{software['descripcion']}</p>
                    <p><strong>Categoría:</strong> {software['categoria']}</p>
                    <p><strong>Ventajas:</strong></p>
                    <ul>
                        {"".join([f"<li>{v}</li>" for v in software['ventajas']])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    
    elif slide_num == 3:
        # Diapositiva 4: Ejemplos de Software Privativo
        st.markdown("""
        <div class="slide-container" style="background: linear-gradient(135deg, #fc466b 0%, #3f5efb 100%);">
            <h2 class="slide-title">Ejemplos de Software Privativo</h2>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(2)
        for i, software in enumerate(EJEMPLOS_SOFTWARE["privativo"]):
            with cols[i % 2]:
                st.markdown(f"""
                <div class="example-card privativo-card">
                    <h3 class="software-name">🔒 {software['nombre']}</h3>
                    <p class="software-description">{software['descripcion']}</p>
                    <p><strong>Categoría:</strong> {software['categoria']}</p>
                    <p><strong>Consideraciones:</strong></p>
                    <ul>
                        {"".join([f"<li>{d}</li>" for d in software['desventajas']])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    
    elif slide_num == 4:
        # Diapositiva 5: Comparación
        st.markdown("""
        <div class="slide-container" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <h2 class="slide-title">Comparación Directa</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Crear tabla comparativa
        comparison_data = {
            "Característica": [
                "Costo de Licencia",
                "Código Fuente",
                "Modificación",
                "Distribución",
                "Soporte",
                "Seguridad",
                "Personalización",
                "Dependencia"
            ],
            "Software Libre": [
                "✅ Generalmente gratuito",
                "✅ Accesible y auditable",
                "✅ Permitida y fomentada",
                "✅ Libre distribución",
                "⚡ Comunidad activa",
                "✅ Transparente y auditable",
                "✅ Total libertad",
                "✅ Sin vendor lock-in"
            ],
            "Software Privativo": [
                "❌ Pago por licencia",
                "❌ Oculto y protegido",
                "❌ Prohibida",
                "❌ Restringida por licencia",
                "💰 Soporte comercial",
                "❓ Confianza en el proveedor",
                "❌ Limitada o nula",
                "❌ Dependencia del proveedor"
            ]
        }
        
        df = pd.DataFrame(comparison_data)
        st.markdown("<div class='comparison-table'>", unsafe_allow_html=True)
        st.table(df)
        st.markdown("</div>", unsafe_allow_html=True)

# Función principal de la aplicación
def main():
    # Sidebar
    with st.sidebar:
        st.markdown("## 📊 Panel de Control")
        st.markdown("### Navegación de Diapositivas")
        
        # Mostrar progreso
        progress = (st.session_state.slide_number + 1) / 5
        st.progress(progress)
        st.markdown(f"**Diapositiva {st.session_state.slide_number + 1} de 5**")
        
        # Botones de navegación en sidebar
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Anterior", use_container_width=True):
                change_slide("prev")
        with col2:
            if st.button("➡️ Siguiente", use_container_width=True):
                change_slide("next")
        
        st.markdown("---")
        
        # Índice de diapositivas
        st.markdown("### 📑 Índice")
        slides = [
            "1. Portada",
            "2. Definiciones",
            "3. Software Libre",
            "4. Software Privativo",
            "5. Comparación"
        ]
        for i, slide in enumerate(slides):
            if i == st.session_state.slide_number:
                st.markdown(f"**▶️ {slide}**")
            else:
                if st.button(slide, key=f"nav_{i}"):
                    st.session_state.slide_number = i
        
        st.markdown("---")
        
        # Botón para actividad complementaria
        st.markdown("### 🎮 Actividad Complementaria")
        if st.button("🧠 Iniciar Quiz Interactivo", type="primary", use_container_width=True):
            show_quiz()
        
        # Información adicional
        st.markdown("---")
        st.markdown("### ℹ️ Información")
        st.info("""
        **Tiempo estimado:** 10 minutos
        
        **Objetivo:** Comprender las diferencias entre software libre y privativo mediante ejemplos reales.
        
        **Actividad:** Quiz interactivo al final
        """)
    
    # Contenido principal
    if not st.session_state.show_quiz:
        # Mostrar diapositiva actual
        render_slide(st.session_state.slide_number)
        
        # Botones de navegación inferior
        st.markdown("""
        <div class="navigation-buttons">
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.session_state.slide_number > 0:
                if st.button("⬅️ Diapositiva Anterior"):
                    change_slide("prev")
        
        with col3:
            if st.session_state.slide_number < 4:
                if st.button("Siguiente Diapositiva ➡️"):
                    change_slide("next")
            else:
                if st.button("🎮 Ir al Quiz", type="primary"):
                    show_quiz()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        # Mostrar Quiz
        st.markdown("""
        <div class="slide-container" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <h2 class="slide-title">🧠 Quiz Interactivo</h2>
            <p class="slide-subtitle">Pon a prueba tus conocimientos</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quiz
        st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
        
        if not st.session_state.quiz_answered:
            score = 0
            
            for i, q in enumerate(QUIZ_QUESTIONS):
                st.markdown(f"<h3 class='quiz-question'>Pregunta {i+1}: {q['pregunta']}</h3>", 
                           unsafe_allow_html=True)
                
                user_answer = st.radio(
                    "",
                    options=q['opciones'],
                    key=f"q_{i}",
                    label_visibility="collapsed"
                )
                
                st.session_state.quiz_responses[i] = user_answer
                
                st.markdown("---")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("📝 Enviar Respuestas", type="primary", use_container_width=True):
                    st.session_state.quiz_answered = True
                    # Calcular puntuación
                    for i, q in enumerate(QUIZ_QUESTIONS):
                        if st.session_state.quiz_responses.get(i) == q['opciones'][q['respuesta_correcta']]:
                            score += 1
                    st.session_state.quiz_score = score
                    st.rerun()
        
        else:
            # Mostrar resultados
            st.markdown(f"""
            <div style="text-align: center; padding: 2rem;">
                <h2 style="color: #333;">🎯 Resultados del Quiz</h2>
                <h1 style="font-size: 4rem; color: #4CAF50;">
                    {st.session_state.quiz_score}/{len(QUIZ_QUESTIONS)}
                </h1>
                <p style="font-size: 1.2rem; color: #666;">
                    ¡{"Excelente trabajo!" if st.session_state.quiz_score >= 4 else "Buen intento!"}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Mostrar respuestas correctas
            st.markdown("### 📚 Revisión de Respuestas")
            for i, q in enumerate(QUIZ_QUESTIONS):
                user_ans = st.session_state.quiz_responses.get(i)
                correct_ans = q['opciones'][q['respuesta_correcta']]
                is_correct = user_ans == correct_ans
                
                st.markdown(f"""
                <div style="background: {'#d4edda' if is_correct else '#f8d7da'}; 
                            padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                    <h4>Pregunta {i+1}: {q['pregunta']}</h4>
                    <p><strong>Tu respuesta:</strong> {user_ans} 
                       {' ✅' if is_correct else ' ❌'}</p>
                    {f'<p><strong>Respuesta correcta:</strong> {correct_ans}</p>' if not is_correct else ''}
                    <p style="font-style: italic; color: #666; margin-top: 0.5rem;">
                        {q['explicacion']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Botón para reiniciar
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🔄 Reiniciar Presentación", type="secondary", use_container_width=True):
                    st.session_state.slide_number = 0
                    st.session_state.quiz_answered = False
                    st.session_state.show_quiz = False
                    st.session_state.quiz_responses = {}
                    st.session_state.quiz_score = 0
                    st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>Software Libre vs Software Privativo - 2da Ronda de Exposiciones</p>
        <p style="font-size: 0.9rem;">Creado con Streamlit 🚀 | Código disponible en GitHub</p>
    </div>
    """, unsafe_allow_html=True)

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
