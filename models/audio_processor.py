import librosa as lb
import soundfile as sf
from spleeter.separator import Separator
import os

class AudioProcessor:
    def __init__(self):
        self.separator = Separator('spleeter:5stems')

    @staticmethod
    def analyze_bpm(audio_file):
        """Analyze BPM of the given audio file"""
        try:
            y, sr = lb.load(audio_file)
            onset_env = lb.onset.onset_strength(y=y, sr=sr)
            tempo, _ = lb.beat.beat_track(onset_envelope=onset_env, sr=sr)
            return tempo
        except Exception as e:
            raise Exception(f"Error analyzing BPM: {str(e)}")

    @staticmethod
    def adjust_speed(audio_file, target_bpm):
        """Adjust audio speed to match target BPM"""
        try:
            # Load audio
            y, sr = lb.load(audio_file)
            
            # Get current BPM
            current_bpm = AudioProcessor.analyze_bpm(audio_file)
            
            # Calculate speed factor
            speed_factor = target_bpm / current_bpm
            
            # Time stretch
            y_adjusted = lb.effects.time_stretch(y, rate=speed_factor)
            
            # Generate output filename
            base_path = os.path.splitext(audio_file)[0]
            output_path = f"{base_path}_adjusted.wav"
            
            # Save processed audio
            sf.write(output_path, y_adjusted, sr)
            return output_path
        except Exception as e:
            raise Exception(f"Error adjusting speed: {str(e)}")

    def separate_stems(self, audio_file, output_path=None):
        """Separate audio into stems using Spleeter"""
        try:
            if output_path is None:
                output_path = os.path.join(os.path.dirname(audio_file), "separated")
            
            # Create output directory if it doesn't exist
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            
            # Perform separation
            self.separator.separate_to_file(
                audio_file,
                output_path,
                codec='wav'
            )
            return output_path
        except Exception as e:
            raise Exception(f"Error separating stems: {str(e)}")
