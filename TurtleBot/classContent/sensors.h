#ifndef SENSORS_H
#define SENSORS_H

#include <Arduino.h>
#include "config.h"

float getBatteryVoltage() {
  int adc_value = analogRead(BDPIN_BAT_PWR_ADC);
  float voltage = map(adc_value, 0, 1023, 0, 330*57/10);
  voltage = voltage / 100.0;
  return voltage;
}

#endif