import bpy
import json

# List to store the joint data
joint_data = []

# Get all armatures in the scene
armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']

# Iterate through each armature
for armature in armatures:
    # Iterate through each bone in the armature
    for bone in armature.pose.bones:
        # Check if the bone has constraints (joint limits)
        if bone.constraints:
            # Dictionary to store the data for the bone
            bone_data = {
                "name": bone.name,
                "max": {},
                "min": {},
            }

            # Iterate through each constraint of the bone
            for constraint in bone.constraints:
                # Check if the constraint is a rotation constraint'
                if constraint.type == 'LIMIT_ROTATION':
                    # Get the constraint limits
                    bone_data["max"]["rotation"] = [constraint.max_x, constraint.max_y, constraint.max_z]
                    bone_data["min"]["rotation"] = [constraint.min_x, constraint.min_y, constraint.min_z]

            # Add the bone's data to the joint data list
            joint_data.append(bone_data)

# Wrap joint_data in a dictionary under the key "joints"
joint_data = {"joints": joint_data}

# Save the joint data to a JSON file
export_path = "C:/Users/gally/OneDrive/Desktop/nico-limity2.json"
with open(export_path, "w") as file:
    json.dump(joint_data, file, indent=4)