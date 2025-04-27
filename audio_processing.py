import numpy as np
import librosa

def extract_audio_features(audio_data, sr=22050):
    """
    Extract audio features such as pitch, tone, and speech patterns from audio data.

    Parameters:
    - audio_data: np.ndarray, audio time series
    - sr: int, sample rate

    Returns:
    - features: dict, extracted audio features
    """
    features = {}

    # Extract pitch (fundamental frequency)
    pitches, magnitudes = librosa.piptrack(y=audio_data, sr=sr)
    pitch = pitches[magnitudes > np.median(magnitudes)].mean() if np.any(magnitudes > np.median(magnitudes)) else 0
    features['pitch'] = pitch

    # Extract spectral centroid as a proxy for tone brightness
    spectral_centroid = librosa.feature.spectral_centroid(y=audio_data, sr=sr)
    features['spectral_centroid_mean'] = spectral_centroid.mean()

    # Extract speech rate (approximate)
    onset_env = librosa.onset.onset_strength(y=audio_data, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    features['tempo'] = tempo[0]

    return features
