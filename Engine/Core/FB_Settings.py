"""
Faithbase Engine - Version 0.1.0
Release Name: Genesis
Compatible: Blender 4.5+

Central Configuration Module
"""
import os
import json

# Project Metadata
ENGINE_VERSION = "0.1.0"
PROJECT_NAME = "Faithbase"
GLOBAL_PREFIX = "FB_"

# Unit Scale Definitions (1.0 Blender Unit = 1.0 Meter)
UNIT_SCALE = 1.0

# Performance & Viewport Constraints
MAX_VERT_COUNT = 1000000
RENDER_ENGINE = 'CYCLES'  # Default production renderer

# Collection Names (Without Prefix)
COLLECTIONS = {
    "ENVIRONMENT": "Environment",
    "VEGETATION": "Vegetation",
    "WATER": "Water",
    "STRUCTURES": "Structures",
    "LIGHTING": "Lighting"
}

# Default Biome Parameters (Fallback if config JSON missing)
DEFAULT_CONFIG = {
    "terrain_size": 150.0,
    "subdivisions": 6,
    "hill_intensity": 0.35,
    "seed": 42
}

def load_biome_config(config_path=""):
    """Loads a configuration JSON file from the Engine/Config directory."""
    if not config_path or not os.path.exists(config_path):
        return DEFAULT_CONFIG
    
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"[{PROJECT_NAME} Warning] Failed to load config: {e}. Using defaults.")
        return DEFAULT_CONFIG