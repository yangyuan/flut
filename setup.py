from __future__ import annotations

import os
import shutil
import subprocess
import sys
from shutil import which

from setuptools import setup
from setuptools.command.build_py import build_py


def _repo_root() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def _run_flutter_build() -> None:
    if os.environ.get("FLUT_SKIP_FLUTTER_BUILD") in {"1", "true", "True"}:
        return

    flutter_dir = os.path.join(_repo_root(), "flut", ".flutter")
    if not os.path.isdir(flutter_dir):
        raise RuntimeError(
            "Flut requires the bundled Flutter host project (missing 'flut/.flutter/' directory)."
        )

    flutter_bin = which("flutter")
    if flutter_bin is None:
        raise RuntimeError(
            "Flutter SDK not found on PATH.\n"
            "\n"
            "Why Flutter is required:\n"
            "This package bundles a Flutter host project and, when installing from source, flutter is required.\n"
            "Sometimes pip's isolated build env doesn't inherit your shell init (.bashrc, etc). You can ensure Flutter is on PATH by PATH=/path/to/flutter/bin:$PATH pip install flut.\n"
            "\n"
            "(If you know what you're doing, you can skip this step with FLUT_SKIP_FLUTTER_BUILD=1)"
        )

    if sys.platform.startswith("win"):
        flutter_cmd = flutter_bin
        if flutter_cmd.lower().endswith((".bat", ".cmd")):
            cmd = [
                "cmd",
                "/c",
                flutter_cmd,
                "build",
                "windows",
                "--release",
                "--no-tree-shake-icons",
            ]
        else:
            cmd = [
                flutter_cmd,
                "build",
                "windows",
                "--release",
                "--no-tree-shake-icons",
            ]
    elif sys.platform == "darwin":
        cmd = [flutter_bin, "build", "macos", "--release", "--no-tree-shake-icons"]
    elif sys.platform.startswith("linux"):
        cmd = [flutter_bin, "build", "linux", "--release", "--no-tree-shake-icons"]
    else:
        raise RuntimeError(f"Unsupported platform for Flutter build: {sys.platform}")

    print(f"[flut] Running: {' '.join(cmd)} (cwd={flutter_dir})")
    subprocess.check_call(cmd, cwd=flutter_dir)


def _get_arch() -> str:
    import platform

    machine = platform.machine().lower()
    if machine in ("amd64", "x86_64", "x64"):
        return "x64"
    elif machine in ("arm64", "aarch64"):
        return "arm64"
    return "x64"  # fallback


def _flutter_build_output_is_usable() -> bool:
    flutter_dir = os.path.join(_repo_root(), "flut", ".flutter")
    arch = _get_arch()
    if sys.platform.startswith("win"):
        base = os.path.join(flutter_dir, "build", "windows", arch, "runner", "Release")
        return (
            os.path.exists(os.path.join(base, "flutter_windows.dll"))
            and os.path.isdir(os.path.join(base, "data", "flutter_assets"))
            and os.path.exists(os.path.join(base, "data", "icudtl.dat"))
        )
    if sys.platform == "darwin":
        base = os.path.join(
            flutter_dir,
            "build",
            "macos",
            "Build",
            "Products",
            "Release",
            "flut.app",
        )
        return os.path.isdir(base)
    if sys.platform.startswith("linux"):
        base = os.path.join(flutter_dir, "build", "linux", arch, "release", "bundle")
        return os.path.isdir(base)
    return False


def _copy_flutter_build_output_into_wheel(build_lib: str) -> None:
    flutter_dir = os.path.join(_repo_root(), "flut", ".flutter")
    arch = _get_arch()

    if sys.platform.startswith("win"):
        src = os.path.join(flutter_dir, "build", "windows", arch, "runner", "Release")
        dst = os.path.join(
            build_lib,
            "flut",
            ".flutter",
            "build",
            "windows",
            arch,
            "runner",
            "Release",
        )
    elif sys.platform == "darwin":
        src = os.path.join(
            flutter_dir,
            "build",
            "macos",
            "Build",
            "Products",
            "Release",
            "flut.app",
        )
        dst = os.path.join(
            build_lib,
            "flut",
            ".flutter",
            "build",
            "macos",
            "Build",
            "Products",
            "Release",
            "flut.app",
        )
    elif sys.platform.startswith("linux"):
        src = os.path.join(flutter_dir, "build", "linux", arch, "release", "bundle")
        dst = os.path.join(
            build_lib, "flut", ".flutter", "build", "linux", arch, "release", "bundle"
        )
    else:
        raise RuntimeError(f"Unsupported platform for Flutter build: {sys.platform}")

    if not os.path.exists(src):
        raise RuntimeError(
            f"Flutter build output not found at: {src}. "
            "Install Flutter or build the host project before building this wheel."
        )

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    print(f"[flut] Bundling Flutter build output into wheel: {dst}")
    shutil.copytree(src, dst)


class CustomBuildPy(build_py):
    def run(self):
        super().run()
        if not _flutter_build_output_is_usable():
            _run_flutter_build()

        _copy_flutter_build_output_into_wheel(self.build_lib)


def _get_platform_tag() -> str:
    arch = _get_arch()
    if sys.platform.startswith("win"):
        return "win_arm64" if arch == "arm64" else "win_amd64"
    elif sys.platform == "darwin":
        return "macosx_10_14_universal2"
    elif sys.platform.startswith("linux"):
        return "manylinux2014_aarch64" if arch == "arm64" else "manylinux1_x86_64"
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")


setup(
    include_package_data=False,
    options={
        "bdist_wheel": {
            "plat_name": _get_platform_tag(),
        }
    },
    cmdclass={
        "build_py": CustomBuildPy,
    },
)
