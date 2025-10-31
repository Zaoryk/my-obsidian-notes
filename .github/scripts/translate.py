#!/usr/bin/env python3
"""
Obsidian Notes Auto-Translator using Google Translate
No API key required
Author: Zaoryk

This script automatically translates Spanish markdown files to English while
preserving all formatting, code blocks, links, and markdown syntax.

Requirements:
    - Python 3.7+
    - deep-translator library (pip install deep-translator)

Usage:
    python translate.py

The script will:
    1. Find all .md files in your configured folders
    2. Translate Spanish content to English
    3. Preserve code blocks, inline code, and links
    4. Save translations to English/ folder
    5. Skip already-translated and up-to-date files
"""

import os
import pathlib
import re
import sys
from deep_translator import GoogleTranslator

# ============================================================================
# CONFIGURATION
# ============================================================================

# Directory structure
SPANISH_ROOT = "."  # Current directory (Spanish notes)
ENGLISH_ROOT = "English"  # Target directory for translations

# Your subject folders (add or remove as needed)
FOLDERS_TO_TRANSLATE = [
    "Aplicaciones Móviles para IoT",
    "Desarrollo de Videojuegos",
    "Ingeniería de Software",
    "Inglés Inicial",
    "Modelamiento de Soluciones Informáticas",
    "Programación Back End",
    "Proyecto Integrado",
    "Archivos"
]

# Translation settings
SOURCE_LANGUAGE = 'es'  # Spanish
TARGET_LANGUAGE = 'en'  # English
CHUNK_SIZE = 4000  # Characters per translation chunk (Google Translate limit)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def should_translate_file(file_path):
    """
    Determine if a file should be translated.
    
    Args:
        file_path (pathlib.Path): Path to the file
        
    Returns:
        bool: True if file should be translated, False otherwise
        
    Skips:
        - Files already in English folder
        - Hidden files and folders (starting with .)
        - Non-markdown files
        - README.md files
    """
    # Skip if already in English folder
    if "English" in str(file_path):
        return False
    
    # Skip hidden files and folders
    if any(part.startswith('.') for part in file_path.parts):
        return False
    
    # Only translate markdown files
    if file_path.suffix != '.md':
        return False
    
    # Skip README.md
    if file_path.name == 'README.md':
        return False
    
    return True

def preserve_and_translate(content):
    """
    Translate markdown content while preserving code blocks and special formatting.
    
    This function:
        1. Extracts and stores code blocks, inline code, and links
        2. Replaces them with placeholder tokens
        3. Translates the remaining text
        4. Restores the preserved elements
    
    Args:
        content (str): Original Spanish markdown content
        
    Returns:
        str: Translated English content with preserved formatting
        
    Preserves:
        - Code blocks: ```code```
        - Inline code: `code`
        - Markdown links: [text](url)
    """
    if not content.strip():
        return content
    
    # Storage for preserved elements
    preserved_items = {
        'code_blocks': [],
        'inline_codes': [],
        'links': []
    }
    
    # Step 1: Preserve code blocks (```code```)
    def save_code_block(match):
        preserved_items['code_blocks'].append(match.group(0))
        return f"\n___CODE_BLOCK_{len(preserved_items['code_blocks'])-1}___\n"
    
    content = re.sub(r'```[\s\S]*?```', save_code_block, content)
    
    # Step 2: Preserve inline code (`code`)
    def save_inline_code(match):
        preserved_items['inline_codes'].append(match.group(0))
        return f"___INLINE_CODE_{len(preserved_items['inline_codes'])-1}___"
    
    content = re.sub(r'`[^`\n]+`', save_inline_code, content)
    
    # Step 3: Preserve markdown links [text](url)
    def save_link(match):
        preserved_items['links'].append(match.group(0))
        return f"___LINK_{len(preserved_items['links'])-1}___"
    
    content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', save_link, content)
    
    # Step 4: Split content into chunks (Google Translate has character limits)
    chunks = []
    current_chunk = ""
    
    for line in content.split('\n'):
        if len(current_chunk + line) > CHUNK_SIZE:
            if current_chunk.strip():
                chunks.append(current_chunk)
            current_chunk = line + '\n'
        else:
            current_chunk += line + '\n'
    
    if current_chunk.strip():
        chunks.append(current_chunk)
    
    # Step 5: Translate each chunk
    translated_chunks = []
    translator = GoogleTranslator(source=SOURCE_LANGUAGE, target=TARGET_LANGUAGE)
    
    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            translated_chunks.append(chunk)
            continue
            
        try:
            print(f"   Translating chunk {i+1}/{len(chunks)}...")
            translated = translator.translate(chunk)
            translated_chunks.append(translated)
            print(f"   ✓ Chunk {i+1} translated ({len(chunk)} chars)")
            
        except Exception as e:
            print(f"   Error translating chunk {i+1}: {e}")
            translated_chunks.append(chunk)  # Keep original on error
    
    # Step 6: Join translated chunks
    translated = ''.join(translated_chunks)
    
    # Step 7: Restore preserved elements
    
    # Restore code blocks
    for i, code_block in enumerate(preserved_items['code_blocks']):
        translated = translated.replace(f"___CODE_BLOCK_{i}___", code_block)
    
    # Restore inline code
    for i, inline_code in enumerate(preserved_items['inline_codes']):
        translated = translated.replace(f"___INLINE_CODE_{i}___", inline_code)
    
    # Restore links
    for i, link in enumerate(preserved_items['links']):
        translated = translated.replace(f"___LINK_{i}___", link)
    
    return translated

def translate_file(spanish_file, english_file):
    """
    Translate a single markdown file from Spanish to English.
    
    Args:
        spanish_file (pathlib.Path): Path to source Spanish file
        english_file (pathlib.Path): Path to target English file
        
    Process:
        1. Read Spanish content
        2. Translate while preserving formatting
        3. Create target directory if needed
        4. Write English content
    """
    print(f"\nTranslating: {spanish_file.name}")
    print(f"   Source: {spanish_file}")
    print(f"   Target: {english_file}")
    
    try:
        # Read Spanish content
        with open(spanish_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Translate content
        translated_content = preserve_and_translate(content)
        
        # Create directory if needed
        english_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write English content
        with open(english_file, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"   Success!")
        
    except Exception as e:
        print(f"   Error: {e}")

def needs_translation(spanish_file, english_file):
    """
    Check if a file needs translation (new or modified).
    
    Args:
        spanish_file (pathlib.Path): Spanish source file
        english_file (pathlib.Path): English target file
        
    Returns:
        bool: True if translation is needed
        
    Logic:
        - If English file doesn't exist: needs translation
        - If Spanish file is newer than English file: needs re-translation
        - Otherwise: skip (already up-to-date)
    """
    # If English file doesn't exist, needs translation
    if not english_file.exists():
        return True
    
    # If Spanish file is newer, needs re-translation
    spanish_mtime = spanish_file.stat().st_mtime
    english_mtime = english_file.stat().st_mtime
    
    return spanish_mtime > english_mtime

# ============================================================================
# MAIN LOGIC
# ============================================================================

def main():
    """
    Main translation function.
    
    Process:
        1. Create English root directory
        2. Iterate through configured folders
        3. Find all markdown files
        4. Translate new or modified files
        5. Print summary statistics
    """
    print("=" * 70)
    print("OBSIDIAN NOTES TRANSLATION: SPANISH → ENGLISH")
    print("=" * 70)
    
    # Create English root directory
    english_root = pathlib.Path(ENGLISH_ROOT)
    english_root.mkdir(exist_ok=True)
    print(f"\nEnglish notes directory: {english_root.absolute()}")
    
    # Statistics tracking
    stats = {
        'total': 0,
        'translated': 0,
        'skipped': 0,
        'errors': 0
    }
    
    # Process each folder
    for folder in FOLDERS_TO_TRANSLATE:
        spanish_folder = pathlib.Path(folder)
        
        if not spanish_folder.exists():
            print(f"\n  Folder not found: {folder}")
            continue
        
        print(f"\n{'='*70}")
        print(f"Processing: {folder}")
        print(f"{'='*70}")
        
        # Find all markdown files recursively
        markdown_files = list(spanish_folder.rglob("*.md"))
        print(f"Found {len(markdown_files)} markdown files")
        
        for spanish_file in markdown_files:
            stats['total'] += 1
            
            # Check if should translate
            if not should_translate_file(spanish_file):
                stats['skipped'] += 1
                continue
            
            # Create corresponding English path
            relative_path = spanish_file.relative_to(spanish_folder)
            english_file = english_root / folder / relative_path
            
            # Check if translation needed
            if needs_translation(spanish_file, english_file):
                try:
                    translate_file(spanish_file, english_file)
                    stats['translated'] += 1
                except Exception as e:
                    print(f"   Failed: {e}")
                    stats['errors'] += 1
            else:
                print(f"\n⏭ Skipping (up to date): {spanish_file.name}")
                stats['skipped'] += 1
    
    # Print summary
    print("\n" + "=" * 70)
    print("TRANSLATION SUMMARY")
    print("=" * 70)
    print(f"Total files found:     {stats['total']}")
    print(f"Translated:         {stats['translated']}")
    print(f"⏭ Skipped (up-to-date): {stats['skipped']}")
    print(f"Errors:             {stats['errors']}")
    print("=" * 70)
    print("\nTranslation complete!\n")

if __name__ == "__main__":
    main()
