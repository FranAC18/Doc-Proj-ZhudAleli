param(
    [Parameter(Position = 0)]
    [ValidateSet("codex", "kimi", "glm", "help")]
    [string]$Profile = "help"
)

$ErrorActionPreference = "Stop"

function Assert-Command([string]$Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "No se encontró '$Name' en PATH. Instala el motor antes de continuar."
    }
}

switch ($Profile) {
    "codex" {
        Assert-Command "codex"
        & codex
        exit $LASTEXITCODE
    }
    "kimi" {
        Assert-Command "kimi"
        & kimi
        exit $LASTEXITCODE
    }
    "glm" {
        Assert-Command "kimi"
        if ([string]::IsNullOrWhiteSpace($env:ZAI_API_KEY)) {
            throw "Define ZAI_API_KEY en la sesión. La clave no se leerá desde archivos del proyecto."
        }
        if ([string]::IsNullOrWhiteSpace($env:GLM_MODEL)) {
            throw "Define GLM_MODEL con una versión disponible. El proyecto no fija un modelo GLM obligatorio."
        }

        $names = @(
            "KIMI_MODEL_NAME",
            "KIMI_MODEL_PROVIDER_TYPE",
            "KIMI_MODEL_BASE_URL",
            "KIMI_MODEL_API_KEY",
            "KIMI_MODEL_MAX_CONTEXT_SIZE",
            "KIMI_MODEL_CAPABILITIES",
            "KIMI_MODEL_DISPLAY_NAME"
        )
        $previous = @{}
        foreach ($name in $names) {
            $previous[$name] = [Environment]::GetEnvironmentVariable($name, "Process")
        }

        try {
            $env:KIMI_MODEL_NAME = $env:GLM_MODEL
            $env:KIMI_MODEL_PROVIDER_TYPE = "openai"
            $env:KIMI_MODEL_BASE_URL = if ($env:ZAI_BASE_URL) { $env:ZAI_BASE_URL } else { "https://api.z.ai/api/coding/paas/v4" }
            $env:KIMI_MODEL_API_KEY = $env:ZAI_API_KEY
            $env:KIMI_MODEL_MAX_CONTEXT_SIZE = if ($env:GLM_MAX_CONTEXT_SIZE) { $env:GLM_MAX_CONTEXT_SIZE } else { "1000000" }
            $env:KIMI_MODEL_CAPABILITIES = if ($env:GLM_CAPABILITIES) { $env:GLM_CAPABILITIES } else { "thinking,tool_use" }
            $env:KIMI_MODEL_DISPLAY_NAME = if ($env:GLM_DISPLAY_NAME) { $env:GLM_DISPLAY_NAME } else { $env:GLM_MODEL }

            & kimi
            $exitCode = $LASTEXITCODE
        }
        finally {
            foreach ($name in $names) {
                if ($null -eq $previous[$name]) {
                    Remove-Item "Env:$name" -ErrorAction SilentlyContinue
                }
                else {
                    [Environment]::SetEnvironmentVariable($name, $previous[$name], "Process")
                }
            }
        }
        exit $exitCode
    }
    default {
        Write-Host "Uso: .\scripts\agent.ps1 <codex|kimi|glm>"
        Write-Host "  codex  Inicia Codex CLI."
        Write-Host "  kimi   Inicia Kimi Code con su configuración local."
        Write-Host "  glm    Perfil opcional; requiere ZAI_API_KEY y GLM_MODEL."
        Write-Host "El script no modifica Git ni guarda credenciales."
    }
}
