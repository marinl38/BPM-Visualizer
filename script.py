import pygame
import time
import win32api
import win32con
import win32gui

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)

pygame.display.set_caption("BPM Visualizer")

pygame.mixer.init()

hwnd, running, intervals_took, font, new_bpm = pygame.display.get_wm_info()["window"], True, [], pygame.font.Font(None, 64), 0
last_sound_played, metronome_interval, metronome_sound = 0, 0, pygame.mixer.Sound("En pause/bpm script/metronome.wav")
is_metronome_on = True

extended_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extended_style | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 255, win32con.LWA_COLORKEY)

while running:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 255), (400, 300), 150, 10)
    bpm_text = font.render(f"BPM: {round(new_bpm)}", True, (255, 255, 255))
    screen.blit(bpm_text, (400 - bpm_text.get_width() // 2, 300 - bpm_text.get_height() // 2))
    if len(intervals_took) >= 10 and time.time() - last_sound_played >= metronome_interval:
        if is_metronome_on:
            metronome_sound.play()
        last_sound_played = time.time()
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            pygame.quit()
        elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            intervals_took.append(time.time())
            if len(intervals_took) >= 2:
                bpm_sum_to_use = sum([intervals_took[i] - intervals_took[i - 1] for i in range(1, len(intervals_took))])
                new_bpm = 60 / (bpm_sum_to_use / (len(intervals_took)))
                metronome_interval = 60 / new_bpm
                print(new_bpm)
                print(round(new_bpm))
        elif event.type == pygame.KEYUP and event.key == pygame.K_a:
            is_metronome_on = not is_metronome_on
    pygame.display.flip()
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

#, scale_factor, 0
#scale_factor = ((time.time() - last_sound_played) % 60 / bpm / 60 / bpm) * 2
    #if scale_factor > 1:
     #   scale_factor = 2 - scale_factor
    #pygame.draw.circle(screen, (0, 255, 255), (400, 300), 100 + int(30 * scale_factor), 10)