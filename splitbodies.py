bl_info = {
    "name": "Separate Objects",
    "category": "Mesh",
    "author": "ntoff",
    "version": (0,0,1),
    "location": "Search popup",
    "description": "Splits a packed 3d printer plate into individual bodies and exports to the current scene output path.",
    "wiki_url": "https://github.com/ntoff/blender_split_bodies",
    "tracker_url": "https://github.com/ntoff/blender_split_bodies",                
}

import bpy

class ObjectSplitBodies(bpy.types.Operator):
    """Split Object Into Separate Bodies"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.split_bodies"        # unique identifier for buttons and menu items to reference.
    bl_label = "Split Bodies"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    def execute(self, context):        # execute() is called by blender when running the operator.
        
    
        scene = context.scene
        exportFolder = scene.render.filepath
        objects = bpy.data.objects
        bpy.ops.mesh.separate(type='LOOSE')
        for object in objects:
            bpy.ops.object.select_all(action='DESELECT')
            object.select = True
            exportName = exportFolder + object.name + '.stl'
            
            bpy.ops.export_mesh.stl(filepath=exportName, use_selection=True)
        
        return {'FINISHED'}            

def register():
    print("Registering Body Splitter")
    bpy.utils.register_class(ObjectSplitBodies)

def unregister():
    bpy.utils.unregister_class(ObjectSplitBodies)
    
 