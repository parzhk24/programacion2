import abc
from typing import List, Dict, Any, Optional
from tools import Tool
from llm_client import LLMClient


class Agent(abc.ABC):
    """
    Clase base abstracta que representa a un Agente Inteligente.
    Aplica:
    - Abstracción: Define el contrato común para todos los agentes.
    - Encapsulamiento: Mantiene protegido el estado interno y la memoria del agente.
    - Composición: Contiene herramientas (Tools) y un motor LLM (LLMClient).
    """

    def __init__(self, name: str, role: str, goal: str, llm_client: LLMClient):
        self._name = name
        self._role = role
        self._goal = goal
        self._llm_client = llm_client
        self._tools: Dict[str, Tool] = {}
        self._memory: List[Dict[str, str]] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def role(self) -> str:
        return self._role

    @property
    def goal(self) -> str:
        return self._goal

    def add_tool(self, tool: Tool) -> None:
        """Agrega una herramienta a la caja de herramientas del agente."""
        self._tools[tool.name] = tool

    def get_tool(self, tool_name: str) -> Optional[Tool]:
        return self._tools.get(tool_name)

    def remember(self, message: str, sender: str = "system") -> None:
        """Almacena información en la memoria interna del agente."""
        self._memory.append({"sender": sender, "message": message})

    def get_memory_context(self) -> str:
        """Retorna un resumen de la memoria contextual."""
        if not self._memory:
            return "Sin historial previo."
        return "\n".join([f"[{item['sender']}]: {item['message']}" for item in self._memory])

    @abc.abstractmethod
    def act(self, task: str) -> str:
        """Método abstracto donde el agente ejecuta su lógica específica."""
        pass


class ResearchAgent(Agent):
    """
    Agente especializado en recopilar información y buscar datos.
    Hereda de Agent (POO: Herencia).
    """

    def act(self, task: str) -> str:
        print(f"\n[{self.name} - {self.role}] Iniciando investigación sobre: '{task}'...")
        
        # Uso de su herramienta de búsqueda (POO: Composición)
        search_tool = self.get_tool("DuckDuckGo Search")
        search_data = ""
        if search_tool:
            print(f"[{self.name}] Consultando herramienta externa: {search_tool.name}...")
            search_data = search_tool.execute(query=task)
        
        system_prompt = (
            f"Eres {self.name}, un agente de IA con el rol de {self.role}.\n"
            f"Tu objetivo principal es: {self.goal}.\n"
            "Analiza el tema y la información encontrada. Devuelve hallazgos clave, claros y fundamentados."
        )

        user_prompt = (
            f"Tema a investigar: {task}\n"
            f"Información recolectada por herramientas:\n{search_data}\n\n"
            "Sintetiza los hallazgos principales en puntos clave estructurados."
        )

        findings = self._llm_client.generate(prompt=user_prompt, system_prompt=system_prompt)
        self.remember(f"Investigación sobre '{task}':\n{findings}", sender="self")
        print(f"[{self.name}] Investigación concluida con éxito.")
        return findings


class WriterAgent(Agent):
    """
    Agente especializado en sintetizar, estructurar y redactar informes finales.
    Hereda de Agent (POO: Herencia).
    """

    def act(self, task: str) -> str:
        print(f"\n[{self.name} - {self.role}] Redactando informe formal...")

        file_writer = self.get_tool("File Writer")

        system_prompt = (
            f"Eres {self.name}, un agente de IA con el rol de {self.role}.\n"
            f"Tu meta es: {self.goal}.\n"
            "Tu tarea es recibir datos sin procesar o hallazgos y transformarlos en un reporte ejecutivo profesional."
        )

        user_prompt = (
            f"Con base en la siguiente información investigada:\n\n{task}\n\n"
            "Genera un informe final con la siguiente estructura:\n"
            "1. TÍTULO DEL INFORME\n"
            "2. RESUMEN EJECUTIVO\n"
            "3. PUNTOS CLAVE Y ANÁLISIS\n"
            "4. CONCLUSIÓN Y RECOMENDACIÓN"
        )

        report = self._llm_client.generate(prompt=user_prompt, system_prompt=system_prompt)
        
        # Si tiene herramienta para guardar archivos, guarda el informe
        if file_writer:
            output_file = "informe_final.txt"
            print(f"[{self.name}] Guardando reporte con {file_writer.name} en '{output_file}'...")
            file_writer.execute(file_path=output_file, content=report)

        self.remember(f"Reporte redactado:\n{report}", sender="self")
        print(f"[{self.name}] Redacción finalizada.")
        return report
