"""
Faithbase Engine - Version 0.1.0
Release Name: Genesis
Compatible: Blender 4.5+

Mathematical Noise & Procedural Map Functions
"""
import mathutils

def sample_perlin_noise_2d(x: float, y: float, scale=50.0, octaves=4, lacunarity=2.0, gain=0.5):
    """
    Generates fractional multi-fractal noise values mapped inside a clean [0.0, 1.0] workspace range.
    """
    if scale <= 0.0:
        scale = 0.01
        
    total = 0.0
    frequency = 1.0 / scale
    amplitude = 1.0
    max_amplitude = 0.0
    
    for _ in range(octaves):
        sample_x = x * frequency
        sample_y = y * frequency
        
        # Pull standard signed mathematical coordinate values [-1.0, 1.0]
        noise_val = mathutils.noise.noise(mathutils.Vector((sample_x, sample_y, 0.0)))
        
        total += noise_val * amplitude
        max_amplitude += amplitude
        
        frequency *= lacunarity
        amplitude *= gain
        
    return (total / max_amplitude + 1.0) * 0.5