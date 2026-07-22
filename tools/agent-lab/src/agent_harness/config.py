from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    model_base_url: str = os.getenv("MODEL_BASE_URL", "https://api.openai.com/v1")
    model_api_key: str = os.getenv("MODEL_API_KEY", "")
    model_name: str = os.getenv("MODEL_NAME", "")
    db_path: str = os.getenv("AGENT_DB", "./data/agent.sqlite3")
    user_id: str = os.getenv("AGENT_USER", "default-user")
    max_steps: int = int(os.getenv("AGENT_MAX_STEPS", "8"))
    agent_profile_dir: str = os.getenv("AGENT_PROFILE_DIR", "agents/tesis")
    project_root: str = os.getenv("AGENT_PROJECT_ROOT", ".")
    obsidian_vault_dir: str = os.getenv("OBSIDIAN_VAULT_DIR", ".")

    def validate_model(self) -> None:
        missing = [name for name, value in {
            "MODEL_BASE_URL": self.model_base_url,
            "MODEL_API_KEY": self.model_api_key,
            "MODEL_NAME": self.model_name,
        }.items() if not value or value.startswith("pon_")]
        if missing:
            raise RuntimeError(
                "Faltan variables de entorno para usar el modelo: " + ", ".join(missing)
            )
