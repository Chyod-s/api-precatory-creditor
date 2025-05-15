$env:PIP_REQUIRE_VIRTUALENV = "true"

function pip-update-reqs {
    Start-Sleep -Seconds 1 
    python -m pip freeze | Out-File -Encoding ASCII "$PWD\requirements.txt" -Force
}

function pip {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$args)
    & python -m pip install @args
    pip-update-reqs
}

function pipu {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$args)
    & python -m pip uninstall -y @args
    pip-update-reqs
}
