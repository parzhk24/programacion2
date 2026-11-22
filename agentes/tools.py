import abc
import os
import json
import urllib.request
import urllib.parse
from typing import Any, List, Dict, Optional


class Tool(abc.ABC):
    """Clase base abstracta para cualquier herramienta del sistema (POO: Abstracción)."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abc.abstractmethod
    def execute(self, **kwargs) -> Any:
        """Método abstracto que cada herramienta especializada debe implementar."""
        pass


class WebSearchTool(Tool):
    """
    Herramienta gratuita para búsqueda web utilizando la API pública/gratuita de DuckDuckGo Instant Answer.
    """
    def __init__(self):
        super().__init__(
            name="DuckDuckGo Search",
            description="Busca resúmenes y temas generales en la web utilizando DuckDuckGo (100% gratuito)."
        )

    def execute(self, query: str) -> str:
        try:
            params = urllib.parse.urlencode({"q": query, "format": "json", "no_html": 1, "skip_disambig": 1})
            url = f"https://api.duckduckgo.com/?{params}"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (IA-Agent-Bot/1.0)"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            
            abstract = data.get("AbstractText", "")
            if abstract:
                return f"[DuckDuckGo Abstract]: {abstract}"
            
            # Si no hay abstract directo, recolectar temas relacionados
            related_topics = data.get("RelatedTopics", [])
            snippets = []
            for item in related_topics[:3]:
                if isinstance(item, dict) and "Text" in item:
                    snippets.append(f"- {item['Text']}")
            
            if snippets:
                return "\n".join(snippets)
            
            return f"No se encontraron resúmenes directos para '{query}'. Se utilizará conocimiento base."
        except Exception as e:
            return f"Aviso de búsqueda: No fue posible consultar la red ({e}). Usando contexto disponible."


class FileReadTool(Tool):
    """Herramienta para leer archivos de texto locales del sistema de archivos."""
    def __init__(self):
        super().__init__(
            name="File Reader",
            description="Lee el contenido de un archivo de texto en el sistema."
        )

    def execute(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            return f"Error: El archivo '{file_path}' no existe."
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error al leer '{file_path}': {e}"


class FileWriteTool(Tool):
    """Herramienta para persistir resultados e informes en archivos locales."""
    def __init__(self):
        super().__init__(
            name="File Writer",
            description="Escribe o guarda texto en un archivo del sistema."
        )

    def execute(self, file_path: str, content: str) -> str:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return f"Archivo guardado exitosamente en '{file_path}'."
        except Exception as e:
            return f"Error al escribir en '{file_path}': {e}"
