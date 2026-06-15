import sys
import importlib

REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}


def check_dependencies() -> tuple[list[str], dict[str, str]]:
    missing = []
    versions = {}
    for pkg in REQUIRED_PACKAGES:
        try:
            mod = importlib.import_module(pkg)
            try:
                versions[pkg] = importlib.metadata.version(pkg)
            except Exception:
                versions[pkg] = getattr(mod, "__version__", "unknown")
        except ImportError:
            missing.append(pkg)
    return missing, versions


def run_analysis() -> None:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    np.random.seed(42)
    raw_data = np.random.randn(1000).cumsum()
    df = pd.DataFrame({"MatrixStream": raw_data})
    print("Generating visualization...\n")
    plt.plot(df["MatrixStream"], color="green")
    plt.title("Matrix Data Stream")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    missing, versions = check_dependencies()
    if missing:
        print()
        print("LOADING STATUS: Error loading programs!\n")
        print("Checking dependencies:")
        for pkg, desc in REQUIRED_PACKAGES.items():
            status = "[MISSING]" if pkg in missing else f"[OK] {pkg}"
            f" ({versions.get(pkg)}) -"
            print(f"{status} {desc}")
        print()
        print("Missing dependencies! Install using:")
        print("Pip:    pip install -r requirements.txt")
        print("Poetry: poetry install")
        sys.exit(1)
    print()
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for pkg, desc in REQUIRED_PACKAGES.items():
        print(f"[OK] {pkg} ({versions.get(pkg)}) - {desc}")
    run_analysis()


if __name__ == "__main__":
    main()
