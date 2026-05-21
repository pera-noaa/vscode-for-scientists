;+
; Calibration demo. Run with:
;
;     IDL> .run main
;     IDL> main
;
; (or in a one-shot terminal: `idl -e "main"`)
;-
pro main
    raw_values = [10.0d, 12.0d,  8.5d,  9.0d, 5.0d]
    channels   = [1,     1,      2,     2,    3   ]

    ; Per-channel coefficients (index = channel - 1).
    slopes  = [1.02d, 0.97d, 1.00d]
    offsets = [-0.15d, 0.04d, 0.00d]

    apply_calibration, raw_values, channels, slopes, offsets, calibrated=calibrated
    summary = calibration_summary(calibrated)

    print, 'Calibrated mean: ', summary.mean
    print, '         min:    ', summary.min
    print, '         max:    ', summary.max
end
