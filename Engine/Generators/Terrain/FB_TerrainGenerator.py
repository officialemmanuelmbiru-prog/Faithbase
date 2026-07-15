"""
FB_TerrainGenerator.py
Version: 0.1.0

Faithbase - Garden of Invitation
Blender 4.5+
"""

import bpy

# ===== Adjustable Parameters =====
TERRAIN_SIZE = 150.0
SUBDIVISIONS = 200

def ensure_collection(name):
    if name in bpy.data.collections:
        return bpy.data.collections[name]
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col

def clear_object(name):
    obj = bpy.data.objects.get(name)
    if obj:
        bpy.data.objects.remove(obj, do_unlink=True)

def create_terrain():
    clear_object("FB_Terrain")

    bpy.ops.mesh.primitive_grid_add(
        x_subdivisions=SUBDIVISIONS,
        y_subdivisions=SUBDIVISIONS,
        size=TERRAIN_SIZE/2,
        location=(0,0,0)
    )

    obj = bpy.context.active_object
    obj.name = "FB_Terrain"

    disp = obj.modifiers.new("TerrainNoise", 'DISPLACE')
    tex = bpy.data.textures.new("FB_TerrainNoise", 'CLOUDS')
    tex.noise_scale = 18.0
    disp.texture = tex
    disp.strength = 2.5

    sub = obj.modifiers.new("Subdivision", 'SUBSURF')
    sub.levels = 1
    sub.render_levels = 2

    mat = bpy.data.materials.get("FB_Ground")
    if mat is None:
        mat = bpy.data.materials.new("FB_Ground")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs["Base Color"].default_value = (0.23,0.35,0.18,1)
        bsdf.inputs["Roughness"].default_value = 0.95
    if not obj.data.materials:
        obj.data.materials.append(mat)

    col = ensure_collection("FB_Environment")
    if obj.name not in col.objects:
        for c in obj.users_collection:
            c.objects.unlink(obj)
        col.objects.link(obj)

if __name__ == "__main__":
    create_terrain()
    print("Faithbase Terrain Generated")
