from pylab import *
from IPython.display import Audio  # awesome IPython tool to embed audio directly in the notebook
from scipy.signal import square

t = arange(0, 0.1, 1 / 10000.)
t.shape
plot(t, square(2 * pi * 100 * t))
title("A square wave!")
ylim(-1.1, 1.1)
grid(True)
Audio(data=square(2 * pi * 100 * t), rate=5000)


def play_melody(melody, sample_freq=10.e3, bpm=50):
	duration = re.compile("^[0-9]+")
	pitch = re.compile("[\D]+[\d]*")
	measure_duration = 4 * 60. / bpm  #usually it's 4/4 measures
	output = zeros((0, ))
	for note in melody.split(','):
		# regexp matching
		duration_match = duration.findall(note)
		pitch_match = pitch.findall(note)

		# duration
		if len(duration_match) == 0:
			t_max = 1 / 4.
		else:
			t_max = 1 / float(duration_match[0])
		if "." in pitch_match[0]:
			t_max *= 1.5
			pitch_match[0] = "".join(pitch_match[0].split("."))
		t_max = t_max * measure_duration

		# pitch
		if pitch_match[0] == 'p':
			freq = 0
		else:
			if pitch_match[0][-1] in ["4", "5", "6", "7"]:  # octave is known
				octave = ["4", "5", "6", "7"].index(pitch_match[0][-1]) + 4
				height = pitch_match[0][:-1]
			else:  # octave is not known
				octave = 5
				height = pitch_match[0]
			freq = 261.626 * 2**(
			 (["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"
			   ].index(height) / 12. + octave - 4))

		# generate sound
		t = arange(0, t_max, 1 / sample_freq)
		wave = square(2 * pi * freq * t)

		# append to output
		output = hstack((output, wave))

	display(Audio(output, rate=sample_freq))
