import abc
import json
import urllib.request
import urllib.error
import os
from typing import List, Dict, Any, Optional


class LLMClient(abc.ABC):
    """Interfaz abstracta para clientes de Modelos de Lenguaje."""
    
    @abc.abstractmethod
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Genera una respuesta de texto a partir de un prompt."""
        pass


class MockLLMClient(LLMClient):
    """
    Cliente simulado de respaldo (Fallback/Offline) que permite probar 
    y demostrar el flujo completo sin necesidad de conexión o API Key externa.
    """
    def __init__(self, agent_role: str = "Asistente"):
        self.agent_role = agent_role

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        if "investigador" in self.agent_role.lower():
            return (
                "HALLAZGOS DE INVESTIGACIÓN:\n"
                "- La Programación Orientada a Objetos (POO) aporta modularidad, encapsulamiento y tipos claros.\n"
                "- Los Agentes de IA añaden razonamiento probabilístico, procesamiento semántico y adaptación dinámica.\n"
                "- Juntos resuelven la rigidez de los algoritmos tradicionales basados en reglas estáticas."
            )
        elif "redactor" in self.agent_role.lower():
            return (
                "INFORME EJECUTIVO FINAL:\n"
                "1. Resumen: La integración de POO con agentes inteligentes transforma sistemas rígidos en arquitecturas adaptativas.\n"
                "2. Conclusión: Mientras la POO estructura las herramientas y el estado, el agente interpreta el contexto no estructurado."
            )
        return f"[Simulación - {self.agent_role}] He procesado la solicitud con éxito."


class GroqLLMClient(LLMClient):
    """
    Cliente para la API Gratuita de Groq (Llama 3 / Mixtral).
    Requiere una API Key gratuita de https://console.groq.com/
    """
    def __init__(self, api_key: Optional[str] = None, model: str = "llama-3.1-8b-instant"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.model = model
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        if not self.api_key:
            raise ValueError("GROQ_API_KEY no encontrada. Configure la variable de entorno o use MockLLMClient.")

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        data = json.dumps({
            "model": self.model,
            "messages": messages,
            "temperature": 0.5
        }).encode("utf-8")

        req = urllib.request.Request(
            self.url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )

        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"]
        except Exception as e:
            raise RuntimeError(f"Error al llamar a la API de Groq: {e}")


class GeminiLLMClient(LLMClient):
    """
    Cliente para la API Gratuita de Google Gemini.
    Requiere una API Key gratuita de Google AI Studio.
    """
    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-flash-lite-latest"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY no encontrada. Configure la variable de entorno o use MockLLMClient.")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        
        contents = []
        if system_prompt:
            contents.append({"role": "user", "parts": [{"text": f"Instrucción de sistema: {system_prompt}"}]})
        contents.append({"role": "user", "parts": [{"text": prompt}]})

        data = json.dumps({"contents": contents}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            raise RuntimeError(f"Error al llamar a la API de Gemini: {e}")
