import bpy
import os
import argparse
import sys

# Usage:
# blender -b -P wrl2stl.py -- -f frame.wrl
# blender -b -P wrl2stl.py -- -d .


def convert_file(file_path):
    if file_path.endswith('.WRL') or file_path.endswith('.wrl'):
        ext = os.path.splitext(file_path)[1]
        obj_file = file_path.replace(ext, '.stl')

        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()

        bpy.ops.import_scene.x3d(filepath=file_path)

        bpy.ops.object.select_all(action='SELECT')

        bpy.ops.export_mesh.stl(filepath=obj_file)

argv = sys.argv
argv = argv[argv.index("--") + 1:]
parser = argparse.ArgumentParser()
parser.description = "Script to convert stl meshes to object mesh format"
parser.prog = "wrl2stl"
group = parser.add_mutually_exclusive_group()
group.add_argument('-f', dest='file_path', help='File path to mesh file.')
group.add_argument('-d', dest='dir_path', help='Directory path containing mesh files')
arguments = parser.parse_args(argv)


if arguments.file_path:
    print(arguments.file_path)
    convert_file(arguments.file_path)
elif arguments.dir_path:
    for root, dirs, files in os.walk(arguments.dir_path):
        for f in files:
            mesh_file = os.path.join(arguments.dir_path, f)
            convert_file(mesh_file)
