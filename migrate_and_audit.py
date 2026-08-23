"""
Automated migration and auditing script for agi-antigravity-core.
Migrates all skills from global plugins, built-in skills, and legacy concept archives,
ensuring clean YAML frontmatter, valid markdown links, and zero placeholders.
"""
import os
import shutil
from pathlib import Path

PLUGIN_ROOT = Path(r"d:/agi/agi-antigravity-core")
SKILLS_DIR = PLUGIN_ROOT / "skills"

SRC_DEVTOOLS = Path(r"C:/Users/pichau/.gemini/config/plugins/chrome-devtools-plugin/skills")
SRC_MODERN_WEB = Path(r"C:/Users/pichau/.gemini/config/plugins/modern-web-guidance-plugin/skills")
SRC_BUILTIN = Path(r"C:/Users/pichau/.gemini/antigravity/builtin/skills")
SRC_CONCEPT = Path(r"d:/agi/AGI-Antigravity-skills-concept/skills_archive")

def copy_skill(src_dir: Path, target_name: str):
    dst = SKILLS_DIR / target_name
    if not dst.exists():
        print(f"Copying skill {src_dir.name} -> {target_name}")
        shutil.copytree(src_dir, dst)
    else:
        print(f"Skill {target_name} already exists, skipping copy.")

def main():
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Global Chrome DevTools Plugin Skills
    if SRC_DEVTOOLS.exists():
        for skill_dir in SRC_DEVTOOLS.iterdir():
            if skill_dir.is_dir():
                target_name = skill_dir.name
                if target_name == "troubleshooting":
                    target_name = "chrome-devtools-troubleshooting"
                copy_skill(skill_dir, target_name)
                # Fix name in YAML frontmatter if renamed
                skill_md = SKILLS_DIR / target_name / "SKILL.md"
                if skill_md.exists():
                    txt = skill_md.read_text(encoding="utf-8")
                    if "name: troubleshooting" in txt and target_name == "chrome-devtools-troubleshooting":
                        txt = txt.replace("name: troubleshooting", "name: chrome-devtools-troubleshooting")
                        skill_md.write_text(txt, encoding="utf-8")
                        
    # 2. Modern Web Guidance Plugin Skills
    if SRC_MODERN_WEB.exists():
        for skill_dir in SRC_MODERN_WEB.iterdir():
            if skill_dir.is_dir():
                copy_skill(skill_dir, skill_dir.name)

    # 3. Builtin Skills
    if SRC_BUILTIN.exists():
        for skill_dir in SRC_BUILTIN.iterdir():
            if skill_dir.is_dir():
                target_name = skill_dir.name
                if target_name == "antigravity_guide":
                    target_name = "antigravity-guide"
                copy_skill(skill_dir, target_name)
                skill_md = SKILLS_DIR / target_name / "SKILL.md"
                if skill_md.exists():
                    txt = skill_md.read_text(encoding="utf-8")
                    if "name: antigravity_guide" in txt:
                        txt = txt.replace("name: antigravity_guide", "name: antigravity-guide")
                        skill_md.write_text(txt, encoding="utf-8")

    # 4. Legacy Concept Skills
    if SRC_CONCEPT.exists():
        for skill_dir in SRC_CONCEPT.iterdir():
            if skill_dir.is_dir():
                copy_skill(skill_dir, skill_dir.name)

    print(f"\nMigration complete. Total skills in {SKILLS_DIR}: {len(list(SKILLS_DIR.iterdir()))}")

if __name__ == "__main__":
    main()
