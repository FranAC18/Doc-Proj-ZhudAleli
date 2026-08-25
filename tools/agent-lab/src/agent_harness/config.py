from dataclasses import dataclass
import os

from dotenv import load_dotenv

from .adapters.deepseek import DeepSeekAdapter
from .adapters.gemini import GeminiAdapter
from .adapters.glm import GLMAdapter
from .adapters.openai import OpenAIAdapter
from .paths import resolve_project_path, resolve_project_root, resolve_vault_dir
from .router import ModelRouter

load_dotenv()


@dataclass(frozen=True)
class Settings:
    default_provider: str = os.getenv("MODEL_PROVIDER", "openai")
    default_model: str = os.getenv("MODEL_NAME", "gpt-5.6-luna")

    # OpenAI
    openai_api_key: str = os.getenv("OPENAI_API_KEY", os.getenv("MODEL_API_KEY", ""))
    openai_base_url: str = os.getenv("OPENAI_BASE_URL", os.getenv("MODEL_BASE_URL", "https://api.openai.com/v1"))

    # DeepSeek
    deepseek_api_key: str = os.getenv("DEEPSEEK_API_KEY", "")
    deepseek_base_url: str = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")

    # GLM / Z.AI
    glm_api_key: str = os.getenv("ZAI_API_KEY", os.getenv("GLM_API_KEY", ""))
    glm_base_url: str = os.getenv("ZAI_BASE_URL", "https://api.z.ai/api/coding/paas/v4")

    # Google Gemini
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", os.getenv("GOOGLE_API_KEY", ""))
    gemini_base_url: str = os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta")

    # Rutas y almacenamiento
    db_path: str = os.getenv("AGENT_DB", "./data/agent.sqlite3")
    user_id: str = os.getenv("AGENT_USER", "default-user")
    max_steps: int = int(os.getenv("AGENT_MAX_STEPS", "8"))
    agent_profile_dir: str = os.getenv("AGENT_PROFILE_DIR", "agents/tesis")
    project_root: str = os.getenv("AGENT_PROJECT_ROOT", "")
    obsidian_vault_dir: str = os.getenv("OBSIDIAN_VAULT_DIR", "")

    def __post_init__(self) -> None:
        root = resolve_project_root(self.project_root)
        vault = resolve_vault_dir(self.obsidian_vault_dir, root)
        db_path = resolve_project_path(self.db_path, root, label="AGENT_DB")
        profile_dir = resolve_project_path(self.agent_profile_dir, root, label="AGENT_PROFILE_DIR")
        object.__setattr__(self, "project_root", str(root))
        object.__setattr__(self, "obsidian_vault_dir", str(vault))
        object.__setattr__(self, "db_path", str(db_path))
        object.__setattr__(self, "agent_profile_dir", str(profile_dir))

    # Propiedades para retrocompatibilidad
    @property
    def model_base_url(self) -> str:
        return self.openai_base_url

    @property
    def model_api_key(self) -> str:
        return self.openai_api_key

    @property
    def model_name(self) -> str:
        return self.default_model

    def build_router(self) -> ModelRouter:
        """Construye y puebla el ModelRouter con los adaptadores disponibles."""
        router = ModelRouter(default_model=self.default_model, default_provider=self.default_provider)

        # 1. Registrar OpenAI
        openai_adapter = OpenAIAdapter(
            base_url=self.openai_base_url,
            api_key=self.openai_api_key,
            model_name=self.default_model if self.default_provider == "openai" else "gpt-5.6-luna",
        )
        router.register("openai:gpt-5.6-luna", openai_adapter)
        router.register("gpt-5.6-luna", openai_adapter)
        router.register("openai:gpt-5.6-sol", OpenAIAdapter(base_url=self.openai_base_url, api_key=self.openai_api_key, model_name="gpt-5.6-sol"))
        router.register("gpt-5.6-sol", OpenAIAdapter(base_url=self.openai_base_url, api_key=self.openai_api_key, model_name="gpt-5.6-sol"))

        # 2. Registrar DeepSeek
        deepseek_adapter = DeepSeekAdapter(
            base_url=self.deepseek_base_url,
            api_key=self.deepseek_api_key,
            model_name="deepseek-v4",
        )
        router.register("deepseek:deepseek-v4", deepseek_adapter)
        router.register("deepseek-v4", deepseek_adapter)
        router.register("deepseek:deepseek-chat", DeepSeekAdapter(base_url=self.deepseek_base_url, api_key=self.deepseek_api_key, model_name="deepseek-chat"))
        router.register("deepseek-chat", DeepSeekAdapter(base_url=self.deepseek_base_url, api_key=self.deepseek_api_key, model_name="deepseek-chat"))

        # 3. Registrar GLM
        glm_adapter = GLMAdapter(
            base_url=self.glm_base_url,
            api_key=self.glm_api_key,
            model_name="glm-5.2",
        )
        router.register("glm:glm-5.2", glm_adapter)
        router.register("glm-5.2", glm_adapter)
        router.register("glm:glm-4", GLMAdapter(base_url=self.glm_base_url, api_key=self.glm_api_key, model_name="glm-4"))
        router.register("glm-4", GLMAdapter(base_url=self.glm_base_url, api_key=self.glm_api_key, model_name="glm-4"))

        # 4. Registrar Google Gemini
        gemini_models = (
            "gemini-2.5-pro",
            "gemini-2.5-flash",
            "gemini-3.7-flash",
            "gemini-3.6-flash",
            "gemini-3.5-flash",
            "gemini-3.1-pro",
        )
        for model_name in gemini_models:
            adapter = GeminiAdapter(
                base_url=self.gemini_base_url,
                api_key=self.gemini_api_key,
                model_name=model_name,
            )
            router.register(f"google:{model_name}", adapter)
            router.register(model_name, adapter)

        return router

    def validate_model(self) -> None:
        """Valida que exista al menos una configuración básica de proveedor."""
        pass
