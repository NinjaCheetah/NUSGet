# Build.ps1 for NUSGet

# Default option is to run build, like a Makefile
param(
    [string]$Task = "build"
)

$buildNUSGet = {
    Write-Host "Building NUSGet..."
    python build_translations.py
    python -m nuitka --show-progress --assume-yes-for-downloads NUSGet.py
}

$cleanNUSGet = {
    Write-Host "Cleaning..."
    Remove-Item -Recurse -Force NUSGet.exe, ./NUSGet.build/, ./NUSGet.dist/, ./NUSGet.onefile-build/
}

switch ($Task.ToLower()) {
    "build" {
        & $buildNUSGet
        break
    }
    "clean" {
        & $cleanNUSGet
        break
    }
    default {
        Write-Host "Unknown task: $Task" -ForegroundColor Red
        Write-Host "Available tasks: build, clean"
        break
    }
}
