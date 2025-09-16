import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Configuración de la página
st.set_page_config(
  page_title="📋 Ejemplos: Software Libre vs Privado",
  page_icon="🖥️",
  layout="wide",
  initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
  .main-header {
      text-align: center;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 2rem;
      border-radius: 15px;
      margin-bottom: 2rem;
      color: white;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .software-card {
      background: white;
      padding: 1.5rem;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      margin: 1rem 0;
      border-left: 4px solid;
      transition: transform 0.3s ease;
  }
  
  .libre-card {
      border-left-color: #28a745;
      background: linear-gradient(135deg, #f8fff9 0%, #e8f5e8 100%);
  }
  
  .privado-card {
      border-left-color: #dc3545;
      background: linear-gradient(135deg, #fff8f8 0%, #ffe8e8 100%);
  }
  
  .quiz-card {
      background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
      padding: 2rem;
      border-radius: 15px;
      margin: 1rem 0;
      border-left: 4px solid #2196f3;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .quiz-correct {
      background: #d4edda;
      border: 1px solid #c3e6cb;
      color: #155724;
      padding: 1rem;
      border-radius: 8px;
      margin: 0.5rem 0;
      animation: fadeIn 0.5s;
  }
  
  .quiz-incorrect {
      background: #f8d7da;
      border: 1px solid #f5c6cb;
      color: #721c24;
      padding: 1rem;
      border-radius: 8px;
      margin: 0.5rem 0;
      animation: fadeIn 0.5s;
  }
  
  .apa-report {
      background: white;
      padding: 2rem;
      font-family: 'Times New Roman', serif;
      line-height: 2;
      text-align: justify;
      border: 1px solid #ddd;
      margin: 1rem 0;
      font-size: 12pt;
  }
  
  .apa-title {
      text-align: center;
      font-weight: bold;
      margin-bottom: 2rem;
      font-size: 14pt;
  }
  
  .apa-author {
      text-align: center;
      margin-bottom: 1rem;
  }
  
  .apa-institution {
      text-align: center;
      margin-bottom: 2rem;
  }
  
  .apa-abstract {
      margin: 2rem 0;
      text-indent: 0;
  }
  
  .apa-paragraph {
      text-indent: 0.5in;
      margin-bottom: 1rem;
  }
  
  .apa-figure {
      text-align: center;
      margin: 2rem 0;
  }
  
  .software-example {
      background: #f8f9fa;
      padding: 1rem;
      border-radius: 8px;
      margin: 0.5rem 0;
      border-left: 3px solid #007bff;
  }
  
  @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
  }
</style>
""", unsafe_allow_html=True)

# Base de datos completa de ejemplos de software
EJEMPLOS_SOFTWARE = {
  "Sistemas Operativos": {
      "libre": [
          {
              "nombre": "Ubuntu Linux",
              "descripcion": "Distribución de Linux fácil de usar basada en Debian",
              "licencia": "GPL v3",
              "desarrollador": "Canonical Ltd.",
              "año": 2004,
              "ventajas": ["Gratuito", "Seguro", "Personalizable", "Gran comunidad"],
              "desventajas": ["Curva de aprendizaje", "Compatibilidad limitada con algunos juegos"],
              "uso_principal": "Escritorio, servidores, desarrollo"
          },
          {
              "nombre": "Debian",
              "descripcion": "Sistema operativo estable y robusto",
              "licencia": "DFSG",
              "desarrollador": "Proyecto Debian",
              "año": 1993,
              "ventajas": ["Muy estable", "Amplio repositorio", "Seguro"],
              "desventajas": ["Software menos actualizado", "Configuración compleja"],
              "uso_principal": "Servidores, sistemas críticos"
          },
          {
              "nombre": "Fedora",
              "descripcion": "Distribución innovadora patrocinada por Red Hat",
              "licencia": "GPL",
              "desarrollador": "Proyecto Fedora",
              "año": 2003,
              "ventajas": ["Tecnología de vanguardia", "Actualizaciones frecuentes", "Seguridad avanzada"],
              "desventajas": ["Menos estable", "Ciclo de vida corto"],
              "uso_principal": "Desarrollo, escritorio avanzado"
          }
      ],
      "privado": [
          {
              "nombre": "Windows 11",
              "descripcion": "Sistema operativo de Microsoft para PC",
              "licencia": "Propietaria",
              "desarrollador": "Microsoft",
              "año": 2021,
              "ventajas": ["Interfaz familiar", "Amplia compatibilidad", "Soporte oficial"],
              "desventajas": ["Costo elevado", "Telemetría", "Vulnerabilidades frecuentes"],
              "uso_principal": "Escritorio, gaming, oficina"
          },
          {
              "nombre": "macOS",
              "descripcion": "Sistema operativo de Apple para Mac",
              "licencia": "Propietaria",
              "desarrollador": "Apple Inc.",
              "año": 2001,
              "ventajas": ["Diseño elegante", "Integración con ecosistema Apple", "Estabilidad"],
              "desventajas": ["Hardware limitado", "Costo alto", "Menos personalizable"],
              "uso_principal": "Diseño, desarrollo iOS, multimedia"
          }
      ]
  },
  "Navegadores Web": {
      "libre": [
          {
              "nombre": "Mozilla Firefox",
              "descripcion": "Navegador web enfocado en privacidad",
              "licencia": "Mozilla Public License",
              "desarrollador": "Mozilla Foundation",
              "año": 2004,
              "ventajas": ["Privacidad por defecto", "Extensiones potentes", "Código abierto"],
              "desventajas": ["Menor cuota de mercado", "Consumo de memoria"],
              "uso_principal": "Navegación privada, desarrollo web"
          },
          {
              "nombre": "Chromium",
              "descripcion": "Proyecto de código abierto base de Chrome",
              "licencia": "BSD",
              "desarrollador": "Proyecto Chromium",
              "año": 2008,
              "ventajas": ["Rápido", "Estándares web", "Sin servicios de Google"],
              "desventajas": ["Menos funciones que Chrome", "Actualizaciones manuales"],
              "uso_principal": "Navegación, desarrollo web"
          }
      ],
      "privado": [
          {
              "nombre": "Google Chrome",
              "descripcion": "Navegador web más popular del mundo",
              "licencia": "Propietaria",
              "desarrollador": "Google",
              "año": 2008,
              "ventajas": ["Rápido", "Sincronización", "Amplia compatibilidad"],
              "desventajas": ["Recopilación de datos", "Consumo de memoria", "Dependencia de Google"],
              "uso_principal": "Navegación general, aplicaciones web"
          },
          {
              "nombre": "Safari",
              "descripcion": "Navegador web de Apple",
              "licencia": "Propietaria",
              "desarrollador": "Apple Inc.",
              "año": 2003,
              "ventajas": ["Optimizado para Mac", "Eficiencia energética", "Privacidad"],
              "desventajas": ["Solo en dispositivos Apple", "Extensiones limitadas"],
              "uso_principal": "Navegación en ecosistema Apple"
          }
      ]
  },
  "Suites Ofimáticas": {
      "libre": [
          {
              "nombre": "LibreOffice",
              "descripcion": "Suite ofimática completa y gratuita",
              "licencia": "Mozilla Public License",
              "desarrollador": "The Document Foundation",
              "año": 2011,
              "ventajas": ["Gratuito", "Compatible con MS Office", "Multiplataforma"],
              "desventajas": ["Interfaz menos moderna", "Funciones avanzadas limitadas"],
              "uso_principal": "Documentos, hojas de cálculo, presentaciones"
          },
          {
              "nombre": "Apache OpenOffice",
              "descripcion": "Suite ofimática de código abierto",
              "licencia": "Apache License 2.0",
              "desarrollador": "Apache Software Foundation",
              "año": 2012,
              "ventajas": ["Gratuito", "Estable", "Formatos estándar"],
              "desventajas": ["Desarrollo lento", "Interfaz desactualizada"],
              "uso_principal": "Oficina básica, educación"
          }
      ],
      "privado": [
          {
              "nombre": "Microsoft Office 365",
              "descripcion": "Suite ofimática líder del mercado",
              "licencia": "Propietaria",
              "desarrollador": "Microsoft",
              "año": 1990,
              "ventajas": ["Funciones avanzadas", "Integración cloud", "Amplia adopción"],
              "desventajas": ["Costo elevado", "Suscripción obligatoria", "Dependencia de Microsoft"],
              "uso_principal": "Oficina profesional, empresas"
          },
          {
              "nombre": "iWork",
              "descripcion": "Suite ofimática de Apple",
              "licencia": "Propietaria",
              "desarrollador": "Apple Inc.",
              "año": 2005,
              "ventajas": ["Diseño elegante", "Integración con iCloud", "Gratuito para usuarios Mac"],
              "desventajas": ["Solo ecosistema Apple", "Compatibilidad limitada"],
              "uso_principal": "Documentos en Mac/iOS"
          }
      ]
  },
  "Editores de Imagen": {
      "libre": [
          {
              "nombre": "GIMP",
              "descripcion": "Editor de imágenes avanzado",
              "licencia": "GPL v3",
              "desarrollador": "Equipo GIMP",
              "año": 1996,
              "ventajas": ["Gratuito", "Muy potente", "Extensible con plugins"],
              "desventajas": ["Interfaz compleja", "Curva de aprendizaje pronunciada"],
              "uso_principal": "Edición profesional de imágenes"
          },
          {
              "nombre": "Krita",
              "descripcion": "Editor enfocado en arte digital",
              "licencia": "GPL v3",
              "desarrollador": "KDE",
              "año": 2005,
              "ventajas": ["Herramientas de pintura avanzadas", "Gratuito", "Orientado a artistas"],
              "desventajas": ["Menos funciones de fotografía", "Consumo de recursos"],
              "uso_principal": "Arte digital, ilustración"
          }
      ],
      "privado": [
          {
              "nombre": "Adobe Photoshop",
              "descripcion": "Editor de imágenes profesional líder",
              "licencia": "Propietaria",
              "desarrollador": "Adobe Systems",
              "año": 1988,
              "ventajas": ["Estándar de la industria", "Funciones avanzadas", "Amplio soporte"],
              "desventajas": ["Muy caro", "Suscripción obligatoria", "Curva de aprendizaje"],
              "uso_principal": "Diseño gráfico profesional, fotografía"
          },
          {
              "nombre": "Canva",
              "descripcion": "Editor de diseño gráfico online",
              "licencia": "Propietaria",
              "desarrollador": "Canva Pty Ltd",
              "año": 2013,
              "ventajas": ["Fácil de usar", "Plantillas prediseñadas", "Colaborativo"],
              "desventajas": ["Funciones limitadas en versión gratuita", "Requiere internet"],
              "uso_principal": "Diseño rápido, redes sociales"
          }
      ]
  },
  "Reproductores Multimedia": {
      "libre": [
          {
              "nombre": "VLC Media Player",
              "descripcion": "Reproductor multimedia universal",
              "licencia": "GPL v2",
              "desarrollador": "VideoLAN",
              "año": 2001,
              "ventajas": ["Reproduce todo", "Gratuito", "Sin codecs adicionales"],
              "desventajas": ["Interfaz básica", "Funciones de organización limitadas"],
              "uso_principal": "Reproducción de video y audio"
          },
          {
              "nombre": "Audacity",
              "descripcion": "Editor de audio de código abierto",
              "licencia": "GPL v2",
              "desarrollador": "Equipo Audacity",
              "año": 2000,
              "ventajas": ["Gratuito", "Multiplataforma", "Funciones profesionales"],
              "desventajas": ["Interfaz desactualizada", "Curva de aprendizaje"],
              "uso_principal": "Edición de audio, podcasting"
          }
      ],
      "privado": [
          {
              "nombre": "Spotify",
              "descripcion": "Servicio de streaming de música",
              "licencia": "Propietaria",
              "desarrollador": "Spotify Technology",
              "año": 2006,
              "ventajas": ["Amplio catálogo", "Recomendaciones personalizadas", "Multiplataforma"],
              "desventajas": ["Suscripción para funciones completas", "Dependencia de internet"],
              "uso_principal": "Streaming de música"
          },
          {
              "nombre": "Adobe Premiere Pro",
              "descripcion": "Editor de video profesional",
              "licencia": "Propietaria",
              "desarrollador": "Adobe Systems",
              "año": 2003,
              "ventajas": ["Herramientas profesionales", "Integración Creative Suite", "Efectos avanzados"],
              "desventajas": ["Muy caro", "Suscripción obligatoria", "Requiere hardware potente"],
              "uso_principal": "Edición de video profesional"
          }
      ]
  }
}

# Preguntas del quiz sobre ejemplos específicos
PREGUNTAS_EJEMPLOS = [
  {
      "pregunta": "¿Cuál de estos navegadores es software libre?",
      "opciones": ["Google Chrome", "Mozilla Firefox", "Safari", "Microsoft Edge"],
      "respuesta_correcta": 1,
      "explicacion": "Mozilla Firefox es software libre bajo la Mozilla Public License, mientras que los demás son propietarios.",
      "categoria": "Navegadores"
  },
  {
      "pregunta": "¿Qué suite ofimática libre es más popular?",
      "opciones": ["Microsoft Office", "LibreOffice", "iWork", "Google Workspace"],
      "respuesta_correcta": 1,
      "explicacion": "LibreOffice es la suite ofimática libre más popular y ampliamente utilizada.",
      "categoria": "Oficina"
  },
  {
      "pregunta": "¿Cuál es la alternativa libre más conocida a Photoshop?",
      "opciones": ["Canva", "GIMP", "Paint.NET", "Pixlr"],
      "respuesta_correcta": 1,
      "explicacion": "GIMP (GNU Image Manipulation Program) es la alternativa libre más conocida y potente a Photoshop.",
      "categoria": "Diseño"
  },
  {
      "pregunta": "¿Qué reproductor multimedia libre reproduce prácticamente cualquier formato?",
      "opciones": ["Windows Media Player", "iTunes", "VLC Media Player", "QuickTime"],
      "respuesta_correcta": 2,
      "explicacion": "VLC Media Player es conocido por reproducir prácticamente cualquier formato de audio y video.",
      "categoria": "Multimedia"
  },
  {
      "pregunta": "¿Cuál de estos sistemas operativos es completamente libre?",
      "opciones": ["Windows 11", "macOS", "Ubuntu Linux", "Chrome OS"],
      "respuesta_correcta": 2,
      "explicacion": "Ubuntu Linux es completamente libre y de código abierto, basado en el kernel Linux.",
      "categoria": "Sistemas Operativos"
  },
  {
      "pregunta": "¿Qué editor de audio libre es más utilizado para podcasting?",
      "opciones": ["Pro Tools", "Audacity", "Logic Pro", "Adobe Audition"],
      "respuesta_correcta": 1,
      "explicacion": "Audacity es el editor de audio libre más popular para podcasting y edición básica de audio.",
      "categoria": "Multimedia"
  },
  {
      "pregunta": "¿Cuál es la principal ventaja de usar LibreOffice sobre Microsoft Office?",
      "opciones": ["Mejor interfaz", "Es gratuito", "Más funciones", "Mejor compatibilidad"],
      "respuesta_correcta": 1,
      "explicacion": "La principal ventaja de LibreOffice es que es completamente gratuito, sin costos de licencia.",
      "categoria": "Oficina"
  },
  {
      "pregunta": "¿Qué navegador está basado en el proyecto libre Chromium?",
      "opciones": ["Firefox", "Safari", "Google Chrome", "Internet Explorer"],
      "respuesta_correcta": 2,
      "explicacion": "Google Chrome está basado en Chromium, que es un proyecto de código abierto.",
      "categoria": "Navegadores"
  },
  {
      "pregunta": "¿Cuál de estos es un editor de imágenes libre especializado en arte digital?",
      "opciones": ["Photoshop", "Krita", "Illustrator", "CorelDRAW"],
      "respuesta_correcta": 1,
      "explicacion": "Krita es un editor libre especializado en arte digital y pintura.",
      "categoria": "Diseño"
  },
  {
      "pregunta": "¿Qué distribución de Linux es conocida por ser muy estable para servidores?",
      "opciones": ["Ubuntu", "Fedora", "Debian", "Arch Linux"],
      "respuesta_correcta": 2,
      "explicacion": "Debian es conocida por su estabilidad y es ampliamente utilizada en servidores.",
      "categoria": "Sistemas Operativos"
  }
]

# Inicializar session state
if 'quiz_score' not in st.session_state:
  st.session_state.quiz_score = 0
if 'quiz_total' not in st.session_state:
  st.session_state.quiz_total = 0
if 'pregunta_actual' not in st.session_state:
  st.session_state.pregunta_actual = 0
if 'quiz_completado' not in st.session_state:
  st.session_state.quiz_completado = False
if 'quiz_iniciado' not in st.session_state:
  st.session_state.quiz_iniciado = False
if 'preguntas_seleccionadas' not in st.session_state:
  st.session_state.preguntas_seleccionadas = []
if 'respuestas_usuario' not in st.session_state:
  st.session_state.respuestas_usuario = []

# Header principal
st.markdown("""
<div class="main-header">
  <h1>📋 Ejemplos de Software Libre vs Software Privado</h1>
  <h3>Catálogo Completo con Quiz e Informes APA</h3>
  <p>Explora ejemplos reales, compara alternativas y genera informes académicos</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🎯 Navegación")
seccion = st.sidebar.selectbox(
  "Selecciona una sección:",
  [
      "🏠 Catálogo de Ejemplos",
      "🔍 Comparador de Software",
      "🎮 Quiz de Ejemplos",
      "📊 Análisis Estadístico",
      "📄 Generar Informe APA"
  ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Estadísticas")

# Calcular estadísticas
total_libre = sum(len(categoria["libre"]) for categoria in EJEMPLOS_SOFTWARE.values())
total_privado = sum(len(categoria["privado"]) for categoria in EJEMPLOS_SOFTWARE.values())
total_categorias = len(EJEMPLOS_SOFTWARE)

st.sidebar.metric("Software Libre", total_libre)
st.sidebar.metric("Software Privado", total_privado)
st.sidebar.metric("Categorías", total_categorias)

if st.session_state.quiz_total > 0:
  accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
  st.sidebar.metric("Precisión Quiz", f"{accuracy:.1f}%")

# Sección: Catálogo de Ejemplos
if seccion == "🏠 Catálogo de Ejemplos":
  st.markdown("## 📋 Catálogo Completo de Ejemplos")
  
  # Selector de categoría
  categoria_seleccionada = st.selectbox(
      "Selecciona una categoría:",
      list(EJEMPLOS_SOFTWARE.keys())
  )
  
  if categoria_seleccionada:
      col1, col2 = st.columns(2)
      
      # Software Libre
      with col1:
          st.markdown(f"""
          <div class="software-card libre-card">
              <h3>🆓 Software Libre - {categoria_seleccionada}</h3>
          </div>
          """, unsafe_allow_html=True)
          
          for software in EJEMPLOS_SOFTWARE[categoria_seleccionada]["libre"]:
              with st.expander(f"📱 {software['nombre']} ({software['año']})"):
                  st.write(f"**Descripción:** {software['descripcion']}")
                  st.write(f"**Licencia:** {software['licencia']}")
                  st.write(f"**Desarrollador:** {software['desarrollador']}")
                  st.write(f"**Uso Principal:** {software['uso_principal']}")
                  
                  col_v, col_d = st.columns(2)
                  with col_v:
                      st.write("**✅ Ventajas:**")
                      for ventaja in software['ventajas']:
                          st.write(f"• {ventaja}")
                  
                  with col_d:
                      st.write("**❌ Desventajas:**")
                      for desventaja in software['desventajas']:
                          st.write(f"• {desventaja}")
      
      # Software Privado
      with col2:
          st.markdown(f"""
          <div class="software-card privado-card">
              <h3>💰 Software Privado - {categoria_seleccionada}</h3>
          </div>
          """, unsafe_allow_html=True)
          
          for software in EJEMPLOS_SOFTWARE[categoria_seleccionada]["privado"]:
              with st.expander(f"💼 {software['nombre']} ({software['año']})"):
                  st.write(f"**Descripción:** {software['descripcion']}")
                  st.write(f"**Licencia:** {software['licencia']}")
                  st.write(f"**Desarrollador:** {software['desarrollador']}")
                  st.write(f"**Uso Principal:** {software['uso_principal']}")
                  
                  col_v, col_d = st.columns(2)
                  with col_v:
                      st.write("**✅ Ventajas:**")
                      for ventaja in software['ventajas']:
                          st.write(f"• {ventaja}")
                  
                  with col_d:
                      st.write("**❌ Desventajas:**")
                      for desventaja in software['desventajas']:
                          st.write(f"• {desventaja}")

# Sección: Comparador de Software
elif seccion == "🔍 Comparador de Software":
  st.markdown("## 🔍 Comparador de Software")
  
  col1, col2 = st.columns(2)
  
  with col1:
      st.markdown("### Selecciona Software Libre")
      categoria_libre = st.selectbox("Categoría:", list(EJEMPLOS_SOFTWARE.keys()), key="cat_libre")
      software_libre_opciones = [s['nombre'] for s in EJEMPLOS_SOFTWARE[categoria_libre]["libre"]]
      software_libre_sel = st.selectbox("Software:", software_libre_opciones, key="soft_libre")
  
  with col2:
      st.markdown("### Selecciona Software Privado")
      categoria_privado = st.selectbox("Categoría:", list(EJEMPLOS_SOFTWARE.keys()), key="cat_privado")
      software_privado_opciones = [s['nombre'] for s in EJEMPLOS_SOFTWARE[categoria_privado]["privado"]]
      software_privado_sel = st.selectbox("Software:", software_privado_opciones, key="soft_privado")
  
  if st.button("🔄 Comparar Software", type="primary"):
      # Encontrar los software seleccionados
      libre_data = next(s for s in EJEMPLOS_SOFTWARE[categoria_libre]["libre"] if s['nombre'] == software_libre_sel)
      privado_data = next(s for s in EJEMPLOS_SOFTWARE[categoria_privado]["privado"] if s['nombre'] == software_privado_sel)
      
      st.markdown("---")
      st.markdown("## 📊 Comparación Detallada")
      
      # Tabla comparativa
      comparacion_df = pd.DataFrame({
          "Aspecto": ["Nombre", "Año", "Licencia", "Desarrollador", "Uso Principal"],
          software_libre_sel: [
              libre_data['nombre'],
              libre_data['año'],
              libre_data['licencia'],
              libre_data['desarrollador'],
              libre_data['uso_principal']
          ],
          software_privado_sel: [
              privado_data['nombre'],
              privado_data['año'],
              privado_data['licencia'],
              privado_data['desarrollador'],
              privado_data['uso_principal']
          ]
      })
      
      st.dataframe(comparacion_df, use_container_width=True)
      
      # Comparación de ventajas y desventajas
      col1, col2 = st.columns(2)
      
      with col1:
          st.markdown(f"### ✅ Ventajas de {software_libre_sel}")
          for ventaja in libre_data['ventajas']:
              st.success(f"✓ {ventaja}")
          
          st.markdown(f"### ❌ Desventajas de {software_libre_sel}")
          for desventaja in libre_data['desventajas']:
              st.error(f"✗ {desventaja}")
      
      with col2:
          st.markdown(f"### ✅ Ventajas de {software_privado_sel}")
          for ventaja in privado_data['ventajas']:
              st.success(f"✓ {ventaja}")
          
          st.markdown(f"### ❌ Desventajas de {software_privado_sel}")
          for desventaja in privado_data['desventajas']:
              st.error(f"✗ {desventaja}")


