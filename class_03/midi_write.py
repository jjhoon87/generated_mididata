import midiutil
def write_midi(seq, bpm, path):
    mf = midiutil.MIDIFile(1, file_format=1)
    track = 0
    channel = 0
    mf.addTempo(track, 0, bpm)
    for i, n in enumerate(seq):
        mf.addNote(
            track,
            channel,
            n['pitch'],
            n['start_time'],
            n['length'],
            n['velocity']
        )
    with open(path, 'wb') as outf:
        mf.writeFile(outf)
