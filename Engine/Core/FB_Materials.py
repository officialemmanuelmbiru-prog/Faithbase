"""
Faithbase Engine - Version 0.1.0
Release Name: Genesis
Compatible: Blender 4.5+

Centralized Node Material Factory
"""
import bpy
from Engine.Core import FB_Settings

def get_or_create_pbr_material(mat_name: str, base_color=(0.1, 0.1, 0.1, 1.0), roughness=0.5):
    """Generates generic principled PBR material pipelines with full node enablement."""
    full_name = f"{FB_Settings.GLOBAL_PREFIX}{mat_name}"
    
    if full_name in bpy.data.materials:
        return bpy.data.materials[full_name]
        
    mat = bpy.data.materials.new(name=full_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    
    nodes.clear()
    
    node_output = nodes.new(type='ShaderNodeOutputMaterial')
    node_principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    
    # Modern BSDF property updates for Blender 4.x+
    node_principled.inputs['Base Color'].default_value = base_color
    node_principled.inputs['Roughness'].default_value = roughness
    
    links = mat.node_tree.links
    links.new(node_principled.outputs['BSDF'], node_output.inputs['Surface'])
    
    return mat