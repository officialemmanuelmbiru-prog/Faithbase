"""
Faithbase Engine - Version 0.1.0
Release Name: Genesis
Compatible: Blender 4.5+

Collection Management Module
"""
import bpy
from Engine.Core import FB_Settings

def get_or_create_collection(collection_key: str):
    """
    Retrieves or generates a master collection using project prefix conventions.
    Usage: get_or_create_collection("ENVIRONMENT")
    """
    raw_name = FB_Settings.COLLECTIONS.get(collection_key, collection_key)
    full_name = f"{FB_Settings.GLOBAL_PREFIX}{raw_name}"
    
    if full_name in bpy.data.collections:
        return bpy.data.collections[full_name]
    
    new_col = bpy.data.collections.new(full_name)
    bpy.context.scene.collection.children.link(new_col)
    print(f"[{FB_Settings.PROJECT_NAME}] Created collection wrapper: {full_name}")
    return new_col

def link_object_to_collection(obj, collection_key: str):
    """Safely links an object to a specific collection and unlinks it from default collections."""
    if not obj:
        return
        
    target_col = get_or_create_collection(collection_key)
    
    if obj.name not in target_col.objects:
        target_col.objects.link(obj)
        
    for col in list(obj.users_collection):
        if col != target_col:
            col.objects.unlink(obj)