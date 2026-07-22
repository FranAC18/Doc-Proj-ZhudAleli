import argparse
import sys

from .agent import Agent
from .config import Settings
from .memory import MemoryStore
from .obsidian import ObsidianStore
from .provider import OpenAICompatibleModel
from .tools import build_tools


def main() -> None:
    parser = argparse.ArgumentParser(description="Agente con arnés local y memoria SQLite")
    parser.add_argument("--once", help="Ejecuta una consulta y termina")
    parser.add_argument("--list-lessons", action="store_true", help="Lista lecciones pendientes de aprobación")
    parser.add_argument("--approve-lesson", type=int, help="Aprueba una lección pendiente por ID")
    args = parser.parse_args()

    settings = Settings()
    if args.list_lessons or args.approve_lesson is not None:
        memory = MemoryStore(settings.db_path)
        try:
            if args.approve_lesson is not None:
                ok = memory.approve_lesson(settings.user_id, args.approve_lesson)
                print("Lección aprobada." if ok else "No se encontró una lección pendiente con ese ID.")
            else:
                for lesson in memory.pending_lessons(settings.user_id):
                    print(f"[{lesson['id']}] {lesson['trigger']} → {lesson['lesson']}")
        finally:
            memory.close()
        return

    try:
        settings.validate_model()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        print("Copia .env.example a .env y completa sus valores.", file=sys.stderr)
        raise SystemExit(2)

    memory = MemoryStore(settings.db_path)
    model = OpenAICompatibleModel(settings.model_base_url, settings.model_api_key, settings.model_name)
    obsidian = ObsidianStore(settings.obsidian_vault_dir)
    agent = Agent(
        model,
        memory,
        build_tools(memory, settings.user_id, obsidian),
        settings.user_id,
        settings.max_steps,
        settings.agent_profile_dir,
        settings.project_root,
    )

    try:
        if args.once:
            print(agent.run(args.once))
            return
        print("Agente listo. Escribe 'salir' para terminar.")
        while True:
            try:
                text = input("\nTú> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if text.lower() in {"salir", "exit", "quit"}:
                break
            if text:
                try:
                    print(f"\nAgente> {agent.run(text)}")
                except Exception as exc:
                    print(f"\nError controlado: {exc}", file=sys.stderr)
    finally:
        memory.close()


if __name__ == "__main__":
    main()
