bl_info = {
    "name": "Smart Bone Reconnect",
    "author": "maxisan137",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > Armature",
    "description": "Re-positions selected bones tails in an armature with their children",
    "warning": "",
    "wiki_url": "",
    "category": "Armature"
}

import bpy
from bpy.types import (
    Operator,
)

##################################################
# SMART BONE RECONNECT BY MAXISAN137
#################################################
# This addon is designed to be used with models imported from decompiled Source Engine files
# It fixes the bone orientation and tail positions
#
# Once installed, the option will appear inder Armature menu in 3D View when in Armature Edit mode
# To use, select the bones that need fixing in edit mode and apply the addon
##################################################


class ARMATURE_OT_smart_bones_reconnect(Operator):
    bl_idname = "armature.smart_bones_reconnect"
    bl_label = "Smart Bones Reconnect"
    bl_description = "Re-positions selected bones tails in an armature with their children"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        arm = bpy.context.active_object
        
        # Checking if the active object is an armature:
        if arm.type != "ARMATURE":
            print("Active object is not an Armature type")
            return {'FINISHED'}
        
        for bone in [b for b in arm.data.edit_bones if b.select == True]:
            
            # If a bone only has one child, move it's tail to the child's head:
            if len(bone.children) == 1:
                bone.tail.xyz = bone.children[0].head.xyz
                
            # If a bone has multiple children, move it's tail to the average position of the children's heads:
            elif len(bone.children) > 1:
                
                # Deselect all bones and joints in the armature:
                for b in arm.data.edit_bones:
                    b.select = False
                    b.select_tail = False
                    b.select_head = False
                    
                # Select children's heads:
                for b in bone.children:
                    b.select_head = True
                # Snap 3D cursor:
                bpy.ops.view3d.snap_cursor_to_selected()
                # Deselect children's heads:
                for b in bone.children:
                    b.select_head = False
                # Select bone tail:
                bone.select_tail = True
                # Snap it to 3D cursor:
                bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
                # Reset 3D cursor and deselect bone tail:
                bpy.ops.view3d.snap_cursor_to_center()
                bone.select_tail = False
            
            # Finally, if the bone has no children and is an only child, it's orientation and length will be adjusted to that of the parent
            elif len(bone.children) == 0 and len(bone.parent.children) == 1:
                bone.tail.xyz = bone.head.xyz + (bone.parent.tail.xyz - bone.parent.head.xyz)
                bone.length = bone.parent.length
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(ARMATURE_OT_smart_bones_reconnect.bl_idname)

def register():
    bpy.utils.register_class(ARMATURE_OT_smart_bones_reconnect)
    bpy.types.VIEW3D_MT_edit_armature.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ARMATURE_OT_smart_bones_reconnect)
    bpy.types.VIEW3D_MT_edit_armature.remove(menu_func)


if __name__ == "__main__":
    register()
