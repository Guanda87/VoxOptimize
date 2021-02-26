# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "VoxOptimize ",
    "author" : "Guanda",
    "description" : "optimize MagicaVoxel models",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 2),
    "location" : "View 3D > Sidebar > VoxOptimize",
    "warning" : "",
    "category" : "Mesh"
}

import bpy
 
class VO_OT_Operator(bpy.types.Operator) :
    bl_idname = "view3d.vox_optimize"
    bl_label = "Vox Optimize"
    bl_description = "Optimize MagicaVoxel Models"


    def execute(self, context):
        if bpy.context.selected_objects != []:
            for obj in bpy.context.selected_objects:
                if obj.type == 'MESH':
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.remove_doubles()
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.object.shade_flat()
        return {'FINISHED'} 

class VO_PT_Panel(bpy.types.Panel):
    bl_idname = "VO_PT_Panel"
    bl_label = "Vox Optimize Panel"
    bl_category = "Vox Optimize"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view3d.vox_optimize', text="Optimize")

def register():
    bpy.utils.register_class(VO_OT_Operator)
    bpy.utils.register_class(VO_PT_Panel)

def unregister():
    bpy.utils.unregister_class(VO_OT_Operator)
    bpy.utils.unregister_class(VO_PT_Panel)

if __name__ == "__main__":
    register()