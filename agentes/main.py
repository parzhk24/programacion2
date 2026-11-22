#!/usr/bin/env python3
"""
Punto de entrada principal para el Sistema de Agentes de IA con POO.
Demuestra colaboración multi-agente, uso de herramientas y principios de POO.
"""

import sys
import os

def load_dotenv(filepath: str = ".env") -> None:
    """Carga variables desde un archivo .env si existe (sin dependencias externas)."""
    if not os.path.exists(filepath):
        return
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = value
    except Exception:
        pass

# Cargar automáticamente el archivo .env si está presente
load_dotenv()

from tools import WebSearchTool, FileReadTool, FileWriteTool
from llm_client import MockLLMClient, GroqLLMClient, GeminiLLMClient
from agents import ResearchAgent, WriterAgent
from coordinator import MultiAgentCoordinator


def main():
    print("=" * 60)
    print("      SISTEMA MULTI-AGENTE DE IA CON POO EN PYTHON")
    print("=" * 60)
    
    # Selección de LLM según variables de entorno disponibles
    if os.getenv("GROQ_API_KEY"):
        print("[Config] Usando API gratuita de Groq (Llama-3).")
        investigator_llm = GroqLLMClient()
        writer_llm = GroqLLMClient()
    elif os.getenv("GEMINI_API_KEY"):
        print("[Config] Usando API gratuita de Google Gemini.")
        investigator_llm = GeminiLLMClient()
        writer_llm = GeminiLLMClient()
    else:
        print("[Config] Modo offline / de demostración (MockLLMClient activo).")
        print("         (Opcional: defina GROQ_API_KEY o GEMINI_API_KEY para LLM real en vivo)")
        investigator_llm = MockLLMClient(agent_role="Investigador")
        writer_llm = MockLLMClient(agent_role="Redactor")

    # 1. Creación de Herramientas (POO: Instanciación)
    search_tool = WebSearchTool()
    file_writer_tool = FileWriteTool()
    file_reader_tool = FileReadTool()

    # 2. Creación de Agentes y asignación de herramientas (POO: Composición)
    investigator = ResearchAgent(
        name="Agente-Investigador",
        role="Especialista en Investigación y Búsqueda",
        goal="Buscar información relevante, sintetizar datos y extraer hechos clave",
        llm_client=investigator_llm
    )
    investigator.add_tool(search_tool)

    writer = WriterAgent(
        name="Agente-Redactor",
        role="Especialista en Síntesis y Redacción Ejecutiva",
        goal="Transformar hallazgos de investigación en informes estructurados y legibles",
        llm_client=writer_llm
    )
    writer.add_tool(file_writer_tool)
    writer.add_tool(file_reader_tool)

    # 3. Creación del Coordinador Multi-Agente
    coordinator = MultiAgentCoordinator(name="Coordinador de Investigación")
    coordinator.register_agent(investigator)
    coordinator.register_agent(writer)

    # 4. Tema a procesar
    topic = "Ventajas de combinar Inteligencia Artificial con Programación Orientada a Objetos en 2026"
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])

    # 5. Ejecución del sistema
    final_output = coordinator.run_pipeline(topic)

    print("\n--- RESULTADO FINAL ENTREGADO POR EL SISTEMA ---\n")
    print(final_output)
    print("\n------------------------------------------------")
    if os.path.exists("informe_final.txt"):
        print("Se generó el archivo 'informe_final.txt' en el directorio actual.")


if __name__ == "__main__":
    main()
