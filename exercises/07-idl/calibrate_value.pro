;+
; Linear calibration: y = slope * x + offset.
;
; :Params:
;    raw : in, required, type=numeric
;       Raw observation value.
;    slope : in, required, type=numeric
;       Channel slope coefficient.
;    offset : in, required, type=numeric
;       Channel offset coefficient.
;
; :Returns:
;    Calibrated value (same type as inputs).
;-
function calibrate_value, raw, slope, offset
    return, slope * raw + offset
end
