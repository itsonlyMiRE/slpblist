import glob, time, os, winsound

bl_file = __file__.replace('py','txt')
sound_file = os.path.dirname(os.path.realpath(__file__)) + '\sound.wav'
slp_dir = ''
with open(bl_file, 'r') as bl_stream:
    slp_dir = bl_stream.readline().replace('\n','')
if slp_dir[-1] != '\\':
    slp_dir = slp_dir + '\\'
if not os.path.isdir(slp_dir):
    exit(f'* provided .slp directory {slp_dir} is invalid, try again\n')
try:
    print('\n* press ctrl+c to exit ...')
    while True:
        on_start = glob.glob(slp_dir+'*.slp')
        while True:
            now = glob.glob(slp_dir+'*.slp')
            diff = list(set(now) - set(on_start))
            if diff != []:
                curr_game = diff[0]
                break
            time.sleep(.5)
        with open(bl_file, 'r') as bl_stream:
            bl = bl_stream.read().splitlines()
        for code in bl:
            code = code.replace('\n','')
        with open(curr_game, 'rb') as opened:
            game_ba = bytearray(opened.read())
            del game_ba[0:589]
            codes = str(game_ba[0:40]).replace('\\x81\\x94','#').replace('\\x00',' ').replace('\"','\'').split('\'')[1].split()
            for code in codes:
                if code.lower() in bl:
                    print(code)
                    winsound.PlaySound(sound_file, winsound.SND_FILENAME)
                    break
except KeyboardInterrupt:
    exit('* exiting\n')
