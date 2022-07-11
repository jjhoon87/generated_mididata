import mido

def read_midi_file(midi_file_path, ticks_per_beat=960):
    # print('midi_file_path', midi_file_path)
    mid = mido.MidiFile(midi_file_path, ticks_per_beat=ticks_per_beat)
    note_temp = []
    note_import = []
    tick = 0
    for i, track in enumerate(mid.tracks):
        for msg in track:
            tick += msg.time
            if msg.type == 'note_on' or msg.type == 'note_off':
                if msg.type == 'note_on':
                    pitch = msg.note
                    start = tick / float(mid.ticks_per_beat)
#                     start = float("{:.4f}".format(start))  # 시간 퀀타이즈
                    velocity = msg.velocity
                    note_info = {
                        'pitch': pitch,
                        'start_time': start,
                        'length': None,
                        'velocity': velocity,
#                         'function': None,
                    }
                    note_temp.append(note_info)
                elif msg.type == 'note_off':
                    for j in range(len(note_temp)):
                        if note_temp[j]['pitch'] == msg.note:
                            end = tick / float(mid.ticks_per_beat)
                            note_temp[j]['length'] = end - note_temp[j]['start_time']
                            note_import.append(note_temp[j])
                            del note_temp[j]
                            break
            else:
                pass
                # print(msg)

    note_import = sorted(note_import, key=lambda k: k['start_time'])
    return note_import
