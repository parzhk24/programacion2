# Sistema Multi-Agente de IA con Programación Orientada a Objetos (POO)

Este proyecto implementa un prototipo de **Sistema Basado en Agentes de Inteligencia Artificial** en Python aplicando principios fundamentales de **Programación Orientada a Objetos (POO)**. Cumple con los requerimientos de resolver un problema real mediante la colaboración de múltiples agentes, herramientas externas y el uso de servicios 100% gratuitos.

---

## 📌 Problema Resuelto: Investigación y Generación Automatizada de Informes

En la investigación tradicional, recopilar información, sintetizar fuentes dispersas y redactar un reporte estructurado requiere mucho tiempo humano y es difícil de programar con algoritmos tradicionales rígidos (que solo entienden reglas fijas o expresiones regulares).

Este sistema resuelve este problema mediante un flujo de trabajo colaborativo en cadena (Pipeline) compuesto por:
1. **Agente Investigador**: Recibe un tema, consulta la web con DuckDuckGo y sintetiza los hallazgos esenciales.
2. **Agente Redactor**: Recibe los hallazgos del investigador, los organiza formalmente con un LLM y guarda el reporte estructurado en disco usando herramientas del sistema de archivos.
3. **Coordinador Multi-Agente**: Administra el ciclo de vida y la comunicación fluida entre los agentes.

---

## 🏛️ Principios de POO Aplicados

El proyecto fue diseñado utilizando buenas prácticas de POO:

- **Abstracción**:
  - `Agent` (clase base abstracta en `agents.py`): define la interfaz común (`act()`, `remember()`, etc.).
  - `Tool` (clase base abstracta en `tools.py`): define la estructura de cualquier herramienta (`execute()`).
  - `LLMClient` (clase base abstracta en `llm_client.py`): desacopla la lógica del agente del proveedor de IA.

- **Herencia**:
  - `ResearchAgent` y `WriterAgent` heredan de `Agent`.
  - `WebSearchTool`, `FileReadTool` y `FileWriteTool` heredan de `Tool`.
  - `GroqLLMClient`, `GeminiLLMClient` y `MockLLMClient` heredan de `LLMClient`.

- **Polimorfismo**:
  - El `MultiAgentCoordinator` no necesita saber qué tipo específico de agente está procesando la tarea; invoca `agent.act()` y cada agente responde con su propio comportamiento especializado.
  - Los agentes ejecutan `tool.execute()` sin preocuparse si la herramienta busca en internet o escribe en disco.

- **Encapsulamiento y Composición**:
  - Los agentes encapsulan su memoria interna (`_memory`) y su diccionario de herramientas (`_tools`).
  - Un agente **contiene** herramientas y un cliente LLM (relación de composición `tiene-un`), lo que permite cambiar el modelo o agregar herramientas en tiempo de ejecución.

---

## 📁 Estructura del Proyecto

```text
.
├── agents.py           # Clases de Agentes (Agent, ResearchAgent, WriterAgent)
├── coordinator.py      # Orquestador del flujo multi-agente (MultiAgentCoordinator)
├── tools.py            # Herramientas (WebSearchTool, FileReadTool, FileWriteTool)
├── llm_client.py       # Clientes de IA (Groq, Gemini y Mock offline)
├── main.py             # Script de entrada ejecutable
├── .env                # Archivo para configurar claves de API (opcional)
├── requirements.txt    # Archivo de dependencias del proyecto
├── informe_final.txt   # Archivo generado por el Agente Redactor (resultado)
└── README.md           # Manual de instalación y uso
```

---

## 🚀 Instalación y Requisitos

### Requisitos
- **Python 3.8+** (utiliza únicamente la librería estándar de Python; **no requiere librerías externas obligatorias**).

### Ejecución Rápida (Sin necesidad de claves API - Modo Demostración)
Puedes ejecutar el sistema directamente con:

```bash
python3 main.py
```

O enviando un tema personalizado por línea de comandos:

```bash
python3 main.py "El impacto de la inteligencia artificial en la medicina moderna"
```

---

## 🔑 Uso de LLMs Gratuitos en Vivo (Google Gemini o Groq)

El sistema incluye soporte nativo y directo mediante peticiones HTTP para modelos gratuitos.

### Configuración con archivo `.env` (Recomendado)
El programa carga automáticamente un archivo `.env` en la raíz del proyecto sin necesidad de librerías externas. Puedes crear un archivo `.env` y definir la clave que prefieras:

```bash
# Para usar Google Gemini (Gratuito en Google AI Studio):
GEMINI_API_KEY="tu_api_key_aqui"

# O para usar Groq (Gratuito en Groq Console):
# GROQ_API_KEY="tu_api_key_aqui"
```

Una vez guardado el archivo `.env`, basta con ejecutar:
```bash
python3 main.py
```

---

### Configuración alternativa vía Variables de Entorno en terminal

Si prefieres no usar el archivo `.env`, puedes exportar la variable directamente en tu terminal:

#### Opción 1: Google Gemini (Gratuito)
1. Obtén tu clave gratuita en [Google AI Studio](https://aistudio.google.com/).
2. Exporta la variable:
   ```bash
   export GEMINI_API_KEY="tu_api_key_aqui"
   ```
3. Ejecuta el sistema:
   ```bash
   python3 main.py
   ```

#### Opción 2: Groq (Llama-3 - Gratuito)
1. Obtén tu clave gratuita en [Groq Console](https://console.groq.com/).
2. Exporta la variable:
   ```bash
   export GROQ_API_KEY="tu_api_key_aqui"
   ```
3. Ejecuta el sistema:
   ```bash
   python3 main.py
   ```

---

## 📄 Archivo de Salida

Tras la ejecución, el **Agente Redactor** almacenará automáticamente el informe final en:
- `informe_final.txt`
