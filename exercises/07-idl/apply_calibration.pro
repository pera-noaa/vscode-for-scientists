;+
; Apply per-channel linear calibration to an array of raw observations.
;
; :Params:
;    raw_values : in, required, type=double array
;       Raw observation values.
;    channels : in, required, type=integer array
;       Channel number for each observation (1-indexed).
;    slopes : in, required, type=double array
;       Slope coefficient per channel (index = channel - 1).
;    offsets : in, required, type=double array
;       Offset coefficient per channel.
;
; :Keywords:
;    calibrated : out, type=double array
;       Output: calibrated values.
;-
pro apply_calibration, raw_values, channels, slopes, offsets, calibrated=calibrated
    n = n_elements(raw_values)
    calibrated = dblarr(n)
    for i = 0, n - 1 do begin
        ch = channels[i]
        calibrated[i] = calibrate_value(raw_values[i], slopes[ch - 1], offsets[ch - 1])
    endfor
end
