import math
import torch

class AudioToFrameCount:
    """
    Converts audio duration to a frame count.
    - Strict mode: seconds * 16 + 1
    - Integer mode: ceil(seconds) * 16 + 1
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                "mode": (["strict", "integer"],),
            },
        }

    RETURN_TYPES = ("INT", "FLOAT",)
    RETURN_NAMES = ("frame_count", "duration_seconds",)
    FUNCTION = "compute_frames"
    CATEGORY = "audio"

    def compute_frames(self, audio, mode):
        # ComfyUI AUDIO format: dict with "waveform" (B, C, S) tensor and "sample_rate" int
        waveform = audio["waveform"]
        sample_rate = audio["sample_rate"]

        num_samples = waveform.shape[-1]
        duration_seconds = num_samples / sample_rate

        if mode == "strict":
            frame_count = int(duration_seconds * 16 + 1)
        else:  # integer
            frame_count = int(math.ceil(duration_seconds) * 16 + 1)

        return (frame_count, duration_seconds,)


NODE_CLASS_MAPPINGS = {
    "AudioToFrameCount": AudioToFrameCount,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AudioToFrameCount": "Audio to Frame Count",
}
