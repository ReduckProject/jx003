from pydub import AudioSegment


def convert_to_8bit(input_file, output_file):
    AudioSegment.converter = "C:\\bin\\ffmpeg.exe"
    AudioSegment.ffmpeg = "C:\\bin\\ffmpeg.exe"
    AudioSegment.ffprobe = "C:\\bin\\ffprobe.exe"
    # Load MP3 file
    audio = AudioSegment.from_mp3(input_file)

    # Convert to 8-bit
    audio = audio.set_sample_width(1)  # Set sample width to 8 bits

    # Export as WAV (you can change the output format if needed)
    audio.export(output_file, format="wav")

# Example usage
input_mp3_file = "E:\\Code\\GitHub\\reduck-music\\target\\classes\\music\\音频怪物 - 朝闻道.mp3"
output_8bit_file = "output_8bit.wav"

convert_to_8bit(input_mp3_file, output_8bit_file)