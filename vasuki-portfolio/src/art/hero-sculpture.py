"""Render the portfolio's original geometric still with Blender in background mode.

blender -b -P hero-sculpture.py -- /path/to/output.png [width] [samples]
"""

import math
import os
import sys

import bpy
from mathutils import Vector


arguments = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
if not arguments:
    raise SystemExit("Pass an output PNG path after --")

output_path = os.path.abspath(arguments[0])
width = int(arguments[1]) if len(arguments) > 1 else 1440
samples = int(arguments[2]) if len(arguments) > 2 else 72

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.samples = samples
scene.cycles.use_denoising = True
scene.cycles.device = "CPU"
scene.cycles.max_bounces = 6
scene.cycles.diffuse_bounces = 3
scene.cycles.glossy_bounces = 3
scene.render.film_transparent = True
scene.render.resolution_x = width
scene.render.resolution_y = round(width * 700 / 820)
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"
scene.render.image_settings.color_depth = "8"
scene.render.filepath = output_path
scene.view_settings.view_transform = "AgX"
scene.view_settings.look = "AgX - Medium High Contrast"


def linear_rgb(value):
    """Turn a published sRGB hex swatch into scene-linear RGB."""
    rgb = [int(value[index:index + 2], 16) / 255 for index in (0, 2, 4)]
    return tuple(
        channel / 12.92 if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
        for channel in rgb
    )


def finish(name, color, roughness=0.49, metal=0.0, micro=0.035):
    material = bpy.data.materials.new(name)
    material.diffuse_color = (*linear_rgb(color), 1.0)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    surface = nodes.get("Principled BSDF")
    surface.inputs["Base Color"].default_value = material.diffuse_color
    surface.inputs["Roughness"].default_value = roughness
    surface.inputs["Metallic"].default_value = metal
    if micro:
        coords = nodes.new("ShaderNodeTexCoord")
        grain = nodes.new("ShaderNodeTexNoise")
        grain.inputs["Scale"].default_value = 182
        grain.inputs["Detail"].default_value = 2.2
        grain.inputs["Roughness"].default_value = 0.7
        links.new(coords.outputs["Object"], grain.inputs["Vector"])
        bump = nodes.new("ShaderNodeBump")
        bump.inputs["Strength"].default_value = micro
        bump.inputs["Distance"].default_value = 0.0025
        links.new(grain.outputs["Fac"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], surface.inputs["Normal"])
    return material


coral = finish("Satin coral ceramic", "FF7F69", 0.42, 0.025)
apricot = finish("Soft illuminated terracotta", "F47864", 0.4)
blush = finish("Blush cast resin", "F1B7B5", 0.40, 0.025)
rose = finish("Muted coral clay", "D78883", 0.51)
stone = finish("Graphite stone", "363539", 0.62)
slate = finish("Black slate", "252529", 0.62)
pencil = finish("Satin graphite", "414046", 0.49, 0.055)
honed = finish("Honed graphite facet", "514D52", 0.54)
ring_enamel = finish("Coral enamel", "FF846B", 0.28, 0.22, 0)

geometry = []


def bevel(obj, radius=0.018):
    """A short rounded edge catches the studio lights without softening the form."""
    if not radius:
        return
    edge = obj.modifiers.new("Machined edge", "BEVEL")
    edge.width = radius
    edge.segments = 3
    edge.limit_method = "ANGLE"
    normals = obj.modifiers.new("Planar face normals", "WEIGHTED_NORMAL")
    normals.keep_sharp = True


def block(name, x0, x1, y0, y1, z0, z1, material, radius=0.018):
    bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2),
    )
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = (x1 - x0, y1 - y0, z1 - z0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    bevel(obj, radius)
    geometry.append(obj)
    return obj


def extrusion(name, points, near, far, material=None, radius=0.0):
    """Extrude a counterclockwise X,Z profile along Y."""
    count = len(points)
    verts = [(x, y, z) for y in (near, far) for x, z in points]
    faces = [tuple(range(count)), tuple(reversed(range(count, count * 2)))]
    for index in range(count):
        after = (index + 1) % count
        faces.append((index, index + count, after + count, after))
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    scene.collection.objects.link(obj)
    if material:
        mesh.materials.append(material)
        geometry.append(obj)
    bevel(obj, radius)
    return obj


def sphere(name, center, radius, material):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=72, ring_count=40, radius=radius, location=center,
    )
    obj = bpy.context.object
    obj.name = name
    for polygon in obj.data.polygons:
        polygon.use_smooth = True
    obj.data.materials.append(material)
    geometry.append(obj)
    return obj


def ring(name, center, radius, section):
    bpy.ops.mesh.primitive_torus_add(
        major_segments=144,
        minor_segments=12,
        location=center,
        rotation=(math.pi / 2, 0, 0),
        major_radius=radius,
        minor_radius=section,
    )
    obj = bpy.context.object
    obj.name = name
    for polygon in obj.data.polygons:
        polygon.use_smooth = True
    obj.data.materials.append(ring_enamel)
    geometry.append(obj)


# A continuous base, three intersecting towers, and a low western terrace.
block("Continuous graphite footing", -3.14, 3.88, -0.63, 1.42, -0.68, -0.10, slate)
extrusion(
    "Sloping western plinth",
    [(-4.12, -0.68), (-0.61, -0.68), (-0.61, 0.27), (-3.14, 0.27)],
    -0.71, 1.57, pencil, 0.016,
)
block("Graphite resonance monolith", -0.70, 1.95, -0.48, 1.49, -0.09, 3.08, stone)
extrusion(
    "Honed triangular graphite face",
    [(-0.68, -0.06), (1.93, 3.06), (-0.68, 3.06)],
    -0.487, -0.478, honed,
)
block("East graphite tower", 1.90, 3.73, -0.18, 1.56, -0.11, 3.12, slate)

# The crown is pierced all the way through. Its aperture, sidewalls, and
# internal shadow come directly from the geometry and studio illumination.
crown = block("Pierced coral crown", -0.75, 1.96, -0.75, 1.57, 3.08, 5.72, coral, 0)
triangle = extrusion(
    "Aperture cutter",
    [(-0.18, 3.60), (1.40, 3.60), (1.40, 5.10)],
    -0.88, 1.94,
)
cut = crown.modifiers.new("Triangular opening", "BOOLEAN")
cut.operation = "DIFFERENCE"
cut.solver = "EXACT"
cut.object = triangle
bpy.context.view_layer.objects.active = crown
bpy.ops.object.modifier_apply(modifier=cut.name)
bpy.data.objects.remove(triangle, do_unlink=True)
bevel(crown, 0.024)

# A split cast block gives the lower-left accent its diagonal seam.
extrusion(
    "Lower terrace blush prism",
    [(-2.50, 0.27), (-0.75, 0.27), (-2.50, 2.01)],
    -0.63, 1.17, blush, 0.010,
)
extrusion(
    "Lower terrace coral prism",
    [(-0.75, 0.27), (-0.75, 2.01), (-2.50, 2.01)],
    -0.63, 1.17, coral, 0.010,
)

# Two offset fins establish a secondary skyline beside the carved opening.
block("Blush east fin", 2.03, 2.80, 0.13, 1.53, 3.12, 4.00, blush)
block("Coral east fin", 2.80, 3.63, 0.13, 1.53, 3.12, 4.83, apricot)

# Four fine enamel rings are physically laid onto the main front plane.
for index, radius in enumerate((0.32, 0.52, 0.74, 0.97)):
    ring(f"Concentric enamel inlay {index + 1}", (0.57, -0.497, 1.82), radius, 0.012)
sphere("Blush ceramic center", (0.57, -0.510, 1.82), 0.147, blush)

# Ascending foreground steps carry a deliberate progression of sphere sizes.
block("First foreground step", 0.53, 1.69, -1.91, -0.43, -0.69, 0.16, pencil)
block("Second foreground step", 1.69, 2.83, -1.62, -0.15, -0.69, 0.72, stone)
block("Third foreground step", 2.83, 3.94, -1.33, -0.04, -0.69, 1.30, pencil)
sphere("Small rose sphere", (1.06, -1.22, 0.295), 0.135, rose)
sphere("Middle blush sphere", (2.22, -0.99, 0.925), 0.205, blush)
sphere("Large coral sphere", (3.38, -0.75, 1.60), 0.300, apricot)
sphere("Suspended coral sphere", (-2.05, 0.12, 3.42), 0.223, coral)


def area_light(name, position, aim, energy, size, color):
    light = bpy.data.lights.new(name, "AREA")
    light.energy = energy
    light.shape = "DISK"
    light.size = size
    light.color = tuple(color)
    obj = bpy.data.objects.new(name, light)
    scene.collection.objects.link(obj)
    obj.location = position
    obj.rotation_euler = (Vector(aim) - obj.location).to_track_quat("-Z", "Y").to_euler()


world = bpy.data.worlds.new("Neutral light tent")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.67, 0.66, 0.68, 1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.15
scene.world = world
area_light("Directional window", (3.1, -5.6, 7.8), (0.2, 0.0, 2.5), 1160, 2.5, (1.0, 0.91, 0.86))
area_light("Cool left bounce", (-7.2, -2.7, 5.1), (0.0, 0.0, 2.0), 255, 6.0, (0.83, 0.86, 1.0))
area_light("Soft skylight", (-1.3, 3.4, 10.7), (0.1, 0.0, 2.3), 1160, 4.4, (1.0, 0.86, 0.80))

camera_data = bpy.data.cameras.new("Orthographic architectural camera")
camera_data.type = "ORTHO"
camera = bpy.data.objects.new("Camera", camera_data)
scene.collection.objects.link(camera)
scene.camera = camera
direction = Vector((-0.36, -1.0, 0.275)).normalized()
camera.rotation_euler = (-direction).to_track_quat("-Z", "Y").to_euler()
bpy.context.view_layer.update()
orientation = camera.rotation_euler.to_matrix()
right = orientation @ Vector((1, 0, 0))
up = orientation @ Vector((0, 1, 0))

# Frame the evaluated silhouette with transparent breathing room on all sides.
projected = []
for obj in geometry:
    for vertex in obj.bound_box:
        point = obj.matrix_world @ Vector(vertex)
        projected.append((right.dot(point), up.dot(point)))
left = min(x for x, _ in projected)
right_edge = max(x for x, _ in projected)
bottom = min(y for _, y in projected)
top = max(y for _, y in projected)
aspect = scene.render.resolution_x / scene.render.resolution_y
camera_data.ortho_scale = max(right_edge - left, (top - bottom) * aspect) * 1.035
focus = right * ((left + right_edge) / 2) + up * ((bottom + top) / 2)
camera.location = focus + direction * 22

os.makedirs(os.path.dirname(output_path), exist_ok=True)
bpy.ops.render.render(write_still=True)
