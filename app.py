import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Configuración de la página
st.set_page_config(
  page_title="🆓 Software Libre vs 💰 Software Privado",
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
  
  .metric-card {
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
      padding: 1.5rem;
      border-radius: 10px;
      text-align: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      margin: 0.5rem 0;
  }
  
  .timeline-item {
      background: white;
      padding: 1rem;
      border-radius: 8px;
      margin: 0.5rem 0;
      border-left: 3px solid #007bff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  }
  
  .quiz-correct {
      background: #d4edda;
      border: 1px solid #c3e6cb;
      color: #155724;
      padding: 1rem;
      border-radius: 8px;
      margin: 0.5rem 0;
  }
  
  .quiz-incorrect {
      background: #f8d7da;
      border: 1px solid #f5c6cb;
      color: #721c24;
      padding: 1rem;
      border-radius: 8px;
      margin: 0.5rem 0;
  }
  
  .case-study {
      background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
      padding: 1.5rem;
      border-radius: 10px;
      margin: 1rem 0;
      border-left: 4px solid #2196f3;
  }
  
  .comparison-bar {
      background: #f8f9fa;
      height: 30px;
      border-radius: 15px;
      margin: 10px 0;
      position: relative;
      overflow: hidden;
  }
  
  .bar-fill-libre {
      background: #28a745;
      height: 100%;
      border-radius: 15px;
      transition: width 0.5s ease;
  }
  
  .bar-fill-privado {
      background: #dc3545;
      height: 100%;
      border-radius: 15px;
      transition: width 0.5s ease;
  }
  
  .cost-summary {
      background: linear-gradient(135deg, #fff9c4 0%, #f7dc6f 100%);
      padding: 1.5rem;
      border-radius: 10px;
      margin: 1rem 0;
      border-left: 4px solid #f39c12;
  }
</style>
""", unsafe_allow_html=True)

# Datos de software
SOFTWARE_LIBRE = {
  "Sistemas Operativos": ["Linux Ubuntu", "Debian", "CentOS", "Fedora", "FreeBSD"],
  "Navegadores": ["Firefox", "Chromium"],
  "Oficina": ["LibreOffice", "Apache OpenOffice"],
  "Diseño": ["GIMP", "Blender", "Inkscape", "Audacity"],
  "Desarrollo": ["Visual Studio Code", "Eclipse", "Git", "Apache", "MySQL"],
  "Multimedia": ["VLC Media Player", "OBS Studio", "Krita"],
  "Herramientas": ["7-Zip", "FileZilla", "Wireshark"]
}

SOFTWARE_PRIVADO = {
  "Sistemas Operativos": ["Windows 11", "macOS", "iOS", "Android (Google)"],
  "Navegadores": ["Google Chrome", "Safari", "Microsoft Edge"],
  "Oficina": ["Microsoft Office", "Adobe Creative Suite"],
  "Diseño": ["Adobe Photoshop", "Adobe Illustrator", "Sketch"],
  "Desarrollo": ["Visual Studio", "JetBrains IDEs", "Xcode"],
  "Multimedia": ["Adobe Premiere Pro", "Final Cut Pro", "Spotify Premium"],
  "Herramientas": ["WinRAR", "TeamViewer", "Zoom Pro"]
}

# Inicializar session state
if 'quiz_score' not in st.session_state:
  st.session_state.quiz_score = 0
if 'quiz_total' not in st.session_state:
  st.session_state.quiz_total = 0
if 'current_comparison' not in st.session_state:
  st.session_state.current_comparison = None
if 'pregunta_actual' not in st.session_state:
  st.session_state.pregunta_actual = 0
if 'quiz_completado' not in st.session_state:
  st.session_state.quiz_completado = False

# Header principal
st.markdown("""
<div class="main-header">
  <h1>🖥️ Software Libre vs Software Privado</h1>
  <h3>Guía Interactiva Completa</h3>
  <p>Explora las diferencias, ventajas y desventajas de cada modelo de software</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🎯 Navegación")
seccion = st.sidebar.selectbox(
  "Selecciona una sección:",
  [
      "🏠 Inicio",
      "📊 Comparación Detallada", 
      "💡 Ejemplos Prácticos",
      "📈 Análisis de Costos",
      "🎮 Quiz Interactivo",
      "📚 Casos de Estudio",
      "🔮 Tendencias Futuras"
  ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Estadísticas de Uso")

# Simular estadísticas
total_software_libre = sum(len(v) for v in SOFTWARE_LIBRE.values())
total_software_privado = sum(len(v) for v in SOFTWARE_PRIVADO.values())

st.sidebar.metric("Software Libre Ejemplos", total_software_libre)
st.sidebar.metric("Software Privado Ejemplos", total_software_privado)

if st.session_state.quiz_total > 0:
  accuracy = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
  st.sidebar.metric("Precisión en Quiz", f"{accuracy:.1f}%")

# Sección: Inicio
if seccion == "🏠 Inicio":
  st.markdown("## 🌟 Bienvenido a la Guía Interactiva")
  
  col1, col2 = st.columns(2)
  
  with col1:
      st.markdown("""
      <div class="software-card libre-card">
          <h3>🆓 Software Libre</h3>
          <p><strong>Definición:</strong> Software que respeta la libertad de los usuarios. Puedes ejecutar, copiar, distribuir, estudiar, modificar y mejorar el software.</p>
          <h4>🔑 Características Clave:</h4>
          <ul>
              <li>✅ Código fuente disponible</li>
              <li>✅ Libertad de modificación</li>
              <li>✅ Redistribución permitida</li>
              <li>✅ Sin restricciones de uso</li>
              <li>✅ Comunidad colaborativa</li>
          </ul>
      </div>
      """, unsafe_allow_html=True)
  
  with col2:
      st.markdown("""
      <div class="software-card privado-card">
          <h3>💰 Software Privado</h3>
          <p><strong>Definición:</strong> Software donde el propietario mantiene control exclusivo sobre el código, distribución y modificación.</p>
          <h4>🔑 Características Clave:</h4>
          <ul>
              <li>🔒 Código fuente cerrado</li>
              <li>🔒 Control del fabricante</li>
              <li>🔒 Licencias restrictivas</li>
              <li>🔒 Soporte comercial</li>
              <li>🔒 Modelo de negocio tradicional</li>
          </ul>
      </div>
      """, unsafe_allow_html=True)
  
  # Métricas generales
  st.markdown("## 📊 Panorama General")
  
  metric_cols = st.columns(4)
  with metric_cols[0]:
      st.markdown("""
      <div class="metric-card">
          <h3>🌍</h3>
          <h4>Adopción Global</h4>
          <p>70% servidores web usan software libre</p>
      </div>
      """, unsafe_allow_html=True)
  
  with metric_cols[1]:
      st.markdown("""
      <div class="metric-card">
          <h3>💰</h3>
          <h4>Ahorro Estimado</h4>
          <p>$60B anuales en licencias</p>
      </div>
      """, unsafe_allow_html=True)
  
  with metric_cols[2]:
      st.markdown("""
      <div class="metric-card">
          <h3>👥</h3>
          <h4>Desarrolladores</h4>
          <p>31M contribuyentes GitHub</p>
      </div>
      """, unsafe_allow_html=True)
  
  with metric_cols[3]:
      st.markdown("""
      <div class="metric-card">
          <h3>🚀</h3>
          <h4>Proyectos Activos</h4>
          <p>200M+ repositorios</p>
      </div>
      """, unsafe_allow_html=True)
  
  # Timeline histórico
  st.markdown("## 📅 Historia del Software Libre")
  
  timeline_data = [
      {"año": 1983, "evento": "Richard Stallman inicia el Proyecto GNU", "tipo": "libre"},
      {"año": 1991, "evento": "Linus Torvalds crea Linux", "tipo": "libre"},
      {"año": 1998, "evento": "Se acuña el término 'Open Source'", "tipo": "libre"},
      {"año": 2004, "evento": "Ubuntu democratiza Linux", "tipo": "libre"},
      {"año": 1975, "evento": "Microsoft fundada - modelo propietario", "tipo": "privado"},
      {"año": 1984, "evento": "Apple Macintosh - interfaz propietaria", "tipo": "privado"},
      {"año": 2001, "evento": "Windows XP - dominancia del escritorio", "tipo": "privado"}
  ]
  
  for item in sorted(timeline_data, key=lambda x: x["año"]):
      color = "#28a745" if item["tipo"] == "libre" else "#dc3545"
      st.markdown(f"""
      <div class="timeline-item" style="border-left-color: {color};">
          <strong>{item['año']}</strong> - {item['evento']}
      </div>
      """, unsafe_allow_html=True)

# Sección: Comparación Detallada
elif seccion == "📊 Comparación Detallada":
  st.markdown("## 📊 Comparación Detallada")
  
  # Tabla comparativa interactiva
  aspectos = [
      "💰 Costo Inicial", "🔍 Código Fuente", "🔧 Personalización", 
      "🛠️ Soporte Técnico", "🔒 Seguridad", "📈 Actualizaciones",
      "🌍 Distribución", "📚 Documentación", "👥 Comunidad",
      "🎯 Facilidad de Uso", "🔄 Compatibilidad", "⚡ Rendimiento"
  ]
  
  libre_scores = [9, 10, 10, 7, 9, 8, 10, 7, 10, 6, 7, 8]
  privado_scores = [3, 2, 3, 9, 7, 6, 4, 9, 5, 9, 8, 8]
  
  # Mostrar comparación con barras CSS
  st.markdown("### 📊 Comparación Visual por Aspectos")
  
  for i, aspecto in enumerate(aspectos):
      libre_score = libre_scores[i]
      privado_score = privado_scores[i]
      
      st.markdown(f"**{aspecto}**")
      
      col1, col2 = st.columns(2)
      
      with col1:
          st.markdown("Software Libre")
          libre_width = (libre_score / 10) * 100
          st.markdown(f"""
          <div class="comparison-bar">
              <div class="bar-fill-libre" style="width: {libre_width}%"></div>
          </div>
          <small>{libre_score}/10</small>
          """, unsafe_allow_html=True)
      
      with col2:
          st.markdown("Software Privado")
          privado_width = (privado_score / 10) * 100
          st.markdown(f"""
          <div class="comparison-bar">
              <div class="bar-fill-privado" style="width: {privado_width}%"></div>
          </div>
          <small>{privado_score}/10</small>
          """, unsafe_allow_html=True)
  
  # Tabla detallada
  st.markdown("### 📋 Tabla Comparativa Detallada")
  
  detailed_comparison = {
      "Aspecto": [
          "💰 Costo", "🔍 Transparencia", "🔧 Flexibilidad", "🛠️ Soporte",
          "🔒 Seguridad", "📈 Control", "🌍 Libertad", "⚡ Innovación"
      ],
      "Software Libre": [
          "Gratuito (generalmente)", "Código abierto y auditable", "Total personalización",
          "Comunidad + comercial", "Transparente y colaborativa", "Usuario controla",
          "Sin restricciones", "Innovación colaborativa"
      ],
      "Software Privado": [
          "Licencias de pago", "Código cerrado", "Limitada por fabricante",
          "Soporte oficial", "Depende del fabricante", "Fabricante controla",
          "Restricciones de licencia", "Innovación controlada"
      ]
  }
  
  df_detailed = pd.DataFrame(detailed_comparison)
  st.dataframe(df_detailed, use_container_width=True)
  
  # Selector interactivo para comparar aspectos específicos
  st.markdown("### 🎯 Comparador Interactivo")
  
  aspecto_seleccionado = st.selectbox(
      "Selecciona un aspecto para análisis detallado:",
      aspectos
  )
  
  if aspecto_seleccionado:
      idx = aspectos.index(aspecto_seleccionado)
      libre_score = libre_scores[idx]
      privado_score = privado_scores[idx]
      
      col1, col2, col3 = st.columns(3)
      
      with col1:
          st.metric("Software Libre", f"{libre_score}/10", 
                   delta=f"{libre_score - privado_score}")
      
      with col2:
          st.metric("Software Privado", f"{privado_score}/10",
                   delta=f"{privado_score - libre_score}")
      
      with col3:
          winner = "Software Libre" if libre_score > privado_score else "Software Privado"
          if libre_score == privado_score:
              winner = "Empate"
          st.metric("Ganador", winner)

# Sección: Ejemplos Prácticos
elif seccion == "💡 Ejemplos Prácticos":
  st.markdown("## 💡 Ejemplos Prácticos por Categoría")
  
  # Selector de categoría
  categoria = st.selectbox(
      "Selecciona una categoría:",
      list(SOFTWARE_LIBRE.keys())
  )
  
  if categoria:
      col1, col2 = st.columns(2)
      
      with col1:
          st.markdown(f"""
          <div class="software-card libre-card">
              <h3>🆓 Software Libre - {categoria}</h3>
          </div>
          """, unsafe_allow_html=True)
          
          for software in SOFTWARE_LIBRE[categoria]:
              if st.button(f"ℹ️ {software}", key=f"libre_{software}"):
                  st.session_state.current_comparison = {
                      'software': software,
                      'tipo': 'libre',
                      'categoria': categoria
                  }
      
      with col2:
          st.markdown(f"""
          <div class="software-card privado-card">
              <h3>💰 Software Privado - {categoria}</h3>
          </div>
          """, unsafe_allow_html=True)
          
          for software in SOFTWARE_PRIVADO[categoria]:
              if st.button(f"ℹ️ {software}", key=f"privado_{software}"):
                  st.session_state.current_comparison = {
                      'software': software,
                      'tipo': 'privado',
                      'categoria': categoria
                  }
  
  # Mostrar información detallada del software seleccionado
  if st.session_state.current_comparison:
      comp = st.session_state.current_comparison
      st.markdown("---")
      st.markdown(f"### 📋 Información Detallada: {comp['software']}")
      
      # Información detallada de software específico
      info_software = {
          'Firefox': {
              'descripcion': 'Navegador web libre desarrollado por Mozilla Foundation',
              'licencia': 'Mozilla Public License 2.0',
              'ventajas': ['Privacidad por defecto', 'Extensiones potentes', 'Código abierto', 'Multiplataforma'],
              'desventajas': ['Menor cuota de mercado', 'Algunos sitios optimizados para Chrome', 'Consumo de memoria'],
              'alternativas': ['Chromium', 'Brave Browser']
          },
          'Linux Ubuntu': {
              'descripcion': 'Distribución de Linux basada en Debian, enfocada en facilidad de uso',
              'licencia': 'GPL y otras licencias libres',
              'ventajas': ['Gratuito', 'Seguro', 'Personalizable', 'Gran comunidad'],
              'desventajas': ['Curva de aprendizaje', 'Compatibilidad de software comercial', 'Soporte de hardware específico'],
              'alternativas': ['Fedora', 'Debian', 'Linux Mint']
          },
          'LibreOffice': {
              'descripcion': 'Suite ofimática libre y gratuita, fork de OpenOffice',
              'licencia': 'Mozilla Public License 2.0',
              'ventajas': ['Gratuito', 'Compatible con formatos MS Office', 'Multiplataforma', 'Sin telemetría'],
              'desventajas': ['Interfaz menos moderna', 'Funciones avanzadas limitadas', 'Rendimiento en documentos grandes'],
              'alternativas': ['Apache OpenOffice', 'OnlyOffice']
          },
          'Windows 11': {
              'descripcion': 'Sistema operativo propietario más reciente de Microsoft',
              'licencia': 'Licencia de Software de Microsoft',
              'ventajas': ['Compatibilidad amplia', 'Soporte oficial', 'Interfaz moderna', 'Gaming optimizado'],
              'desventajas': ['Costo de licencia', 'Telemetría extensiva', 'Requisitos de hardware', 'Actualizaciones forzadas'],
              'alternativas': ['macOS', 'Chrome OS']
          },
          'Microsoft Office': {
              'descripcion': 'Suite ofimática propietaria líder en el mercado empresarial',
              'licencia': 'Licencia comercial de Microsoft',
              'ventajas': ['Estándar de la industria', 'Funciones avanzadas', 'Integración con servicios MS', 'Soporte profesional'],
              'desventajas': ['Costo elevado', 'Dependencia del proveedor', 'Modelo de suscripción', 'Telemetría'],
              'alternativas': ['Google Workspace', 'Apple iWork']
          }
      }
      
      # Información por defecto si no está en el diccionario
      default_info = {
          'descripcion': f'{comp["software"]} - Software de {comp["categoria"]}',
          'licencia': 'GPL/MIT/Apache' if comp['tipo'] == 'libre' else 'Licencia Propietaria',
          'ventajas': ['Código abierto', 'Gratuito', 'Personalizable', 'Comunidad activa'] if comp['tipo'] == 'libre' 
                     else ['Soporte oficial', 'Interfaz pulida', 'Documentación completa', 'Funciones avanzadas'],
          'desventajas': ['Curva de aprendizaje', 'Soporte limitado'] if comp['tipo'] == 'libre' 
                        else ['Costo elevado', 'Dependencia del proveedor', 'Licencias restrictivas'],
          'alternativas': ['Consultar repositorios'] if comp['tipo'] == 'libre' else ['Opciones limitadas']
      }
      
      info = info_software.get(comp['software'], default_info)
      
      col1, col2 = st.columns(2)
      
      with col1:
          st.markdown("#### 📝 Descripción")
          st.write(info['descripcion'])
          st.markdown("#### 📄 Licencia")
          st.write(info['licencia'])
      
      with col2:
          st.markdown("#### ✅ Ventajas")
          for ventaja in info['ventajas']:
              st.write(f"• {ventaja}")
          
          st.markdown("#### ❌ Desventajas")
          for desventaja in info['desventajas']:
              st.write(f"• {desventaja}")
      
      if 'alternativas' in info:
          st.markdown("#### 🔄 Alternativas")
          st.write(", ".join(info['alternativas']))

# Sección: Análisis de Costos
elif seccion == "📈 Análisis de Costos":
  st.markdown("## 📈 Análisis de Costos")
  
  # Calculadora de costos
  st.markdown("### 💰 Calculadora de Costos")
  
  col1, col2 = st.columns(2)
  
  with col1:
      st.markdown("#### Configuración")
      num_usuarios = st.number_input("Número de usuarios", 1, 1000, 50)
      años = st.slider("Período (años)", 1, 10, 5)
      incluir_soporte = st.checkbox("Incluir soporte técnico")
      incluir_capacitacion = st.checkbox("Incluir capacitación")
      incluir_migracion = st.checkbox("Incluir costos de migración")
  
  with col2:
      # Costos estimados (valores realistas del mercado)
      costo_licencia_office = 150  # USD por usuario por año
      costo_licencia_windows = 200  # USD por usuario (una vez)
      costo_soporte = 50  # USD por usuario por año
      costo_capacitacion = 100  # USD por usuario (una vez)
      costo_migracion = 75  # USD por usuario (una vez)
      
      # Cálculos para software privado
      costo_privado = (
          (costo_licencia_office * años * num_usuarios) +
          (costo_licencia_windows * num_usuarios) +
          (costo_soporte * años * num_usuarios if incluir_soporte else 0) +
          (costo_capacitacion * num_usuarios if incluir_capacitacion else 0) +
          (costo_migracion * num_usuarios if incluir_migracion else 0)
      )
      
      # Cálculos para software libre (costos reducidos pero no cero)
      costo_libre = (
          (costo_soporte * 0.4 * años * num_usuarios if incluir_soporte else 0) +  # 40% del costo de soporte comercial
          (costo_capacitacion * 0.6 * num_usuarios if incluir_capacitacion else 0) +  # 60% del costo de capacitación
          (costo_migracion * 1.2 * num_usuarios if incluir_migracion else 0)  # 120% por complejidad de migración
      )
      
      ahorro = costo_privado - costo_libre
      
      st.markdown("#### Resultados")
      st.metric("Costo Software Privado", f"${costo_privado:,.2f}")
      st.metric("Costo Software Libre", f"${costo_libre:,.2f}")
      st.metric("Ahorro Total", f"${ahorro:,.2f}", 
               delta=f"{(ahorro/costo_privado)*100:.1f}%" if costo_privado > 0 else "0%")
  
  # Resumen de costos
  st.markdown(f"""
  <div class="cost-summary">
      <h4>💡 Resumen de Análisis</h4>
      <p><strong>Configuración:</strong> {num_usuarios} usuarios por {años} años</p>
      <p><strong>Ahorro estimado:</strong> ${ahorro:,.2f} ({(ahorro/costo_privado)*100:.1f}% menos)</p>
      <p><strong>Ahorro por usuario/año:</strong> ${ahorro/(num_usuarios*años):,.2f}</p>
  </div>
  """, unsafe_allow_html=True)
  
  # Tabla de costos detallada
  st.markdown("### 📊 Desglose Detallado de Costos")
  
  cost_breakdown = {
      'Concepto': ['Licencias Office', 'Licencias SO', 'Soporte Técnico', 'Capacitación', 'Migración', 'TOTAL'],
      'Software Privado': [
          f"${costo_licencia_office * años * num_usuarios:,.2f}",
          f"${costo_licencia_windows * num_usuarios:,.2f}",
          f"${costo_soporte * años * num_usuarios if incluir_soporte else 0:,.2f}",
          f"${costo_capacitacion * num_usuarios if incluir_capacitacion else 0:,.2f}",
          f"${costo_migracion * num_usuarios if incluir_migracion else 0:,.2f}",
          f"${costo_privado:,.2f}"
      ],
      'Software Libre': [
          "$0.00",
          "$0.00",
          f"${costo_soporte * 0.4 * años * num_usuarios if incluir_soporte else 0:,.2f}",
          f"${costo_capacitacion * 0.6 * num_usuarios if incluir_capacitacion else 0:,.2f}",
          f"${costo_migracion * 1.2 * num_usuarios if incluir_migracion else 0:,.2f}",
          f"${costo_libre:,.2f}"
      ]
  }
  
  df_costs = pd.DataFrame(cost_breakdown)
  st.dataframe(df_costs, use_container_width=True)

# Sección: Quiz Interactivo
elif seccion == "🎮 Quiz Interactivo":
  st.markdown("## 🎮 Quiz Interactivo")
  
  # Preguntas del quiz
  preguntas = [
      {
          "pregunta": "¿Cuál es la principal característica del software libre?",
          "opciones": [
              "Es gratuito",
              "El código fuente está disponible",
              "No
