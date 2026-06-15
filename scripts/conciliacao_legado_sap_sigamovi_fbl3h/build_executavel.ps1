# Build do executavel Windows para o case de conciliacao Legado x SAP
# Execute a partir da raiz do repositorio.

$ErrorActionPreference = "Stop"

$ScriptPath = "scripts/conciliacao_legado_sap_sigamovi_fbl3h/conciliacao_legado_sap_sigamovi_fbl3h.py"
$AppName = "conciliacao_legado_sap_sigamovi_fbl3h"

python -m pip install --upgrade pip
python -m pip install pandas numpy openpyxl pyinstaller

pyinstaller `
  --onefile `
  --noconsole `
  --name $AppName `
  $ScriptPath

Write-Host "Build concluido. Verifique a pasta dist/." -ForegroundColor Green
