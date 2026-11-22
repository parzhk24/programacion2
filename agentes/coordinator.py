from typing import List, Optional
from agents import Agent


class MultiAgentCoordinator:
    """
    Coordinador de flujo de trabajo Multi-Agente.
    Aplica el principio de Composición (POO) para coordinar la interacción,
    comunicación y transferencia de tareas entre diferentes agentes.
    """

    def __init__(self, name: str = "Coordinator"):
        self.name = name
        self._agents: List[Agent] = []

    def register_agent(self, agent: Agent) -> None:
        """Registra un agente en el equipo colaborativo."""
        self._agents.append(agent)
        print(f"[{self.name}] Agente registrado: {agent.name} (Rol: {agent.role})")

    def run_pipeline(self, initial_topic: str) -> str:
        """
        Ejecuta un flujo colaborativo en tubería (Pipeline):
        1. El primer agente (ej. Investigador) procesa el tema.
        2. El resultado se transfiere como entrada al segundo agente (ej. Redactor).
        """
        print(f"\n========================================================")
        print(f"INICIANDO SISTEMA MULTI-AGENTE: {self.name}")
        print(f"TEMA INICIAL: {initial_topic}")
        print(f"========================================================")

        current_input = initial_topic

        for i, agent in enumerate(self._agents):
            print(f"\n>>> Paso {i+1}: Delegando trabajo a '{agent.name}' ({agent.role})")
            
            # Ejecución del agente (Polimorfismo: todos responden a .act())
            result = agent.act(current_input)
            
            # Comunicación inter-agente: el resultado del paso actual es el insumo del siguiente
            current_input = result

        print(f"\n========================================================")
        print(f"PIPELINE COMPLETADO EXITOSAMENTE")
        print(f"========================================================")
        return current_input
