import sys
import os
import site


def main() -> None:
    if sys.prefix != sys.base_prefix:
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        venv_path = os.environ.get('VIRTUAL_ENV')
        if not venv_path:
            venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        package_installation_path = ""
        for path in site.getsitepackages():
            if venv_path in path:
                package_installation_path = path
                break
        if not package_installation_path and site.getsitepackages():
            package_installation_path = site.getsitepackages()[0]
        if not package_installation_path:
            python_version_dir = f"python{sys.version_info.major}."
            f"{sys.version_info.minor}"
            package_installation_path = os.path.join(
                venv_path, "lib", python_version_dir, "site-packages")
        print(f"Package installation path:\n{package_installation_path}")
    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
