"""
Faithbase Engine - Version 0.1.0
Release Name: Genesis
Compatible: Blender 4.5+

Core Scene & Object Utilities
"""
import bpy
import mathutils
from Engine.Core import FB_Settings

def safe_delete_object(obj_name: str):
    """Removes an object completely from scene memory to avoid name increment pollution (.001)."""
    if obj_name in bpy.data.objects:
        obj = bpy.data.objects[obj_name]
        bpy.data.objects.remove(obj, do_unlink=True)
        print(f"[{FB_Settings.PROJECT_NAME}] Safely purged object: {obj_name}")

def apply_all_modifiers(obj):
    """Locks in procedural modifiers to evaluate or optimize raw polygon mesh states."""
    if not obj:
        return
    bpy.context.view_layer.objects.active = obj
    for mod in list(obj.modifiers):
        try:
            bpy.ops.object.modifier_apply(modifier=mod.name)
        except Exception as e:
            print(f"[{FB_Settings.PROJECT_NAME} Warning] Could not apply modifier {mod.name}: {e}")

def set_object_origin_to_base(obj):
    """Snaps the object transform origin points flush to its lowest Z boundary point (crucial for scattering)."""
    if not obj or obj.type != 'MESH':
        return
        
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bound_box = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
    lowest_z = min(v.z for v in bound_box)
    
    old_cursor_loc = bpy.context.scene.cursor.location.copy()
    bpy.context.scene.cursor.location = (obj.location.x, obj.location.y, lowest_z)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.cursor.location = old_cursor_loc