import bpy
import os
import argparse
import sys

# Usage:
# blender -b -P stl2obj.py -- -f frame.STL
# blender -b -P stl2obj.py -- -d .

def convert_stl(mesh_file):
    if mesh_file.endswith('.STL') or mesh_file.endswith('.stl'):
        ext = os.path.splitext(mesh_file)[1]
        obj_file = mesh_file.replace(ext, '.obj')

        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()

        bpy.ops.import_mesh.stl(filepath=mesh_file)

        bpy.ops.object.select_all(action='SELECT')

        bpy.ops.export_scene.obj(filepath=obj_file)

argv = sys.argv
argv = argv[argv.index("--") + 1:]
parser = argparse.ArgumentParser()
parser.description = "Script to convert stl meshes to object mesh format"
parser.prog = "slt2obj"
group = parser.add_mutually_exclusive_group()
group.add_argument('-f', dest='file_path', help='File path to mesh file.')
group.add_argument('-d', dest='dir_path', help='Directory path containing mesh files')
arguments = parser.parse_args(argv)


if arguments.file_path:
    print(arguments.file_path)
    convert_stl(arguments.file_path)
elif arguments.dir_path:
    for root, dirs, files in os.walk(arguments.dir_path):
        for f in files:
            mesh_file = os.path.join(arguments.dir_path, f)
            convert_stl(mesh_file)
