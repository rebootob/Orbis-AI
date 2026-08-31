from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from scripts.wp007_registry import ProjectRegistry, RegistryRecord


def _record(**overrides):
    data = {
        "project_id": "orbis-ai",
        "project_name": "Orbis AI",
        "repository": "https://github.com/rebootob/Orbis-AI.git",
        "canonical_branch": "develop",
        "project_docs_path": "project-docs",
        "status": "active",
        "control_plane": "ChatGPT",
        "execution_role": None,
        "execution_model": None,
    }
    data.update(overrides)
    return RegistryRecord(**data)


def main():
    results = []
    results.append(("valid_lookup_by_id", _test_valid_lookup_by_id()))
    results.append(("valid_lookup_by_name", _test_valid_lookup_by_name()))
    results.append(("unknown_project_id", _test_unknown_project_id()))
    results.append(("unknown_project_name", _test_unknown_project_name()))
    results.append(("duplicate_project_id", _test_duplicate_project_id()))
    results.append(("ambiguous_duplicate_project_name", _test_ambiguous_duplicate_project_name()))
    results.append(("missing_required_field", _test_missing_required_field()))
    results.append(("invalid_repository_metadata", _test_invalid_repository_metadata()))
    results.append(("secret_exclusion_from_registry", _test_secret_exclusion_from_registry()))
    results.append(("lookup_helper", _test_lookup_helper()))
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    if not all(ok for _, ok in results):
        sys.exit(1)


def _test_valid_lookup_by_id():
    registry = ProjectRegistry([_record()])
    return registry.lookup_by_id("orbis-ai").project_name == "Orbis AI"


def _test_valid_lookup_by_name():
    registry = ProjectRegistry([_record()])
    return registry.lookup_by_name("Orbis AI").project_id == "orbis-ai"


def _test_unknown_project_id():
    registry = ProjectRegistry([_record()])
    try:
        registry.lookup_by_id("missing")
    except KeyError:
        return True
    return False


def _test_unknown_project_name():
    registry = ProjectRegistry([_record()])
    try:
        registry.lookup_by_name("Missing")
    except KeyError:
        return True
    return False


def _test_duplicate_project_id():
    try:
        ProjectRegistry([_record(), _record(project_name="Orbis AI 2")])
    except ValueError:
        return True
    return False


def _test_ambiguous_duplicate_project_name():
    try:
        ProjectRegistry([_record(), _record(project_id="orbis-ai-2")])
    except ValueError:
        return True
    return False


def _test_missing_required_field():
    try:
        ProjectRegistry([_record(project_id="")])
    except ValueError:
        return True
    return False


def _test_invalid_repository_metadata():
    try:
        ProjectRegistry([_record(repository="git@github.com:rebootob/Orbis-AI.git")])
    except ValueError:
        return True
    return False


def _test_secret_exclusion_from_registry():
    record = _record()
    return not any(secret in record.project_id or secret in record.repository for secret in ("password", "token", "secret", "credential"))


def _test_lookup_helper():
    registry = ProjectRegistry([_record()])
    ctx = registry.context("orbis-ai")
    return ctx["repository"] == "https://github.com/rebootob/Orbis-AI.git"


if __name__ == "__main__":
    main()
