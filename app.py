import streamlit as st
import pandas as pd
from datetime import datetime
import random
import time

# Configuración de la página
st.set_page_config(
  page_title="🎓 Quiz Profesional: Software Libre vs Privado",
  page_icon="🖥️",
  layout="wide",
  initial_sidebar_state="expanded"
)

# CSS profesional
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
  
  * {
      font-family: 'Inter', sans-serif;
  }
  
  .main-header {
      text-align: center;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 3rem 2rem;
      border-radius: 20px;
      margin-bottom: 2rem;
      color: white;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  }
  
  .main-header h1 {
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  }
  
  .main-header h3 {
      font-size: 1.2rem;
      font-weight: 400;
      opacity: 0.9;
      margin-bottom: 1rem;
  }
  
  .professional-card {
      background: white;
      padding: 2rem;
      border-radius: 15px;
      box-shadow: 0 5px 20px rgba(0,0,0,0.1);
      margin: 1.5rem 0;
      border: 1px solid #e1e8ed;
      transition: all 0.3s ease;
  }
  
  .professional-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(0,0,0,0.15);
  }
  
  .software-card-libre {
      background: linear-gradient(135deg, #f8fff9 0%, #e8f5e8 100%);
      border-left: 5px solid #28a745;
  }
  
  .software-card-privado {
      background: linear-gradient(135deg, #fff8f8 0%, #ffe8e8 100%);
      border-left: 5px solid #dc3545;
  }
  
  .quiz-container {
      background: linear-gradient(135deg, #f8f9ff 0%, #e8f2ff 100%);
      padding: 2.5rem;
      border-radius: 20px;
      margin: 2rem 0;
      border: 2px solid #4285f4;
      box-shadow: 0 8px 25px rgba(66, 133, 244, 0.15);
  }
  
  .quiz-header {
      text-align: center;
      margin-bottom: 2rem;
  }
  
  .quiz-header h2 {
      color: #1a73e8;
      font-weight: 600;
      font-size: 2rem;
      margin-bottom: 0.5rem;
  }
  
  .quiz-progress {
      background: #f1f3f4;
      height: 8px;
      border-radius: 4px;
      margin: 1rem 0;
      overflow: hidden;
  }
  
  .quiz-progress-fill {
      background: linear-gradient(90deg, #4285f4, #34a853);
      height: 100%;
      border-radius: 4px;
      transition: width 0.5s ease;
  }
  
  .question-card {
      background: white;
      padding: 2rem;
      border-radius: 15px;
      margin: 1.5rem 0;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      border-left: 4px solid #4285f4;
  }
  
  .question-number {
      background: #4285f4;
      color: white;
      padding: 0.5rem 1rem;
      border-radius: 20px;
      font-weight: 600;
      font-size: 0.9rem;
      display: inline-block;
      margin-bottom: 1rem;
  }
  
  .question-text {
      font-size: 1.2rem;
      font-weight: 500;
      color: #202124;
      margin-bottom: 1.5rem;
      line-height: 1.5;
  }
  
  .option-button {
      background: white;
      border: 2px solid #e8eaed;
      padding: 1rem 1.5rem;
      border-radius: 10px;
      margin: 0.5rem 0;
      width: 100%;
      text-align: left;
      cursor: pointer;
      transition: all 0.3s ease;
      font-size: 1rem;
      color: #3c4043;
  }
  
  .option-button:hover {
      border-color: #4285f4;
      background: #f8f9ff;
      transform: translateX(5px);
  }
  
  .option-correct {
      background: #e8f5e8 !important;
      border-color: #34a853 !important;
      color: #137333 !important;
      font-weight: 500;
  }
  
  .option-incorrect {
      background: #fce8e6 !important;
      border-color: #ea4335 !important;
      color: #d33b2c !important;
  }
  
  .explanation-box {
      background: #f8f9fa;
      border-left: 4px solid #34a853;
      padding: 1.5rem;
      border-radius: 8px;
      margin: 1rem 0;
      font-style: italic;
      color: #5f6368;
  }
  
  .stats-container {
      display: flex;
      justify-content: space-around;
      background: white;
      padding: 2rem;
      border-radius: 15px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      margin: 2rem 0;
  }
  
  .stat-item {
      text-align: center;
  }
  
  .stat-number {
      font-size: 2.5rem;
      font-weight: 700;
      color: #1a73e8;
      display: block;
  }
  
  .stat-label {
      font-size: 0.9rem;
      color: #5f6368;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.5px;
  }
  
  .results-container {
      background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
      padding: 2.5rem;
      border-radius: 20px;
      text-align: center;
      margin: 2rem 0;
      border: 2px solid #ff9800;
  }
  
  .results-score {
      font-size: 4rem;
      font-weight: 700;
      color: #e65100;
      margin-bottom: 1rem;
  }
  
  .results-message {
      font-size: 1.3rem;
      color: #bf360c;
      font-weight: 500;
      margin-bottom: 2rem;
  }
  
  .category-badge {
      background: #e3f2fd;
      color: #1976d2;
      padding: 0.3rem 0.8rem;
      border-radius: 15px;
      font-size: 0.8rem;
      font-weight: 500;
      display: inline-block;
      margin-bottom: 1rem;
  }
  
  .software-example {
      background: #f8f9fa;
      padding: 1.5rem;
      border-radius: 10px;
      margin: 1rem 0;
      border-left: 3px solid #4285f4;
  }
  
  .software-name {
      font-weight: 600;
      color: #1a73e8;
      font-size: 1.1rem;
      margin-bottom: 0.5rem;
  }
  
  .software-description {
      color: #5f6368;
      margin-bottom: 1rem;
      line-height: 1.5;
  }
  
  .software-details {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      font-size: 0.9rem;
  }
  
  .detail-item {
      color: #3c4043;
  }
  
  .detail-label {
      font-weight: 500;
      color: #1a73e8;
  }
  
  .comparison-table {
      background: white;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      margin: 2rem 0;
  }
  
  .table-header {
      background: #4285f4;
      color: white;
      padding: 1rem;
      font-weight: 600;
  }
  
  .table-row {
      padding: 1rem;
      border-bottom: 1px solid #e8eaed;
  }
  
  .table-row:nth-child(even) {
      background: #f8f9fa;
  }
  
  .btn-primary {
      background: linear-gradient(135deg, #4285f4 0%, #1a73e8 100%);
      color: white;
      border: none;
      padding: 1rem 2rem;
      border-radius: 25px;
      font-weight: 600;
      font-size: 1rem;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 4px 15px rgba(66, 133, 244, 0.3);
  }
  
  .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(66, 133, 244, 0.4);
  }
  
  .btn-secondary {
      background: white;
      color: #4285f4;
      border: 2px solid #4285f4;
      padding: 1rem 2rem;
      border-radius: 25px;
      font-weight: 600;
      font-size: 1rem;
      cursor: pointer;
      transition: all 0.3s ease;
  }
  
  .btn-secondary:hover {
      background: #4285f4;
      color: white;
  }
  
  @keyframes fadeInUp {
      from {
          opacity: 0;
          transform: translateY(30px);
      }
      to {
          opacity: 1;
          transform: translateY(0);
      }
  }
  
  .fade-in {
      animation: fadeInUp 0.6s ease-out;
  }
  
  @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
  }
  
  .pulse {
      animation: pulse 2s infinite;
  }
</style>
""", unsafe_allow_html=True)

# Base de datos profesional de ejemplos de software
EJEMPLOS_SOFTWARE_PROFESIONAL = {
  "Sistemas Operativos": {
      "libre": [
          {
              "nombre": "Ubuntu Linux",
              "descripcion": "Distribución de Linux más popular para escritorio, conocida por su facilidad de uso y amplio soporte comunitario",
              "licencia": "GPL v3 + Licencias adicionales",
              "desarrollador": "Canonical Ltd.",
              "año": 2004,
              "ventajas": ["Completamente gratuito", "Altamente seguro", "Personalizable", "Gran comunidad de soporte", "Actualizaciones regulares"],
              "desventajas": ["Curva de aprendizaje inicial", "Compatibilidad limitada con algunos juegos", "Menos software comercial disponible"],
              "uso_principal": "Escritorio personal, desarrollo de software, servidores web",
              "cuota_mercado": "2.6% escritorio mundial",
              "empresas_usuarios": ["Netflix", "Tesla", "SpaceX"]
          },
          {
              "nombre": "Debian GNU/Linux",
              "descripcion": "Sistema operativo universal conocido por su estabilidad y filosofía de software completamente libre",
              "licencia": "DFSG (Debian Free Software Guidelines)",
              "desarrollador": "Proyecto Debian",
              "año": 1993,
              "ventajas": ["Extremadamente estable", "Amplio repositorio de software", "Seguridad robusta", "Arquitecturas múltiples"],
              "desventajas": ["Ciclos de actualización lentos", "Configuración más técnica", "Software menos actualizado"],
              "uso_principal": "Servidores críticos, sistemas embebidos, base para otras distribuciones",
              "cuota_mercado": "Base para Ubuntu y 100+ distribuciones",
              "empresas_usuarios": ["Google", "NASA", "CERN"]
          }
      ],
      "privado": [
          {
              "nombre": "Microsoft Windows 11",
              "descripcion": "Sistema operativo más utilizado en escritorios, con interfaz moderna y integración con servicios Microsoft",
              "licencia": "Licencia Propietaria Microsoft",
              "desarrollador": "Microsoft Corporation",
              "año": 2021,
              "ventajas": ["Interfaz familiar", "Amplia compatibilidad de software", "Soporte técnico oficial", "Integración con Office 365"],
              "desventajas": ["Costo de licencia elevado", "Recopilación de datos telemetría", "Actualizaciones forzadas", "Vulnerabilidades frecuentes"],
              "uso_principal": "Escritorio empresarial, gaming, aplicaciones de oficina",
              "cuota_mercado": "73% del mercado de escritorio",
              "empresas_usuarios": ["La mayoría de empresas Fortune 500"]
          },
          {
              "nombre": "Apple macOS",
              "descripcion": "Sistema operativo exclusivo de Apple, conocido por su diseño elegante y integración con el ecosistema Apple",
              "licencia": "Licencia Propietaria Apple",
              "desarrollador": "Apple Inc.",
              "año": 2001,
              "ventajas": ["Diseño elegante y intuitivo", "Integración perfecta con dispositivos Apple", "Excelente para creativos", "Seguridad avanzada"],
              "desventajas": ["Limitado a hardware Apple", "Costo muy elevado", "Menos personalizable", "Dependencia del ecosistema Apple"],
              "uso_principal": "Diseño gráfico, desarrollo iOS, producción multimedia",
              "cuota_mercado": "15.6% del mercado de escritorio",
              "empresas_usuarios": ["Pixar", "Adobe", "muchas agencias creativas"]
          }
      ]
  },
  "Navegadores Web": {
      "libre": [
          {
              "nombre": "Mozilla Firefox",
              "descripcion": "Navegador web enfocado en privacidad y personalización, desarrollado por una organización sin fines de lucro",
              "licencia": "Mozilla Public License 2.0",
              "desarrollador": "Mozilla Foundation",
              "año": 2004,
              "ventajas": ["Privacidad por defecto", "Extensiones potentes", "Código abierto auditable", "No rastrea usuarios"],
              "desventajas": ["Menor cuota de mercado", "Algunos sitios optimizados para Chrome", "Consumo de memoria variable"],
              "uso_principal": "Navegación privada, desarrollo web, usuarios conscientes de privacidad",
              "cuota_mercado": "7.6% mundial",
              "empresas_usuarios": ["Tor Project", "DuckDuckGo", "organizaciones de privacidad"]
          },
          {
              "nombre": "Chromium",
              "descripcion": "Proyecto de código abierto que sirve como base para Google Chrome y otros navegadores",
              "licencia": "Licencia BSD",
              "desarrollador": "Proyecto Chromium (Google)",
              "año": 2008,
              "ventajas": ["Código abierto", "Base de muchos navegadores", "Rápido y eficiente", "Sin servicios propietarios de Google"],
              "desventajas": ["Menos funciones que Chrome", "Actualizaciones manuales", "Menos soporte para usuarios finales"],
              "uso_principal": "Base para otros navegadores, desarrollo, usuarios técnicos",
              "cuota_mercado": "Base para 65%+ de navegadores",
              "empresas_usuarios": ["Microsoft Edge", "Opera", "Brave"]
          }
      ],
      "privado": [
          {
              "nombre": "Google Chrome",
              "descripcion": "Navegador web más popular del mundo, desarrollado por Google con integración completa de servicios Google",
              "licencia": "Licencia Propietaria Google",
              "desarrollador": "Google LLC",
              "año": 2008,
              "ventajas": ["Velocidad excepcional", "Sincronización entre dispositivos", "Amplia compatibilidad web", "Actualizaciones automáticas"],
              "desventajas": ["Recopilación extensiva de datos", "Alto consumo de memoria", "Dependencia de servicios Google"],
              "uso_principal": "Navegación general, aplicaciones web, integración con Google Workspace",
              "cuota_mercado": "65.1% mundial",
              "empresas_usuarios": ["Mayoría de empresas que usan Google Workspace"]
          },
          {
              "nombre": "Microsoft Edge",
              "descripcion": "Navegador moderno de Microsoft, reemplazó a Internet Explorer con motor Chromium",
              "licencia": "Licencia Propietaria Microsoft",
              "desarrollador": "Microsoft Corporation",
              "año": 2015,
              "ventajas": ["Integración con Windows", "Funciones de productividad", "Seguridad empresarial", "Eficiencia energética"],
              "desventajas": ["Limitado principalmente a ecosistema Microsoft", "Menor extensión de mercado", "Recopilación de datos"],
              "uso_principal": "Navegación en Windows, entornos empresariales Microsoft",
              "cuota_mercado": "4.2% mundial",
              "empresas_usuarios": ["Empresas con infraestructura Microsoft"]
          }
      ]
  },
  "Suites Ofimáticas": {
      "libre": [
          {
              "nombre": "LibreOffice",
              "descripcion": "Suite ofimática completa y profesional, compatible con formatos Microsoft Office",
              "licencia": "Mozilla Public License 2.0",
              "desarrollador": "The Document Foundation",
              "año": 2011,
              "ventajas": ["Completamente gratuito", "Compatible con formatos MS Office", "Multiplataforma", "Sin suscripciones"],
              "desventajas": ["Interfaz menos moderna", "Funciones colaborativas limitadas", "Curva de aprendizaje para usuarios de Office"],
              "uso_principal": "Documentos profesionales, hojas de cálculo, presentaciones",
              "cuota_mercado": "100+ millones de usuarios",
              "empresas_usuarios": ["Gobierno francés", "Gobierno italiano", "muchas universidades"]
          },
          {
              "nombre": "Apache OpenOffice",
              "descripcion": "Suite ofimática de código abierto, precursora de LibreOffice",
              "licencia": "Apache License 2.0",
              "desarrollador": "Apache Software Foundation",
              "año": 2012,
              "ventajas": ["Gratuito", "Estable", "Soporte para múltiples idiomas", "Formatos estándar abiertos"],
              "desventajas": ["Desarrollo más lento", "Interfaz desactualizada", "Menos funciones modernas"],
              "uso_principal": "Oficina básica, educación, organizaciones con presupuesto limitado",
              "cuota_mercado": "Millones de descargas anuales",
              "empresas_usuarios": ["Organizaciones educativas", "ONGs"]
          }
      ],
      "privado": [
          {
              "nombre": "Microsoft Office 365",
              "descripcion": "Suite ofimática líder mundial con servicios en la nube y colaboración avanzada",
              "licencia": "Licencia Propietaria Microsoft",
              "desarrollador": "Microsoft Corporation",
              "año": 1990,
              "ventajas": ["Funciones avanzadas", "Colaboración en tiempo real", "Integración cloud", "Soporte profesional"],
              "desventajas": ["Costo elevado de suscripción", "Dependencia de internet", "Recopilación de datos"],
              "uso_principal": "Oficina profesional, colaboración empresarial, productividad",
              "cuota_mercado": "1.2 mil millones de usuarios",
              "empresas_usuarios": ["85% de empresas Fortune 500"]
          },
          {
              "nombre": "Google Workspace",
              "descripcion": "Suite de productividad basada en la nube con colaboración en tiempo real",
              "licencia": "Licencia Propietaria Google",
              "desarrollador": "Google LLC",
              "año": 2006,
              "ventajas": ["Colaboración excelente", "Basado en la nube", "Integración con servicios Google", "Actualizaciones automáticas"],
              "desventajas": ["Funciones limitadas offline", "Dependencia de Google", "Menos funciones avanzadas que Office"],
              "uso_principal": "Colaboración en línea, startups, educación",
              "cuota_mercado": "3 mil millones de usuarios",
              "empresas_usuarios": ["Spotify", "Airbnb", "muchas startups"]
          }
      ]
  }
}

# Preguntas profesionales del quiz
PREGUNTAS_QUIZ_PROFESIONAL = [
  {
      "pregunta": "¿Cuál es la principal diferencia filosófica entre software libre y software privado?",
      "opciones": [
          "El software libre es siempre gratuito, el privado siempre es de pago",
          "El software libre garantiza las cuatro libertades fundamentales del usuario",
          "El software libre es menos seguro que el privado",
          "El software privado tiene mejor calidad que el libre"
      ],
      "respuesta_correcta": 1,
      "explicacion": "El software libre se basa en las cuatro libertades fundamentales: ejecutar, estudiar, redistribuir y mejorar el software. Esta filosofía contrasta con el software privado que restringe estas libertades.",
      "categoria": "Fundamentos",
      "dificultad": "Intermedio"
  },
  {
      "pregunta": "¿Qué navegador web libre es conocido por su enfoque en la privacidad del usuario?",
      "opciones": [
          "Google Chrome",
          "Microsoft Edge",
          "Mozilla Firefox",
          "Safari"
      ],
      "respuesta_correcta": 2,
      "explicacion": "Mozilla Firefox es desarrollado por una organización sin fines de lucro y se enfoca en proteger la privacidad del usuario, bloqueando rastreadores por defecto y siendo completamente de código abierto.",
      "categoria": "Navegadores",
      "dificultad": "Básico"
  },
  {
      "pregunta": "¿Cuál de estos sistemas operativos tiene la mayor cuota de mercado en escritorios?",
      "opciones": [
          "Ubuntu Linux",
          "macOS",
          "Windows 11",
          "Debian"
      ],
      "respuesta_correcta": 2,
      "explicacion": "Windows 11 (y versiones anteriores de Windows) mantiene aproximadamente el 73% de la cuota de mercado en escritorios a nivel mundial, siendo el sistema operativo más utilizado.",
      "categoria": "Sistemas Operativos",
      "dificultad": "Básico"
  },
  {
      "pregunta": "¿Qué suite ofimática libre es más compatible con los formatos de Microsoft Office?",
      "opciones": [
          "Apache OpenOffice",
          "LibreOffice",
          "Google Docs",
          "WPS Office"
      ],
      "respuesta_correcta": 1,
      "explicacion": "LibreOffice ofrece la mejor compatibilidad con formatos de Microsoft Office (.docx, .xlsx, .pptx) entre las suites ofimáticas libres, y se actualiza constantemente para mantener esta compatibilidad.",
      "categoria": "Oficina",
      "dificultad": "Intermedio"
  },
  {
      "pregunta": "¿Cuál es una ventaja clave del software libre en términos de seguridad?",
      "opciones": [
          "Nunca tiene vulnerabilidades",
          "El código puede ser auditado por cualquier persona",
          "Solo lo usan expertos en seguridad",
          "Las empresas no lo atacan"
      ],
      "respuesta_correcta": 1,
      "explicacion": "La transparencia del código fuente permite que investigadores de seguridad, desarrolladores y usuarios auditen el código, identifiquen vulnerabilidades y contribuyan a su corrección rápidamente.",
      "categoria": "Seguridad",
      "dificultad": "Intermedio"
  },
  {
      "pregunta": "¿Qué modelo de negocio es más común en las empresas de software libre?",
      "opciones": [
          "Venta de licencias de uso",
          "Publicidad integrada en el software",
          "Servicios de soporte, consultoría y personalización",
          "Suscripciones mensuales obligatorias"
      ],
      "respuesta_correcta": 2,
      "explicacion": "Las empresas de software libre generalmente monetizan a través de servicios profesionales como soporte técnico, consultoría, implementación, capacitación y desarrollo personalizado.",
      "categoria": "Modelos de Negocio",
      "dificultad": "Avanzado"
  },
  {
      "pregunta": "¿Cuál de estas distribuciones Linux es conocida por su extrema estabilidad en servidores?",
      "opciones": [
          "Ubuntu",
          "Fedora",
          "Debian",
          "Arch Linux"
      ],
      "respuesta_correcta": 2,
      "explicacion": "Debian es reconocida por su estabilidad excepcional, con ciclos de prueba exhaustivos y actualizaciones conservadoras, siendo la elección preferida para servidores críticos y sistemas de producción.",
      "categoria": "Sistemas Operativos",
      "dificultad": "Intermedio"
  },
  {
      "pregunta": "¿Qué porcentaje aproximado del mercado de navegadores web tiene Google Chrome?",
      "opciones": [
          "45%",
          "55%",
          "65%",
          "75%"
      ],
      "respuesta_correcta": 2,
      "explicacion": "Google Chrome mantiene aproximadamente el 65% de la cuota de mercado mundial de navegadores web, siendo el navegador más utilizado en la mayoría de plataformas.",
      "categoria": "Navegadores",
      "dificultad": "Avanzado"
  },
  {
      "pregunta": "¿Cuál es la principal desventaja del software libre para usuarios no técnicos?",
      "opciones": [
          "Es muy caro",
          "No se puede modificar",
          "Puede tener una curva de aprendizaje más pronunciada",
          "No funciona en computadoras modernas"
      ],
      "respuesta_correcta": 2,
      "explicacion": "El software libre a menudo requiere más conocimientos técnicos para instalación, configuración y uso optimal, lo que puede representar un desafío para usuarios menos experimentados.",
      "categoria": "Usabilidad",
      "dificultad": "Básico"
  },
  {
      "pregunta": "¿Qué empresas importantes utilizan Ubuntu Linux en su infraestructura?",
      "opciones": [
          "Solo pequeñas startups",
          "Netflix, Tesla y SpaceX",
          "Únicamente universidades",
          "Solo servidores web básicos"
      ],
      "respuesta_correcta": 1,
      "explicacion": "Grandes empresas tecnológicas como Netflix, Tesla y SpaceX utilizan Ubuntu Linux en su infraestructura crítica, demostrando su confiabilidad y escalabilidad empresarial.",
      "categoria": "Casos de Uso",
      "dificultad": "Avanzado"
  },
  {
      "pregunta": "¿Cuál es la licencia más común para el software libre?",
      "opciones": [
          "MIT License",
          "GPL (General Public License)",
          "Apache License",
          "BSD License"
      ],
      "respuesta_correcta": 1,
      "explicacion": "La GPL (General Public License) es la licencia de software libre más utilizada, especialmente la GPL v3, que garantiza que el software y sus derivados permanezcan libres.",
      "categoria": "Licencias",
      "dificultad": "Intermedio"
  },
  {
      "pregunta": "¿Qué suite ofimática tiene más usuarios a nivel mundial?",
      "opciones": [
          "LibreOffice",
          "Google Workspace",
          "Microsoft Office 365",
          "Apache OpenOffice"
      ],
      "respuesta_correcta": 2,
      "explicacion": "Microsoft Office 365 tiene más de 1.2 mil millones de usuarios y es utilizado por el 85% de las empresas Fortune 500, siendo la suite ofimática más popular mundialmente.",
      "categoria": "

