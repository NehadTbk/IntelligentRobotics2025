#ifndef SONGS_H
#define SONGS_H

#include <Arduino.h>
#include "pitches.h"
#include "config.h"

void playHarryPotterTheme() {
  int melody[] = {
    NOTE_B4, NOTE_E5, NOTE_G5, NOTE_FS5, NOTE_E5, NOTE_B5, NOTE_A5, NOTE_FS5,
    NOTE_E5, NOTE_G5, NOTE_FS5, NOTE_DS5, NOTE_F5, NOTE_B4
  };
  
  int durations[] = {
    4, 4, 8, 4, 2, 4, 2, 4
  };
  
  for (int i = 0; i < 14; i++) {
    int duration = 1000 / durations[i];
    tone(BUZZER, melody[i], duration);
    delay(duration * 1.3);
    noTone(BUZZER);
  }
}

#endif