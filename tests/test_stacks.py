"""Tests for stack profile rendering and validation."""

from specify_cli.stacks import (
    APPROVED_STACKS,
    STACK_CONTEXT_FILE,
    StackProfile,
    load_stack_profile_from_context,
    render_stack_context,
    validate_stack_context_content,
)


class TestStackContextValidation:
    def test_rendered_stack_context_contains_required_sections(self):
        content = render_stack_context(APPROVED_STACKS["laravel-inertia-react"])

        assert "## Purpose / Typical Use" in content
        assert "## When This Stack Fits" in content
        assert "## When This Stack Is a Poor Fit" in content
        assert "## Core Constraints" in content
        assert "## Security Controls" in content
        assert "## Security Pitfalls" in content
        assert "## Security Evidence" in content
        assert validate_stack_context_content(content) == []

    def test_all_approved_stacks_define_security_sections(self) -> None:
        for stack_id, profile in APPROVED_STACKS.items():
            assert isinstance(profile, StackProfile)
            assert profile.security_controls, f"{stack_id}: security_controls empty"
            assert profile.security_pitfalls, f"{stack_id}: security_pitfalls empty"
            assert profile.security_evidence, f"{stack_id}: security_evidence empty"
            rendered = render_stack_context(profile)
            assert validate_stack_context_content(rendered) == [], stack_id

    def test_validation_rejects_incomplete_context(self):
        content = """---
stack_id: laravel-inertia-react
stack_name: Laravel + Inertia + React
---

# Project Stack Profile

## Selected Stack

- **ID**: laravel-inertia-react
- **Name**: Laravel + Inertia + React

## Purpose / Typical Use

- Modern Laravel apps.
"""

        errors = validate_stack_context_content(content)
        assert any("When This Stack Fits" in err for err in errors)
        assert any("Things To Avoid" in err for err in errors)

    def test_load_stack_profile_from_context_reads_valid_profile(self, tmp_path):
        context_path = tmp_path / STACK_CONTEXT_FILE
        context_path.parent.mkdir(parents=True, exist_ok=True)
        context_path.write_text(
            render_stack_context(APPROVED_STACKS["moodle5-plugin"]),
            encoding="utf-8",
        )

        profile, errors = load_stack_profile_from_context(tmp_path)

        assert errors == []
        assert profile is not None
        assert profile.key == "moodle5-plugin"

    def test_load_stack_profile_from_context_rejects_corrupt_profile(self, tmp_path):
        context_path = tmp_path / STACK_CONTEXT_FILE
        context_path.parent.mkdir(parents=True, exist_ok=True)
        context_path.write_text(
            "---\nstack_id: invalid-stack\nstack_name: Broken\n---\n\n# Broken\n",
            encoding="utf-8",
        )

        profile, errors = load_stack_profile_from_context(tmp_path)

        assert profile is None
        assert errors
