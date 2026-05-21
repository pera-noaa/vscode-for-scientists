;+
; Compute summary statistics over a calibrated array.
;
; :Params:
;    values : in, required, type=numeric array
;
; :Returns:
;    Anonymous structure { n, mean, min, max }.
;-
function calibration_summary, values
    return, { $
        n:    n_elements(values), $
        mean: mean(values),       $
        min:  min(values),        $
        max:  max(values)         $
    }
end
