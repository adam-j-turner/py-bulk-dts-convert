import enzyme
import glob
import sys, os

targetDir = sys.argv[1]

nested = glob.glob(f'{targetDir}/**/*.mkv', recursive=True)
inRoot = glob.glob(f'{targetDir}/*.mkv', recursive=True)

metadata = {}
toBeConverted = []

for filename in (nested + inRoot):
  with open(filename, 'rb') as f:
    meta = enzyme.MKV(f)

    metadata[filename] = meta.audio_tracks

ccuCodecs = ['A_AC3','A_AAC','A_FLAC','A_WAV','A_MP3']
englishTerms = ['english','eng','en']

for path,tracks in metadata.items():
  # if only track is DTS
  if len(tracks) == 1 and tracks[0].codec_id == 'A_DTS':
    toBeConverted.append(path)
  
  # convert if the default track is DTS
  # and there are no other tracks with
  # english defined as the language.
  defaultTrack = next(iter([t for t in tracks if t.default and t.codec_id == 'A_DTS']), None)

  englishNonDefaults = [
    t for t in tracks if t.language is not None and \
      t.language.lower() in englishTerms and \
      t.codec_id in ccuCodecs
  ]
  
  if defaultTrack is not None and len(englishNonDefaults) == 0:
    toBeConverted.append(path)

for filename in toBeConverted:
  os.system(f'{sys.path[0]}/mkvdts2ac3.sh -d "{filename}"')
