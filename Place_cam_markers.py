import bpy


BPM = 44
FPS = 30
RUN_LENGTH_SECS = 6 * 60 + 30
SUPERCYCLE_LENGTH = 12

CAMERAS = ["Camera 02 closeup", "Camera 01 closeup", "Camera 02 closeup", "Camera 03 flyover", "Camera 01 closeup"]

def beat_nr_to_frame(beat_nr):
    return FPS * 60 / BPM * beat_nr

def beat_nr_to_seconds(beat_nr):
    return 60 / BPM * beat_nr

def duration_secs_to_beats(dur_sec):
    return int(dur_sec * BPM / 60)

def place_cam_marker(beat_nr, cam_name):
    marker_seconds = beat_nr_to_seconds(beat_nr)
    marker_frame = round(beat_nr_to_frame(beat_nr))
    print(f"frame: {marker_frame}, time: {marker_seconds:.2f} secs, cam: {cam_name}")
    marker = bpy.context.scene.timeline_markers.new(cam_name, frame=marker_frame)
    marker.camera = bpy.data.objects[cam_name]

print("Markers BEFORE:")
print("\n".join([f"{str(marker.camera)}" for marker in bpy.context.scene.timeline_markers]))

total_beats = duration_secs_to_beats(RUN_LENGTH_SECS)

print(f"Total beats: {total_beats}")

for supercycle_idx in [supercycle_nr * SUPERCYCLE_LENGTH for supercycle_nr in range(int(total_beats / SUPERCYCLE_LENGTH))]:
    # TODO: Generalize: turn to internal loop, offsets as (n+1)-th powers of 2, for CAMERAS[n] 
    place_cam_marker(supercycle_idx + 2, CAMERAS[0])
    place_cam_marker(supercycle_idx + 4, CAMERAS[1])
    place_cam_marker(supercycle_idx + 6, CAMERAS[2])
    place_cam_marker(supercycle_idx + 8, CAMERAS[3])
    place_cam_marker(supercycle_idx + 12, CAMERAS[4])


print("Markers AFTER:")
print("\n".join([f"{str(marker.camera)}" for marker in bpy.context.scene.timeline_markers]))
