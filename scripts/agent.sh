#!/usr/bin/env bash
set -euo pipefail

profile="${1:-help}"

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "No se encontró '$1' en PATH. Instala el motor antes de continuar." >&2
    exit 127
  fi
}

case "$profile" in
  codex)
    require_command codex
    exec codex
    ;;
  kimi)
    require_command kimi
    exec kimi
    ;;
  glm)
    require_command kimi
    if [[ -z "${ZAI_API_KEY:-}" ]]; then
      echo "Define ZAI_API_KEY en la sesión. La clave no se leerá desde archivos del proyecto." >&2
      exit 2
    fi
    if [[ -z "${GLM_MODEL:-}" ]]; then
      echo "Define GLM_MODEL con una versión disponible. El proyecto no fija un modelo GLM obligatorio." >&2
      exit 2
    fi
    export KIMI_MODEL_NAME="$GLM_MODEL"
    export KIMI_MODEL_PROVIDER_TYPE="openai"
    export KIMI_MODEL_BASE_URL="${ZAI_BASE_URL:-https://api.z.ai/api/coding/paas/v4}"
    export KIMI_MODEL_API_KEY="$ZAI_API_KEY"
    export KIMI_MODEL_MAX_CONTEXT_SIZE="${GLM_MAX_CONTEXT_SIZE:-1000000}"
    export KIMI_MODEL_CAPABILITIES="${GLM_CAPABILITIES:-thinking,tool_use}"
    export KIMI_MODEL_DISPLAY_NAME="${GLM_DISPLAY_NAME:-$GLM_MODEL}"
    exec kimi
    ;;
  help|-h|--help)
    cat <<'EOF'
Uso: ./scripts/agent.sh <perfil>

Perfiles:
  codex  Inicia Codex CLI con la configuración local del usuario.
  kimi   Inicia Kimi Code con su proveedor/modelo local.
  glm    Perfil opcional; requiere ZAI_API_KEY y GLM_MODEL.

El script no modifica Git ni guarda credenciales.
EOF
    ;;
  *)
    echo "Perfil desconocido: $profile. Usa codex, kimi o glm." >&2
    exit 2
    ;;
esac
