$ErrorActionPreference = "Stop"

$raizProjeto = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$python = Join-Path $raizProjeto ".venv\Scripts\python.exe"
$entrada = Join-Path $PSScriptRoot "conciliacao_contabil_razoes.py"
$pastaDist = Join-Path $PSScriptRoot "dist"
$pastaBuildCurta = Join-Path $env:TEMP "conciliacao_contabil_razoes_build"
$pastaWork = Join-Path $pastaBuildCurta "work"
$pastaSpec = Join-Path $pastaBuildCurta "spec"

# Usa caminho curto para reduzir risco de WinError 206 em ambientes Windows com caminhos longos.
if (Test-Path -LiteralPath $pastaBuildCurta) {
    Remove-Item -LiteralPath $pastaBuildCurta -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $pastaDist, $pastaWork, $pastaSpec | Out-Null

& $python -X utf8 -m PyInstaller `
    --clean `
    --onefile `
    --console `
    --name "Conciliacao_Contabil_Razoes_SAP_HANA" `
    --distpath $pastaDist `
    --workpath $pastaWork `
    --specpath $pastaSpec `
    --hidden-import fastexcel `
    --hidden-import tkinter `
    --hidden-import tkinter.filedialog `
    --exclude-module pandas `
    --exclude-module jinja2 `
    $entrada

if ($LASTEXITCODE -ne 0) {
    throw "Falha ao gerar o executavel. Codigo de saida: $LASTEXITCODE"
}

$executavel = Join-Path $pastaDist "Conciliacao_Contabil_Razoes_SAP_HANA.exe"
if (-not (Test-Path -LiteralPath $executavel)) {
    throw "Executavel nao encontrado em: $executavel"
}

Write-Host ""
Write-Host "Executavel gerado em:" -ForegroundColor Green
Write-Host $executavel

