# Smart Bone Reconnect - blender Addon

This addon is used to fix bone position and orientation in armatures of rigged models imported from other engines (such as the Source game engine)

## Examples
Models imported from the Source engine often have Armatures with short and disoriented bones that look like this:

![Alt text](/example-images/image-01.png)

After selecting the bones and appying the addon, their position will become fixed as such:

![Alt text](/example-images/image-03.png)

## How it works
Selected bones, which have a single child, will move their tails to the child head

Bones which have multiple children (such as a wrist bone with multiple fingers) will move it's tail to the averaged position of all children's heads

Bones which are end points (have no children) will move their tail in the same orientation as their parent bone and become the same length

## How to install
 - Download the included **SmartBoneReconnect.py** file
 - In blender, go to **Edit > Preferences > Add-ons**
 - Click the **Install** button and select the **SmartBoneReconnect.py** file
 - Enable the addon with the checkmark

## How to use
- Once installed, the option will appear under the **Armature menu** in 3D View when in Armature Edit mode
- Simply select all the bones you want to fix in Edit mode and click **Armature > Smart Bone Disssolve**

![Alt text](/example-images/image-02.png)
