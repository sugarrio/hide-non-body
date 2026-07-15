bl_info = {
    "name": "Hide Selected Non-Body Objects",
    "author": "riozaburou",
    "version": (3, 1, 0),
    "blender": (2, 79, 0),
    "location": "3D View > Tools (2.79) / Sidebar > Hide Tools (2.80+)",
    "description": "Hide selected objects whose names do not contain 'body'",
    "category": "Object",
}

import bpy

IS_280_OR_NEWER = bpy.app.version >= (2, 80, 0)


def set_hidden(obj, hidden=True):
    if IS_280_OR_NEWER:
        obj.hide_set(hidden)
    else:
        obj.hide = hidden


class OBJECT_OT_hide_selected_non_body(bpy.types.Operator):
    bl_idname = "object.hide_selected_non_body"
    bl_label = "body以外を非表示"
    bl_description = "選択中のオブジェクトのうち、名前にbodyを含まないものを非表示にします"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'

    def execute(self, context):
        selected = list(context.selected_objects)

        if not selected:
            self.report({'WARNING'}, "オブジェクトが選択されていません")
            return {'CANCELLED'}

        hidden_count = 0
        kept_count = 0

        for obj in selected:
            if "body" in obj.name.lower():
                kept_count += 1
            else:
                set_hidden(obj, True)
                hidden_count += 1

        self.report(
            {'INFO'},
            "{}個を非表示、bodyを含む{}個を維持しました".format(
                hidden_count, kept_count
            )
        )
        return {'FINISHED'}


class VIEW3D_PT_hide_non_body_279(bpy.types.Panel):
    bl_label = "Hide Non Body"
    bl_idname = "VIEW3D_PT_hide_non_body_279"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'

    def draw(self, context):
        self.layout.operator(
            OBJECT_OT_hide_selected_non_body.bl_idname,
            text="body以外を非表示"
        )


class VIEW3D_PT_hide_non_body_280(bpy.types.Panel):
    bl_label = "Hide Non Body"
    bl_idname = "VIEW3D_PT_hide_non_body_280"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Hide Tools"

    def draw(self, context):
        self.layout.operator(
            OBJECT_OT_hide_selected_non_body.bl_idname,
            text="body以外を非表示"
        )


def _classes():
    if IS_280_OR_NEWER:
        return (
            OBJECT_OT_hide_selected_non_body,
            VIEW3D_PT_hide_non_body_280,
        )
    return (
        OBJECT_OT_hide_selected_non_body,
        VIEW3D_PT_hide_non_body_279,
    )


def register():
    for cls in _classes():
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(_classes()):
        bpy.utils.unregister_class(cls)
