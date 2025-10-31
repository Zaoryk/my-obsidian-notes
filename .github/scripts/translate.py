import os
import pathlib
import re
import sys
from deep_translator import GoogleTranslator

SPANISH_ROOT = "."
ENGLISH_ROOT = "English"

FOLDERS_TO_TRANSLATE = [
    "Aplicaciones Móviles para IoT",
    "Desarrollo de Videojuegos",
    "Ingeniería de Software",
    "Inglés Inicial",
    "Modelamiento de Soluciones Informáticas",
    "Programación Back End",
    "Proyecto Integrado",
    "Archivos",
    "Apuntes"
]

FOLDER_NAME_TRANSLATIONS = {
    "Aplicaciones Móviles para IoT": "Mobile Applications for IoT",
    "Desarrollo de Videojuegos": "Video Game Development",
    "Ingeniería de Software": "Software Engineering",
    "Inglés Inicial": "Initial English",
    "Modelamiento de Soluciones Informáticas": "IT Solutions Modeling",
    "Programación Back End": "Back End Programming",
    "Proyecto Integrado": "Integrated Project",
    "Archivos": "Files",
    "Apuntes": "Notes"
}

SOURCE_LANGUAGE = 'es'
TARGET_LANGUAGE = 'en'
CHUNK_SIZE = 4000

def should_translate_file(file_path):
    if "English" in str(file_path):
        return False
    if any(part.startswith('.') for part in file_path.parts):
        return False
    if file_path.suffix != '.md':
        return False
    if file_path.name == 'README.md':
        return False
    return True

def preserve_and_translate(content):
    if not content.strip():
        return content
    
    preserved_items = {
        'code_blocks': [],
        'inline_codes': [],
        'links': []
    }
    
    def save_code_block(match):
        preserved_items['code_blocks'].append(match.group(0))
        return f"\n___CODE_BLOCK_{len(preserved_items['code_blocks'])-1}___\n"
    
    content = re.sub(r'```[\s\S]*?```', save_code_block, content)
    
    def save_inline_code(match):
        preserved_items['inline_codes'].append(match.group(0))
        return f"___INLINE_CODE_{len(preserved_items['inline_codes'])-1}___"
    
    content = re.sub(r'`[^`\n]+`', save_inline_code, content)
    
    def save_link(match):
        preserved_items['links'].append(match.group(0))
        return f"___LINK_{len(preserved_items['links'])-1}___"
    
    content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', save_link, content)
    
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
    
    translated_chunks = []
    translator = GoogleTranslator(source=SOURCE_LANGUAGE, target=TARGET_LANGUAGE)
    
    for chunk in chunks:
        if not chunk.strip():
            translated_chunks.append(chunk)
            continue
        
        try:
            translated = translator.translate(chunk)
            translated_chunks.append(translated)
        except:
            translated_chunks.append(chunk)
    
    translated = ''.join(translated_chunks)
    
    for i, code_block in enumerate(preserved_items['code_blocks']):
        translated = translated.replace(f"___CODE_BLOCK_{i}___", code_block)
    
    for i, inline_code in enumerate(preserved_items['inline_codes']):
        translated = translated.replace(f"___INLINE_CODE_{i}___", inline_code)
    
    for i, link in enumerate(preserved_items['links']):
        translated = translated.replace(f"___LINK_{i}___", link)
    
    return translated

def translate_file(spanish_file, english_file):
    try:
        with open(spanish_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translated_content = preserve_and_translate(content)
        
        english_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(english_file, 'w', encoding='utf-8') as f:
            f.write(translated_content)
    except:
        pass

def needs_translation(spanish_file, english_file):
    if not english_file.exists():
        return True
    
    spanish_mtime = spanish_file.stat().st_mtime
    english_mtime = english_file.stat().st_mtime
    
    return spanish_mtime > english_mtime

def get_english_folder_name(spanish_folder_name):
    return FOLDER_NAME_TRANSLATIONS.get(spanish_folder_name, spanish_folder_name)

def main():
    english_root = pathlib.Path(ENGLISH_ROOT)
    english_root.mkdir(exist_ok=True)
    
    for folder in FOLDERS_TO_TRANSLATE:
        spanish_folder = pathlib.Path(folder)
        
        if not spanish_folder.exists():
            continue
        
        english_folder_name = get_english_folder_name(folder)
        
        markdown_files = list(spanish_folder.rglob("*.md"))
        
        for spanish_file in markdown_files:
            if not should_translate_file(spanish_file):
                continue
            
            relative_path = spanish_file.relative_to(spanish_folder)
            english_file = english_root / english_folder_name / relative_path
            
            if needs_translation(spanish_file, english_file):
                try:
                    translate_file(spanish_file, english_file)
                except:
                    pass

if __name__ == "__main__":
    main()