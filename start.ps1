# Ativa o ambiente virtual no mesmo contexto
. .\venv\Scripts\Activate.ps1

# Espera 2 segundos antes de continuar
Start-Sleep -Seconds 1

# Carrega seu script customizado de funções pip
. .\venv\Scripts\Activate-custom.ps1

Write-Host "Ambiente virtual ativado e funções pip carregadas."
