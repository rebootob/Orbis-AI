#!/usr/bin/env python3
"""WP-007 Project Registry: minimal version-controlled lookup."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


REQUIRED_FIELDS = (
    "project_id",
    "project_name",
    "repository",
    "canonical_branch",
    "project_docs_path",
    "status",
    "control_plane",
)


@dataclass(frozen=True)
class RegistryRecord:
    project_id: str
    project_name: str
    repository: str
    canonical_branch: str
    project_docs_path: str
    status: str
    control_plane: str
    execution_role: Optional[str] = None
    execution_model: Optional[str] = None

    def validate(self) -> List[str]:
        errors: List[str] = []
        for field in REQUIRED_FIELDS:
            value = getattr(self, field, None)
            if value is None or (isinstance(value, str) and not value.strip()):
                errors.append(f"missing required field: {field}")
        if not self.repository.startswith("http://") and not self.repository.startswith("https://"):
            errors.append("invalid repository metadata: repository must be http(s)")
        return errors


class ProjectRegistry:
    def __init__(self, records: Iterable[RegistryRecord]) -> None:
        self.records: List[RegistryRecord] = []
        self._by_id: Dict[str, RegistryRecord] = {}
        self._by_name: Dict[str, List[RegistryRecord]] = {}
        for record in records:
            errors = record.validate()
            if errors:
                raise ValueError(f"invalid registry record {record.project_id}: {errors}")
            if record.project_id in self._by_id:
                raise ValueError(f"duplicate project_id: {record.project_id}")
            self.records.append(record)
            self._by_id[record.project_id] = record
            name_key = record.project_name.lower()
            self._by_name.setdefault(name_key, []).append(record)
            if len(self._by_name[name_key]) > 1:
                raise ValueError(f"ambiguous duplicate project_name: {record.project_name}")

    def lookup_by_id(self, project_id: str) -> RegistryRecord:
        record = self._by_id.get(project_id)
        if record is None:
            raise KeyError(f"unknown project_id: {project_id}")
        return record

    def lookup_by_name(self, project_name: str) -> RegistryRecord:
        matches = self._by_name.get(project_name.lower())
        if not matches:
            raise KeyError(f"unknown project_name: {project_name}")
        if len(matches) > 1:
            raise ValueError(f"ambiguous duplicate project_name: {project_name}")
        return matches[0]

    def context(self, project_id: str) -> Dict[str, str]:
        record = self.lookup_by_id(project_id)
        return {
            "project_id": record.project_id,
            "project_name": record.project_name,
            "repository": record.repository,
            "canonical_branch": record.canonical_branch,
            "project_docs_path": record.project_docs_path,
            "status": record.status,
            "control_plane": record.control_plane,
            "execution_role": record.execution_role or "",
            "execution_model": record.execution_model or "",
        }


def _default_registry() -> ProjectRegistry:
    registry_file = Path(__file__).with_suffix(".txt")
    records: List[RegistryRecord] = []
    if registry_file.exists():
        for line in registry_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [part.strip() for part in line.split("|")]
            if len(parts) < 7:
                raise ValueError(f"invalid registry line: {line}")
            records.append(
                RegistryRecord(
                    project_id=parts[0],
                    project_name=parts[1],
                    repository=parts[2],
                    canonical_branch=parts[3],
                    project_docs_path=parts[4],
                    status=parts[5],
                    control_plane=parts[6],
                    execution_role=parts[7] if len(parts) > 7 and parts[7] else None,
                    execution_model=parts[8] if len(parts) > 8 and parts[8] else None,
                )
            )
    return ProjectRegistry(records)


_registry: Optional[ProjectRegistry] = None


def get_registry() -> ProjectRegistry:
    global _registry
    if _registry is None:
        _registry = _default_registry()
    return _registry


def lookup(project_id: Optional[str] = None, project_name: Optional[str] = None) -> Dict[str, str]:
    if project_id and project_name:
        raise ValueError("provide exactly one of project_id or project_name")
    if not project_id and not project_name:
        raise ValueError("missing lookup key")
    registry = get_registry()
    if project_id:
        record = registry.lookup_by_id(project_id)
    else:
        record = registry.lookup_by_name(project_name or "")
    return {
        "project_id": record.project_id,
        "project_name": record.project_name,
        "repository": record.repository,
        "canonical_branch": record.canonical_branch,
        "project_docs_path": record.project_docs_path,
        "status": record.status,
        "control_plane": record.control_plane,
        "execution_role": record.execution_role or "",
        "execution_model": record.execution_model or "",
    }
