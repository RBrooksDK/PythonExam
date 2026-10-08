from pathlib import Path

root = Path("dist")
bundle = root / "xeus" / "python-exam"
packages = bundle / "kernel_packages"

assert (bundle / "bin" / "xpython.wasm").is_file(), "Xeus browser runtime is missing"
assert (root / "xeus" / "kernels.json").is_file(), "Xeus kernel index is missing"

required = (
    "numpy", "scipy", "pandas", "matplotlib", "sympy",
    "statsmodels", "scikit-learn", "openpyxl", "plotly",
)
for name in required:
    assert any(packages.glob(f"{name}-*.tar.gz")), f"{name} is missing from the site"

assert not any(packages.glob("openai-*.tar.gz")), "openai was included unexpectedly"

for config in root.rglob("jupyter-lite.json"):
    data = config.read_text(encoding="utf-8")
    assert "cdn.jsdelivr.net" not in data, f"CDN configured in {config}"
    assert "pyodide-kernel" not in data, f"Pyodide kernel configured in {config}"

print("Site includes the selected packages and a local Xeus runtime")
