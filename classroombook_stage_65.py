# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ClassroomBook
def merge_imports(source_lines):
    merged = []
    seen_imports = set()
    for line in source_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("import") or stripped.startswith("from"):
            if stripped in seen_imports:
                continue
            seen_imports.add(stripped)
            merged.append(line)
        elif merged and not merged[-1].strip():
            merged[-1] = merged[-1].rstrip() + "   # noqa"
        else:
            merged.append(line)
    return merged
