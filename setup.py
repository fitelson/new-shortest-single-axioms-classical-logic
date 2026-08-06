import os
import sys
import stat
import subprocess
import urllib.request
import shutil
import argparse
import platform
import zipfile

parser = argparse.ArgumentParser(description="Setup for Short Axiom Searching")

parser.add_argument("--skip_vampire", action='store_true', help="Skip installing vampire")
parser.add_argument("--include_libraries", action='store_true', help="Including installing and updating numpy and scipy")

args = parser.parse_args()

VAMPIRE_VERSION = "5.0.1"
VAMPIRE_TARGET_PATH = "theorem_provers/vampire"
VENDORED_VAMPIRE_PATH = "vendor/vampire-5.0.1/bin/macos-arm64/vampire"

if not args.skip_vampire and not os.path.exists(VAMPIRE_TARGET_PATH):
    vampire_dir = os.path.dirname(VAMPIRE_TARGET_PATH)
    if not os.path.exists(vampire_dir):
        os.makedirs(vampire_dir)

    system = platform.system()
    machine = platform.machine().lower()
    architecture = "ARM64" if machine in {"arm64", "aarch64"} else "X64"
    if system == "Darwin" and architecture == "ARM64" and os.path.isfile(
        VENDORED_VAMPIRE_PATH
    ):
        print(
            f"Installing vendored Vampire {VAMPIRE_VERSION} reference executable"
        )
        shutil.copy2(VENDORED_VAMPIRE_PATH, VAMPIRE_TARGET_PATH)
    elif system not in {"Darwin", "Linux"}:
        raise RuntimeError(
            "Automatic Vampire installation supports macOS and Linux; "
            "install Vampire 5.0.1 manually on this platform."
        )
    else:
        platform_name = "macOS" if system == "Darwin" else "Linux"
        archive_name = f"vampire-{platform_name}-{architecture}.zip"
        vampire_binary_url = (
            "https://github.com/vprover/vampire/releases/download/"
            f"v{VAMPIRE_VERSION}/{archive_name}"
        )
        archive_path = os.path.join("build", archive_name)
        extract_path = os.path.join("build", f"vampire-{VAMPIRE_VERSION}")
        os.makedirs("build", exist_ok=True)

        print(f"Downloading Vampire {VAMPIRE_VERSION} from {vampire_binary_url}")
        urllib.request.urlretrieve(vampire_binary_url, archive_path)
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(extract_path)
        extracted_candidates = [
            os.path.join(root, filename)
            for root, _, filenames in os.walk(extract_path)
            for filename in filenames
            if filename in {"vampire", "vampire.exe"}
        ]
        if len(extracted_candidates) != 1:
            raise RuntimeError(
                f"Expected one Vampire executable in {archive_path}; "
                f"found {len(extracted_candidates)}."
            )
        shutil.copy2(extracted_candidates[0], VAMPIRE_TARGET_PATH)

    print(f"Setting executable permissions for {VAMPIRE_TARGET_PATH}")
    os.chmod(VAMPIRE_TARGET_PATH, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)
    if system == "Darwin":
        subprocess.run(
            ["xattr", "-d", "com.apple.quarantine", VAMPIRE_TARGET_PATH],
            capture_output=True,
            check=False,
        )

    print("Vampire fully setup.")

if not args.skip_vampire:
    vampire_version = subprocess.run(
        [VAMPIRE_TARGET_PATH, "--version"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()[0]
    if not vampire_version.startswith(f"Vampire {VAMPIRE_VERSION}") or (
        "commit 1b13eaf" not in vampire_version
    ):
        raise RuntimeError(
            "Expected Vampire 5.0.1 release commit 1b13eaf, found: "
            f"{vampire_version}"
        )
    print(vampire_version)

if args.include_libraries:
    print("Installing scipy and numpy.")

    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "numpy"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "scipy"])

    print("Setup complete.")

print(
    "The paper's reference Prover9 and Vampire releases are bundled under "
    "vendor/."
)
