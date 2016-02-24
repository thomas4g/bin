from subprocess import Popen, PIPE

class Py3status:
    def pianobar_status(self, i3s_output_list, i3s_config):
        title, title_err = Popen(['bash', 'bin/get_song_title'], stdout=PIPE, stderr=PIPE).communicate()
        time, time_err = Popen(['bash', 'bin/get_song_time'], stdout=PIPE, stderr=PIPE).communicate()
        title = title.split('\n', 1)[0].split('>', 1)[1].split('" on "', 1)[0].strip() + '"'
        time = time.replace('\n', '')
        return {
            'full_text': time + ' | ' + title,
            'cached_until': 0
        }
