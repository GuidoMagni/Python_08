import os
from dotenv import load_dotenv

# python3 -m venv venv
#     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
#     pip install python-dotenv

load_dotenv()


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...\n")
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    missing_vars = []
    if not matrix_mode:
        missing_vars.append("MATRIX_MODE")
        matrix_mode = "development"
    if not database_url:
        missing_vars.append("DATABASE_URL")
    if not api_key:
        missing_vars.append("API_KEY")
    if not log_level:
        missing_vars.append("LOG_LEVEL")
        log_level = "WARNING"
    if not zion_endpoint:
        missing_vars.append("ZION_ENDPOINT")

    if missing_vars:
        print("⚠️  WARNING: Missing configuration variables."
              " Using defaults or indicating absence:")
        for var in missing_vars:
            print(f"  - {var} was not found.")
        print()

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    if database_url:
        if matrix_mode == "production":
            print("Database: Connected to remote instance")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Offline (DATABASE_URL missing)")
    if api_key and api_key != "your_secret_api_key_here":
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated (API_KEY missing)")
    print(f"Log Level: {log_level}")
    if zion_endpoint:
        if matrix_mode == "production":
            print("Zion Network: SECURE TUNNEL ESTABLISHED")
        else:
            print("Zion Network: Online")
    else:
        print("Zion Network: Offline (ZION_ENDPOINT missing)")

    print("\nEnvironment security check:")
    if (api_key == "your_secret_api_key_here" or
        database_url and ("user:password" in database_url or
                          "password@localhost" in database_url)):
        print("[WARNING] Potential hardcoded secrets or placeholders"
              " detected! Review your configurations.")
    else:
        print("[OK] No hardcoded secrets detected")

    gitignore_exists = os.path.exists(".gitignore")
    env_exists = os.path.exists(".env")
    env_is_ignored = False
    if gitignore_exists:
        try:
            with open(".gitignore", "r", encoding="utf-8") as f:
                gitignore_content = f.read()
                if ".env" in gitignore_content.split():
                    env_is_ignored = True
        except IOError:
            print("[WARNING] Could not read .gitignore file.")
    if env_exists and env_is_ignored:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file security check failed")

    if matrix_mode == "production":
        print("[OK] Production overrides in use")
        if zion_endpoint and "secure" in zion_endpoint.lower():
            print("  - Secure Zion Endpoint configured for production.")
    else:
        print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
